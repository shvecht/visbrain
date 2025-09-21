"""Shared fixtures for the :mod:`visbrain.gui.sleep` test suite."""

from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path
from typing import Iterator, TYPE_CHECKING

import numpy as np
import pytest

if TYPE_CHECKING:  # pragma: no cover - imported for type checking only
    from visbrain.gui import Sleep


# ---------------------------------------------------------------------------
# Lightweight stubs for optional runtime dependencies
# ---------------------------------------------------------------------------

def _install_test_stubs() -> None:
    """Provide lightweight stand-ins for optional modules."""

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

        def _mne_switch(*args, **kwargs):  # pragma: no cover - deterministic stub
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

        def configure_headless():  # pragma: no cover - stub for fixture import
            return types.SimpleNamespace(show_pyqt_app=False, show_gui=False)

        config_module.PROFILER = _Profiler()
        config_module.configure_headless = configure_headless
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


_install_test_stubs()

# Import after patching optional dependencies so the modules load deterministically.
from visbrain.gui.sleep.model import SleepDataset  # noqa: E402

try:  # pragma: no cover - optional Qt bindings
    from visbrain.gui.sleep.controller import SleepController  # noqa: E402
    from visbrain.gui.sleep.view import SleepView  # noqa: E402
except Exception:  # pragma: no cover - Qt not installed
    SleepController = SleepView = None

try:  # pragma: no cover - optional Qt bindings
    from visbrain.qt import QtWidgets  # noqa: E402
except ImportError:  # pragma: no cover - Qt not installed
    QtWidgets = None


@pytest.fixture(scope="session")
def synthetic_sleep_arrays() -> tuple[np.ndarray, np.ndarray, list[str], float]:
    """Return deterministic arrays used across tests."""

    rng = np.random.default_rng(1337)
    data = rng.standard_normal((2, 400)).astype(np.float32)
    hypno = np.zeros(400, dtype=np.float32)
    hypno[50:100] = 1
    hypno[200:260] = 4
    channels = ["Cz", "Pz"]
    sf = 100.0
    return data, hypno, channels, sf


@pytest.fixture
def sleep_dataset(synthetic_sleep_arrays) -> SleepDataset:
    """Instantiate :class:`SleepDataset` with in-memory arrays."""

    data, hypno, channels, sf = synthetic_sleep_arrays
    return SleepDataset(
        data=data.copy(),
        channels=channels,
        sf=sf,
        hypno=hypno.copy(),
        href=["art", "wake", "rem", "n1", "n2", "n3"],
        preload=True,
        use_mne=False,
        downsample=sf,
        kwargs_mne={},
        annotations=None,
    )


@pytest.fixture
def sleep_view(qtbot) -> Iterator[SleepView]:
    """Provide a :class:`SleepView` widget managed by ``qtbot``."""

    if QtWidgets is None or SleepView is None:
        # pragma: no cover - optional dependency guard
        pytest.skip("Qt bindings are unavailable")
    view = SleepView()
    qtbot.addWidget(view)
    yield view
    view.close()


@pytest.fixture
def sleep_controller(
    sleep_dataset: SleepDataset, sleep_view: SleepView
) -> Iterator[SleepController]:
    """Build a controller connected to the synthetic dataset and view."""

    if SleepController is None:  # pragma: no cover - optional dependency guard
        pytest.skip("Qt bindings are unavailable")

    controller = SleepController(sleep_dataset, sleep_view, axis=True)
    yield controller


@pytest.fixture
def sleep_facade(
    synthetic_sleep_arrays, qtbot
) -> Iterator["Sleep"]:
    """End-to-end :class:`Sleep` instance wired to synthetic arrays."""

    if QtWidgets is None or SleepController is None:
        # pragma: no cover - optional dependency guard
        pytest.skip("Qt bindings are unavailable")

    from visbrain.gui import Sleep

    data, hypno, channels, sf = synthetic_sleep_arrays
    sleep = Sleep(
        data=data.copy(),
        hypno=hypno.copy(),
        channels=channels,
        sf=sf,
        downsample=sf,
        preload=True,
        use_mne=False,
        axis=True,
    )
    qtbot.addWidget(sleep.view)
    yield sleep
    sleep.view.close()
