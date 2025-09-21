"""Tests for the :mod:`visbrain._pyqt_module` helpers."""
from __future__ import annotations

from typing import List, Tuple

from visbrain._pyqt_module import _PyQtModule
from visbrain.config import get_config, qt_app
from visbrain.resources import load_icon
from visbrain.qt import QtGui, QtWidgets


class _DummyDescribable:
    def describe_tree(self) -> str:
        return "dummy tree"


class _DummyWindow(QtWidgets.QMainWindow, _PyQtModule):
    def __init__(self) -> None:
        QtWidgets.QMainWindow.__init__(self)
        self.describable = _DummyDescribable()
        self.tree_logs: List[Tuple[str, str]] = []
        _PyQtModule.__init__(
            self,
            to_describe=["describable", self._custom_description],
            icon="brain_icon.svg",
        )
        self.q_widget = self

    def _custom_description(self) -> str:
        return "custom tree"

    def _pyqt_title(self, title, msg, symbol='='):
        self.tree_logs.append((title, msg))
        return super()._pyqt_title(title, msg, symbol)


def test_icon_loader_and_description_hooks():
    """Icons load without temporary files and description hooks execute."""

    cfg = get_config()
    original_show = cfg.show_gui
    cfg.show_gui = False
    try:
        with qt_app(force=True):
            icon = load_icon("brain_icon.svg")
            assert isinstance(icon, QtGui.QIcon)
            assert not icon.isNull()

            window = _DummyWindow()
            window.show()

            descriptions = [msg for _, msg in window.tree_logs]
            assert "dummy tree" in descriptions
            assert "custom tree" in descriptions

            window_icon = window.windowIcon()
            assert isinstance(window_icon, QtGui.QIcon)
            assert not window_icon.isNull()

            window.close()
            window.deleteLater()
    finally:
        cfg.show_gui = original_show
