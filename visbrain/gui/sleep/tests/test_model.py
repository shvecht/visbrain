"""Tests for :mod:`visbrain.gui.sleep.model`."""

from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path

import numpy as np
import pytest


def _install_test_stubs() -> None:
    """Provide lightweight stubs for optional runtime dependencies."""

    if "visbrain.qt" not in sys.modules:
        class _Color:
            def name(self) -> str:  # pragma: no cover - trivial accessor
                return ""

        class _QColorDialog:
            @staticmethod
            def getColor():  # pragma: no cover - trivial accessor
                return _Color()

        class _QFileDialog:
            @staticmethod
            def getOpenFileName(*args, **kwargs):  # pragma: no cover
                return "", ""

            @staticmethod
            def getSaveFileName(*args, **kwargs):  # pragma: no cover
                return "", ""

        qt_module = types.ModuleType("visbrain.qt")
        qt_module.QtWidgets = types.SimpleNamespace(
            QFileDialog=_QFileDialog, QColorDialog=_QColorDialog
        )
        sys.modules["visbrain.qt"] = qt_module

    if "visbrain.io.mneio" not in sys.modules:
        mneio_module = types.ModuleType("visbrain.io.mneio")

        def _mne_switch(*args, **kwargs):  # pragma: no cover - unused in tests
            raise RuntimeError("MNE backend is unavailable in tests")

        mneio_module.mne_switch = _mne_switch
        sys.modules["visbrain.io.mneio"] = mneio_module

    if "visbrain.utils.mesh" not in sys.modules:
        mesh_module = types.ModuleType("visbrain.utils.mesh")

        def vispy_array(data, dtype=np.float32):
            arr = np.asarray(data)
            if not bool(arr.flags.c_contiguous):
                arr = np.ascontiguousarray(arr, dtype=dtype)
            if arr.dtype != dtype:
                arr = arr.astype(dtype, copy=False)
            return arr

        mesh_module.vispy_array = vispy_array
        sys.modules["visbrain.utils.mesh"] = mesh_module

    utils_path = Path(__file__).resolve().parents[3] / "utils"
    if "visbrain.utils" not in sys.modules:
        utils_module = types.ModuleType("visbrain.utils")
        utils_module.__path__ = [str(utils_path)]
        sys.modules["visbrain.utils"] = utils_module
    
    if "visbrain.utils.sleep" not in sys.modules:
        sleep_module = types.ModuleType("visbrain.utils.sleep")
        sleep_module.__path__ = [str(utils_path / "sleep")]
        sys.modules["visbrain.utils.sleep"] = sleep_module
    else:
        sleep_module = sys.modules["visbrain.utils.sleep"]

    if "visbrain.utils.sleep.hypnoprocessing" not in sys.modules:
        hypo_module = types.ModuleType("visbrain.utils.sleep.hypnoprocessing")

        def sleepstats(*args, **kwargs):  # pragma: no cover - deterministic stub
            return {}

        def transient(*args, **kwargs):  # pragma: no cover - deterministic stub
            return [], [], []

        hypo_module.sleepstats = sleepstats
        hypo_module.transient = transient
        sys.modules["visbrain.utils.sleep.hypnoprocessing"] = hypo_module
        sleep_module.hypnoprocessing = hypo_module

    if "visbrain.config" not in sys.modules:
        config_module = types.ModuleType("visbrain.config")

        class _Profiler:
            def __call__(self, *args, **kwargs):  # pragma: no cover - stub
                return None

        config_module.PROFILER = _Profiler()
        sys.modules["visbrain.config"] = config_module

    if "visbrain.io" not in sys.modules:
        io_module = types.ModuleType("visbrain.io")
        io_module.__path__ = [str(Path(__file__).resolve().parents[3] / "io")]
        sys.modules["visbrain.io"] = io_module

    if "visbrain.io.read_sleep" not in sys.modules:
        module_path = Path(__file__).resolve().parents[3] / "io" / "read_sleep.py"
        spec = importlib.util.spec_from_file_location(
            "visbrain.io.read_sleep", module_path
        )
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        sys.modules["visbrain.io.read_sleep"] = module


def _load_sleep_dataset() -> type:
    """Import :class:`SleepDataset` without triggering GUI side-effects."""

    module_path = Path(__file__).resolve().parents[1] / "model.py"
    spec = importlib.util.spec_from_file_location("_sleep_model", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.SleepDataset


_install_test_stubs()
SleepDataset = _load_sleep_dataset()


@pytest.fixture
def sample_dataset():
    """Create a minimal :class:`SleepDataset` for testing."""

    rng = np.random.default_rng(0)
    data = rng.standard_normal((2, 100))
    hypno = np.zeros(100, dtype=np.float32)
    channels = ["Cz", "Pz"]
    return SleepDataset(
        data=data,
        channels=channels,
        sf=100.0,
        hypno=hypno,
        href=["art", "wake", "rem", "n1", "n2", "n3"],
        preload=True,
        use_mne=False,
        downsample=100.0,
        kwargs_mne={},
        annotations=None,
    )


def test_dataset_initial_statistics(sample_dataset):
    """Summary statistics are computed on initialisation."""

    info = sample_dataset.datainfo
    np.testing.assert_allclose(info["mean"], sample_dataset.data.mean(1))
    np.testing.assert_allclose(info["min"], sample_dataset.data.min(1))
    np.testing.assert_allclose(info["max"], sample_dataset.data.max(1))


def test_dataset_len_and_types(sample_dataset):
    """Channels and arrays keep their expected size and dtype."""

    assert len(sample_dataset) == 2
    assert sample_dataset.data.dtype == np.float32
    assert sample_dataset.hypno.dtype == np.float32
    step = sample_dataset.time[1] - sample_dataset.time[0]
    assert step == pytest.approx(1.0 / sample_dataset.sf)


def test_refresh_data_info(sample_dataset):
    """Updating ``data`` recomputes cached statistics."""

    new_data = np.zeros_like(sample_dataset.data)
    new_data[0, :] = 3.0
    new_data[1, :] = -1.0
    sample_dataset.data = new_data
    info = sample_dataset.datainfo
    assert info["mean"][0] == pytest.approx(3.0)
    assert info["mean"][1] == pytest.approx(-1.0)


def test_detection_override(sample_dataset):
    """Custom detection hooks are stored in the dataset."""

    def custom(data, sf, time, hypno):  # pragma: no cover - simple hook
        return np.array([[0, 10]])

    sample_dataset.replace_detection("spindle", custom)
    assert sample_dataset.has_custom_detection("spindle")
    assert sample_dataset.get_detection("spindle") is custom

    with pytest.raises(ValueError):
        sample_dataset.replace_detection("invalid", custom)

    with pytest.raises(AssertionError):
        sample_dataset.replace_detection("sw", None)
