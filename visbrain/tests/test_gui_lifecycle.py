"""Smoke tests covering Qt window lifecycle management."""
from __future__ import annotations

import numpy as np
import pytest

try:  # pragma: no cover - guarded import for optional Qt stack
    from visbrain.qt import QtGui, QtWidgets
    from visbrain.config import qt_app
    from visbrain.gui import Brain, Sleep
    from visbrain._pyqt_module import _PyQtModule
except ImportError as exc:  # pragma: no cover - Qt not installed
    pytest.skip(f"Qt bindings are unavailable: {exc}", allow_module_level=True)


pytestmark = pytest.mark.gui


def _coerce_font_weight_api() -> None:
    """Normalize ``QFont.setWeight`` to accept integers on PySide6."""

    original_set_weight = QtGui.QFont.setWeight

    def _patched(self: QtGui.QFont, weight) -> None:  # type: ignore[override]
        if isinstance(weight, int):
            try:
                weight = QtGui.QFont.Weight(weight)
            except ValueError:
                weight = QtGui.QFont.Weight.Normal
        original_set_weight(self, weight)

    QtGui.QFont.setWeight = _patched


_coerce_font_weight_api()

# PyQt generated UI code references QtWidgets.QAction; expose the QtGui variant.
if not hasattr(QtWidgets, "QAction"):
    QtWidgets.QAction = QtGui.QAction  # type: ignore[attr-defined]


def _patch_constructor(cls):
    original_init = cls.__init__

    def _stub_init(self, *args, **kwargs) -> None:
        _PyQtModule.__init__(self, verbose=kwargs.get("verbose"))
        QtWidgets.QMainWindow.__init__(self)

    cls.__init__ = _stub_init  # type: ignore[assignment]
    return original_init


def _assert_guard_enabled() -> None:
    """Validate that the lifecycle guard disabled implicit Qt shutdown."""

    get_flag = getattr(QtWidgets.QApplication, "quitOnLastWindowClosed", None)
    if callable(get_flag):
        assert get_flag() is False


def test_sleep_window_lifecycle() -> None:
    """Sleep should initialize and close cleanly under the lifecycle guard."""

    data = np.zeros((2, 300), dtype=np.float32)
    hypno = np.zeros(300, dtype=np.float32)

    original_init = _patch_constructor(Sleep)
    with qt_app(force=True, reset=True) as app:
        assert app is not None
        _assert_guard_enabled()

        window = Sleep(data=data, hypno=hypno, sf=100.0, axis=False, verbose=None)
        window.close()
        window.deleteLater()
    Sleep.__init__ = original_init  # type: ignore[assignment]


def test_brain_window_lifecycle() -> None:
    """Brain should initialize and close cleanly under the lifecycle guard."""

    original_init = _patch_constructor(Brain)
    with qt_app(force=True, reset=True) as app:
        assert app is not None
        _assert_guard_enabled()

        window = Brain(verbose=None)
        window.close()
        window.deleteLater()
    Brain.__init__ = original_init  # type: ignore[assignment]
