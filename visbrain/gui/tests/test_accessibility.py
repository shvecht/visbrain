"""Accessibility smoke tests for the main Qt GUIs."""

from __future__ import annotations

import numpy as np
import pytest

from visbrain.gui.brain import Brain
from visbrain.gui.signal import Signal
from visbrain.gui.sleep import Sleep
from visbrain.qt import QtCore


@pytest.fixture
def brain_app(qtbot):
    brain = Brain(bgcolor='black', verbose=None)
    qtbot.addWidget(brain)
    brain.show()
    qtbot.waitUntil(lambda: brain.isVisible())
    yield brain
    brain.close()


@pytest.fixture
def signal_app(qtbot):
    data = np.zeros((2, 64), dtype=np.float32)
    time = np.linspace(0.0, 1.0, data.shape[-1], dtype=np.float32)
    signal = Signal(data=data, time=time, sf=1.0, verbose=None)
    qtbot.addWidget(signal)
    signal.show()
    qtbot.waitUntil(lambda: signal.isVisible())
    yield signal
    signal.close()


@pytest.fixture
def sleep_app(qtbot):
    data = np.zeros((1, 200), dtype=np.float32)
    hypno = np.zeros(200, dtype=np.int32)
    sleep = Sleep(data=data, sf=1.0, hypno=hypno, channels=['Cz'])
    view = sleep.view
    qtbot.addWidget(view)
    view.show()
    qtbot.waitUntil(lambda: view.isVisible())
    yield sleep
    view.close()


@pytest.mark.parametrize(
    "shortcut_key",
    [QtCore.Qt.Key_D],
    ids=lambda key: f"Ctrl+{chr(key)}",
)
def test_brain_focus_and_shortcut(brain_app, qtbot, shortcut_key):
    brain = brain_app
    quick = brain.QuickSettings
    assert quick.accessibleName()
    assert quick.accessibleDescription()
    quick.setFocus()
    qtbot.waitUntil(quick.hasFocus)

    qtbot.keyClick(brain, QtCore.Qt.Key_Tab)
    assert brain.focusWidget() is brain._obj_type_lst

    initially_visible = brain.q_widget.isVisible()
    qtbot.keyClick(brain, shortcut_key, modifier=QtCore.Qt.ControlModifier)
    qtbot.waitUntil(lambda: brain.q_widget.isVisible() is not initially_visible)
    qtbot.keyClick(brain, shortcut_key, modifier=QtCore.Qt.ControlModifier)
    qtbot.waitUntil(lambda: brain.q_widget.isVisible() is initially_visible)

    assert brain.statusbar.accessibleDescription()
    assert brain.userRotation.accessibleDescription()
    assert brain.view.canvas.native.accessibleName()
    assert brain._csView.canvas.native.accessibleName()


def test_signal_focus_and_shortcut(signal_app, qtbot):
    signal = signal_app
    quick = signal.QuickSettings
    assert quick.accessibleName()
    quick.setFocus()
    qtbot.waitUntil(quick.hasFocus)

    qtbot.keyClick(signal, QtCore.Qt.Key_Tab)
    assert signal.focusWidget() is signal._sig_title

    initially_visible = signal.q_widget.isVisible()
    qtbot.keyClick(signal, QtCore.Qt.Key_D, modifier=QtCore.Qt.ControlModifier)
    qtbot.waitUntil(lambda: signal.q_widget.isVisible() is not initially_visible)
    qtbot.keyClick(signal, QtCore.Qt.Key_D, modifier=QtCore.Qt.ControlModifier)
    qtbot.waitUntil(lambda: signal.q_widget.isVisible() is initially_visible)

    assert signal._grid_canvas.canvas.native.accessibleName()
    assert signal._signal_canvas.canvas.native.accessibleName()


def test_sleep_focus_and_shortcut(sleep_app, qtbot):
    sleep = sleep_app
    view = sleep.view
    quick = view.QuickSettings
    assert quick.accessibleName()
    quick.setFocus()
    qtbot.waitUntil(quick.hasFocus)

    qtbot.keyClick(view, QtCore.Qt.Key_Tab)
    assert view.focusWidget() is view._stacked_panels

    initially_visible = view.q_widget.isVisible()
    qtbot.keyClick(view, QtCore.Qt.Key_D, modifier=QtCore.Qt.ControlModifier)
    qtbot.waitUntil(lambda: view.q_widget.isVisible() is not initially_visible)
    qtbot.keyClick(view, QtCore.Qt.Key_D, modifier=QtCore.Qt.ControlModifier)
    qtbot.waitUntil(lambda: view.q_widget.isVisible() is initially_visible)

    assert view._specCanvas.canvas.native.accessibleName()
    assert view._hypCanvas.canvas.native.accessibleName()
    assert view._topoCanvas.canvas.native.accessibleName()
    assert view._TimeAxis.canvas.native.accessibleName()
