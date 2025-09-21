"""Unit tests targeting the Sleep controller without launching the façade."""

from __future__ import annotations

import numpy as np
import pytest

try:  # pragma: no cover - optional Qt bindings
    from visbrain.qt import QtWidgets
except ImportError:  # pragma: no cover - Qt not installed
    QtWidgets = None

from visbrain.gui.sleep.controller import SleepController
from visbrain.gui.sleep.model import SleepDataset
from visbrain.gui.sleep.view import SleepView


pytestmark = [
    pytest.mark.skipif(QtWidgets is None, reason="Qt bindings are unavailable"),
]


@pytest.fixture(scope="module")
def controller_instance():
    """Build a controller with synthetic data for signal simulation tests."""
    rng = np.random.default_rng(0)
    data = rng.standard_normal((2, 600)).astype(np.float32)
    hypno = np.zeros(600, dtype=float)
    dataset = SleepDataset(
        data,
        channels=["Cz", "Pz"],
        sf=100.0,
        hypno=hypno,
        href=['art', 'wake', 'rem', 'n1', 'n2', 'n3'],
        preload=True,
        use_mne=False,
        downsample=100.0,
        kwargs_mne={},
        annotations=None,
    )
    view = SleepView()
    return SleepController(dataset, view)


def test_slider_simulation(controller_instance):
    """Trigger slider related slots without GUI interaction."""
    controller = controller_instance
    controller._SigSlStep.setValue(2)
    controller._SigWin.setValue(20)
    controller._fcn_slider_settings()
    controller._fcn_slider_move()


def test_detection_command(controller_instance):
    """Simulate detection combo box changes and command execution."""
    controller = controller_instance
    controller._ToolDetectChan.setCurrentIndex(0)
    controller._ToolDetectType.setCurrentIndex(0)
    controller._fcn_apply_detection()


def test_scoring_window_toggle(controller_instance):
    """Toggle scoring window visibility programmatically."""
    controller = controller_instance
    controller._ScorWinVisible.setChecked(False)
    controller._fcn_scorwin_indicator_toggle()
    controller._ScorWinVisible.setChecked(True)
    controller._fcn_scorwin_indicator_toggle()
