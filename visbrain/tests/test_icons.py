"""Tests related to packaged GUI icons."""

from __future__ import annotations

import pytest


@pytest.mark.gui
def test_module_icon_uses_packaged_resource(monkeypatch):
    """The generic Qt module should load icons from packaged data."""

    try:
        from visbrain.qt import QtWidgets
    except ImportError:
        pytest.skip("Qt bindings are unavailable")

    from visbrain._pyqt_module import _PyQtModule
    from visbrain.config import CONFIG

    class DummyWindow(_PyQtModule, QtWidgets.QMainWindow):
        """Minimal window exposing the ``show`` helper."""

        def __init__(self) -> None:
            QtWidgets.QMainWindow.__init__(self)
            _PyQtModule.__init__(self, icon="brain_icon.svg", show_settings=False)

    # Guard against accidental GUI execution inside tests.
    monkeypatch.setattr(CONFIG, "show_pyqt_app", False)

    window = DummyWindow()
    window.show()

    assert not window.windowIcon().isNull()
