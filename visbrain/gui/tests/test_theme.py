"""Tests covering the runtime Qt theme integration."""

from __future__ import annotations

import numpy as np

from visbrain.config import get_config, qt_app, vispy_app
from visbrain.gui.signal import Signal
from visbrain.gui.theme import theme_manager
from visbrain.gui.tests._screenshot import capture_screenshot
from visbrain.qt import QtCore, QtGui, QtWidgets


def _restore_theme(name: str) -> None:
    """Best-effort restore helper used by the tests."""

    try:
        theme_manager.set_theme(name)
    except Exception:  # pragma: no cover - defensive fallback
        pass


def test_theme_integration_workflow():
    """Exercise runtime theming, menu integration and screenshot styling."""

    cfg = get_config()
    original = cfg.theme
    palette_changes: list[str] = []
    theme_manager.themeChanged.connect(palette_changes.append)

    try:
        with qt_app(force=True, reset=True) as app:
            theme_manager.set_theme("light")
            definition = theme_manager.get_definition("light")
            expected = QtGui.QColor(
                definition.palette_values[QtGui.QPalette.Window]
            ).name().lower()
            assert app is not None
            assert (
                app.palette().color(QtGui.QPalette.Window).name().lower() == expected
            )
            theme_manager.set_theme("dark")

        assert palette_changes[:2] == ["light", "dark"]

        data = np.tile(np.linspace(-1.0, 1.0, 200, dtype=np.float32), (2, 1))
        with qt_app(force=True, reset=True), vispy_app(force=True, reset=True):
            gui = Signal(data, enable_grid=False, display_grid=False)
            try:
                menu_titles = [
                    action.menu().title()
                    for action in gui.menuDisplay.actions()
                    if action.menu() is not None
                ]
                assert "Theme" in menu_titles
            finally:
                gui.close()

        class _Preview(QtWidgets.QMainWindow):
            def __init__(self) -> None:
                super().__init__()
                central = QtWidgets.QWidget(self)
                layout = QtWidgets.QVBoxLayout(central)
                header = QtWidgets.QLabel("Theme preview", central)
                header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                button = QtWidgets.QPushButton("Toggle", central)
                layout.addWidget(header)
                layout.addWidget(button)
                central.setLayout(layout)
                self.setCentralWidget(central)
                self.resize(320, 200)

        def _make_window() -> QtWidgets.QMainWindow:
            window = _Preview()
            theme_manager.apply(widget=window)
            return window

        theme_manager.set_theme("dark")
        dark = capture_screenshot(
            _make_window, size=(640, 360), use_vispy=False
        )
        theme_manager.set_theme("light")
        light = capture_screenshot(
            _make_window, size=(640, 360), use_vispy=False
        )

        assert dark.shape == light.shape
        assert not np.array_equal(dark, light)
        delta = np.abs(dark.astype(np.int16) - light.astype(np.int16))
        assert float(delta.mean()) > 0.5
    finally:
        try:
            theme_manager.themeChanged.disconnect(palette_changes.append)
        except RuntimeError:
            pass
        _restore_theme(original)
