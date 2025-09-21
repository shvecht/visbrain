"""Centralized Qt theme definitions for Visbrain GUIs."""

from __future__ import annotations

from dataclasses import dataclass
import math
import weakref
from typing import Callable, Dict, Iterable, Mapping, Optional

from visbrain.config import get_config
from visbrain.qt import QtCore, QtGui, QtWidgets

try:
    Signal = QtCore.Signal  # type: ignore[attr-defined]
except AttributeError:  # pragma: no cover - PyQt5 fallback
    Signal = QtCore.pyqtSignal  # type: ignore[attr-defined]

__all__ = [
    "ThemeMetrics",
    "ThemeDefinition",
    "ThemeManager",
    "theme_manager",
]

_BASE_DPI = 96.0


@dataclass(frozen=True)
class ThemeMetrics:
    """Scaled metrics used by the Qt stylesheet."""

    scale: float
    padding: int
    radius: int
    border: int
    spacing: int
    font_size: float
    small_font_size: float


@dataclass(frozen=True)
class ThemeDefinition:
    """Description of a named Visbrain theme."""

    name: str
    title: str
    palette_values: Mapping[QtGui.QPalette.ColorRole, str]
    accent: str
    base_font_size: float = 10.0
    base_padding: int = 6
    base_radius: int = 6
    base_spacing: int = 8

    def metrics(self, scale: float) -> ThemeMetrics:
        padding = max(4, round(self.base_padding * scale))
        radius = max(3, round(self.base_radius * scale))
        border = max(1, round(scale))
        spacing = max(4, round(self.base_spacing * scale))
        font_size = max(7.0, self.base_font_size * scale)
        small_font = max(6.0, (self.base_font_size - 1.0) * scale)
        return ThemeMetrics(
            scale,
            padding,
            radius,
            border,
            spacing,
            font_size,
            small_font,
        )

    def palette(self) -> QtGui.QPalette:
        palette = QtGui.QPalette()
        for group in (QtGui.QPalette.Active, QtGui.QPalette.Inactive):
            for role, value in self.palette_values.items():
                palette.setColor(group, role, QtGui.QColor(value))
        for role, value in self.palette_values.items():
            base_color = QtGui.QColor(value)
            if role in (
                QtGui.QPalette.WindowText,
                QtGui.QPalette.Text,
                QtGui.QPalette.ButtonText,
                QtGui.QPalette.HighlightedText,
            ):
                disabled = QtGui.QColor(base_color)
                disabled.setAlphaF(0.55)
            else:
                disabled = base_color.lighter(115)
            palette.setColor(QtGui.QPalette.Disabled, role, disabled)
        return palette

    def build_stylesheet(self, palette: QtGui.QPalette, metrics: ThemeMetrics) -> str:
        window = palette.color(QtGui.QPalette.Window).name()
        text = palette.color(QtGui.QPalette.WindowText).name()
        base = palette.color(QtGui.QPalette.Base).name()
        alt_base = palette.color(QtGui.QPalette.AlternateBase).name()
        button = palette.color(QtGui.QPalette.Button).name()
        highlight = palette.color(QtGui.QPalette.Highlight).name()
        highlight_text = palette.color(QtGui.QPalette.HighlightedText).name()
        tooltip_base = palette.color(QtGui.QPalette.ToolTipBase).name()
        tooltip_text = palette.color(QtGui.QPalette.ToolTipText).name()
        mid = palette.color(QtGui.QPalette.Mid).name()
        shadow = palette.color(QtGui.QPalette.Shadow).name()
        spacing = metrics.spacing
        padding = metrics.padding
        radius = metrics.radius
        border = metrics.border
        font_size = metrics.font_size
        small_font = metrics.small_font_size
        min_scroll = max(6, math.ceil(padding * 0.9))

        return f"""
        QWidget {{
            color: {text};
            background-color: {window};
            font-size: {font_size:.1f}pt;
        }}
        QToolTip {{
            color: {tooltip_text};
            background-color: {tooltip_base};
            border: {border}px solid {self.accent};
            padding: {max(2, padding // 2)}px;
            border-radius: {max(2, radius // 2)}px;
        }}
        QStatusBar {{
            font-size: {small_font:.1f}pt;
        }}
        QLineEdit, QPlainTextEdit, QTextEdit, QSpinBox, QDoubleSpinBox,
        QComboBox, QListView, QTreeView, QTableView {{
            background-color: {base};
            selection-background-color: {highlight};
            selection-color: {highlight_text};
            border: {border}px solid {mid};
            border-radius: {radius}px;
            padding: {max(2, padding // 2)}px;
        }}
        QComboBox::drop-down {{
            border-left: {border}px solid {mid};
        }}
        QGroupBox {{
            border: {border}px solid {mid};
            border-radius: {radius}px;
            margin-top: {padding + radius}px;
        }}
        QGroupBox::title {{
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0px {padding}px;
        }}
        QPushButton {{
            background-color: {button};
            border: {border}px solid {mid};
            border-radius: {radius}px;
            padding: {padding}px {padding + 4}px;
        }}
        QPushButton:hover {{
            border-color: {self.accent};
        }}
        QPushButton:pressed {{
            background-color: {alt_base};
        }}
        QPushButton:default {{
            background-color: {self.accent};
            color: {highlight_text};
            border-color: {self.accent};
        }}
        QTabWidget::pane {{
            border: {border}px solid {mid};
            border-radius: {radius}px;
            padding-top: {max(2, padding // 2)}px;
        }}
        QTabBar::tab {{
            background: {button};
            border: {border}px solid transparent;
            border-top-left-radius: {radius}px;
            border-top-right-radius: {radius}px;
            margin-right: {max(2, spacing // 2)}px;
            padding: {max(2, padding // 2)}px {padding + 2}px;
        }}
        QTabBar::tab:selected {{
            background: {base};
            border-color: {mid};
        }}
        QHeaderView::section {{
            background-color: {button};
            color: {text};
            padding: {max(2, padding // 2)}px;
            border: {border}px solid {mid};
        }}
        QScrollBar:vertical {{
            width: {min_scroll}px;
            margin: {padding}px 0 {padding}px 0;
        }}
        QScrollBar:horizontal {{
            height: {min_scroll}px;
            margin: 0 {padding}px 0 {padding}px;
        }}
        QScrollBar::handle {{
            background-color: {mid};
            border-radius: {max(2, radius // 2)}px;
        }}
        QScrollBar::handle:hover {{
            background-color: {self.accent};
        }}
        QScrollBar::add-line, QScrollBar::sub-line {{
            background: none;
            border: none;
        }}
        QMenu {{
            background-color: {window};
            border: {border}px solid {mid};
            padding: {max(2, padding // 2)}px;
        }}
        QMenu::item:selected {{
            background-color: {highlight};
            color: {highlight_text};
        }}
        QMenu::separator {{
            height: {border}px;
            background: {shadow};
            margin: {max(2, padding // 2)}px 0;
        }}
        """.strip()


class _ThemeMenuController(QtCore.QObject):
    """Book-keeping helper that keeps menu actions in sync with the manager."""

    def __init__(
        self,
        owner: Optional[QtWidgets.QWidget],
        menu: QtWidgets.QMenu,
        manager: "ThemeManager",
    ) -> None:
        super().__init__(menu)
        self._owner_ref: Callable[[], Optional[QtWidgets.QWidget]]
        if owner is not None:
            self._owner_ref = weakref.ref(owner)
        else:
            self._owner_ref = lambda: None
        self._manager = manager
        self.menu = menu
        self._group = QtGui.QActionGroup(menu)
        self._group.setExclusive(True)
        self._actions: Dict[str, QtGui.QAction] = {}
        for definition in manager.definitions:
            action = QtGui.QAction(definition.title, menu)
            action.setCheckable(True)
            action.setData(definition.name)
            self._group.addAction(action)
            menu.addAction(action)
            self._actions[definition.name] = action
        self._group.triggered.connect(self._on_triggered)
        menu.aboutToShow.connect(self._sync_state)
        manager.themeChanged.connect(self._sync_state)
        self._sync_state()

    @QtCore.Slot()
    def _sync_state(self) -> None:
        current = self._manager.current
        for name, action in self._actions.items():
            block = action.blockSignals(True)
            try:
                action.setChecked(name == current)
            finally:
                action.blockSignals(block)

    @QtCore.Slot(QtGui.QAction)
    def _on_triggered(self, action: QtGui.QAction) -> None:
        if action is None:
            return
        name = action.data()
        if not isinstance(name, str):
            name = str(name)
        widget = self._owner_ref()
        self._manager.set_theme(name, widget=widget)


class ThemeManager(QtCore.QObject):
    """Coordinate Qt application styling across Visbrain GUIs."""

    themeChanged = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self._definitions: Dict[str, ThemeDefinition] = {}
        self._current: Optional[str] = None
        self._metrics: Optional[ThemeMetrics] = None
        self._install_default_definitions()

    # ------------------------------------------------------------------
    # Theme definitions
    # ------------------------------------------------------------------
    def _install_default_definitions(self) -> None:
        dark_palette: Dict[QtGui.QPalette.ColorRole, str] = {
            QtGui.QPalette.Window: "#15171b",
            QtGui.QPalette.WindowText: "#f1f3f5",
            QtGui.QPalette.Base: "#0f1115",
            QtGui.QPalette.AlternateBase: "#1b1e24",
            QtGui.QPalette.ToolTipBase: "#272b33",
            QtGui.QPalette.ToolTipText: "#f1f3f5",
            QtGui.QPalette.Text: "#f1f3f5",
            QtGui.QPalette.Button: "#1f232a",
            QtGui.QPalette.ButtonText: "#f1f3f5",
            QtGui.QPalette.BrightText: "#ff6b6b",
            QtGui.QPalette.Highlight: "#3d7eff",
            QtGui.QPalette.HighlightedText: "#ffffff",
            QtGui.QPalette.Link: "#82b1ff",
            QtGui.QPalette.LinkVisited: "#bb86fc",
            QtGui.QPalette.Light: "#262a32",
            QtGui.QPalette.Midlight: "#22252c",
            QtGui.QPalette.Dark: "#0b0d10",
            QtGui.QPalette.Mid: "#272b33",
            QtGui.QPalette.Shadow: "#060708",
        }
        light_palette: Dict[QtGui.QPalette.ColorRole, str] = {
            QtGui.QPalette.Window: "#f5f6fa",
            QtGui.QPalette.WindowText: "#1c1f24",
            QtGui.QPalette.Base: "#ffffff",
            QtGui.QPalette.AlternateBase: "#eef0f4",
            QtGui.QPalette.ToolTipBase: "#ffffff",
            QtGui.QPalette.ToolTipText: "#1c1f24",
            QtGui.QPalette.Text: "#1c1f24",
            QtGui.QPalette.Button: "#f0f2f6",
            QtGui.QPalette.ButtonText: "#1c1f24",
            QtGui.QPalette.BrightText: "#e53935",
            QtGui.QPalette.Highlight: "#316cff",
            QtGui.QPalette.HighlightedText: "#ffffff",
            QtGui.QPalette.Link: "#1f5bd8",
            QtGui.QPalette.LinkVisited: "#6c3ad2",
            QtGui.QPalette.Light: "#ffffff",
            QtGui.QPalette.Midlight: "#dfe3eb",
            QtGui.QPalette.Dark: "#b7bcc6",
            QtGui.QPalette.Mid: "#c8ccd4",
            QtGui.QPalette.Shadow: "#a6abb5",
        }
        self._definitions = {
            definition.name: definition
            for definition in (
                ThemeDefinition(
                    name="dark",
                    title="Dark",
                    palette_values=dark_palette,
                    accent="#3d7eff",
                ),
                ThemeDefinition(
                    name="light",
                    title="Light",
                    palette_values=light_palette,
                    accent="#316cff",
                ),
            )
        }

    @property
    def definitions(self) -> Iterable[ThemeDefinition]:
        return self._definitions.values()

    def get_definition(self, name: str) -> ThemeDefinition:
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise ValueError(f"Unknown theme {name!r}") from exc

    # ------------------------------------------------------------------
    # Metrics helpers
    # ------------------------------------------------------------------
    def _resolve_scale(self, widget: Optional[QtWidgets.QWidget]) -> float:
        screen = None
        if isinstance(widget, QtWidgets.QWidget):
            screen = widget.screen()
        if screen is None:
            app = QtGui.QGuiApplication.instance()
            if app is not None:
                screen = app.primaryScreen()
        if screen is None:
            return 1.0
        dpi = screen.logicalDotsPerInch() or _BASE_DPI
        scale = dpi / _BASE_DPI
        return max(0.75, min(2.0, scale))

    def metrics_for(self, widget: Optional[QtWidgets.QWidget] = None) -> ThemeMetrics:
        definition = self.get_definition(self.current)
        scale = self._resolve_scale(widget)
        return definition.metrics(scale)

    @property
    def metrics(self) -> Optional[ThemeMetrics]:
        return self._metrics

    # ------------------------------------------------------------------
    # Application helpers
    # ------------------------------------------------------------------
    @property
    def current(self) -> str:
        if self._current is None:
            config = get_config()
            candidate = getattr(config, "theme", None) or "dark"
            if candidate not in self._definitions:
                candidate = "dark"
            self._current = candidate
        return self._current

    def ensure_application_theme(self) -> None:
        app = QtWidgets.QApplication.instance()
        if app is None:
            return
        self._apply_theme(app, widget=None)

    def apply(self, widget: Optional[QtWidgets.QWidget] = None) -> None:
        app = QtWidgets.QApplication.instance()
        self._apply_theme(app, widget)

    def _apply_theme(
        self,
        app: Optional[QtWidgets.QApplication],
        widget: Optional[QtWidgets.QWidget],
    ) -> None:
        definition = self.get_definition(self.current)
        scale = self._resolve_scale(widget if widget is not None else app)
        metrics = definition.metrics(scale)
        palette = definition.palette()
        stylesheet = definition.build_stylesheet(palette, metrics)
        font = QtWidgets.QApplication.font() if app is not None else QtGui.QFont()
        if font is None:
            font = QtGui.QFont()
        font.setPointSizeF(metrics.font_size)
        self._metrics = metrics
        if app is not None:
            style_factory = getattr(QtWidgets, "QStyleFactory", None)
            if style_factory is not None:
                fusion = style_factory.create("Fusion")
                if fusion is not None:
                    app.setStyle(fusion)
            app.setPalette(palette)
            app.setFont(font)
            app.setStyleSheet(stylesheet)
        if isinstance(widget, QtWidgets.QWidget):
            widget.setPalette(palette)
            widget.setFont(font)
            widget.setStyleSheet(app.styleSheet() if app is not None else stylesheet)
            widget.style().polish(widget)

    # ------------------------------------------------------------------
    # Theme switching
    # ------------------------------------------------------------------
    def set_theme(
        self,
        name: str,
        *,
        widget: Optional[QtWidgets.QWidget] = None,
    ) -> None:
        if name not in self._definitions:
            raise ValueError(f"Unknown theme {name!r}")
        if name == self.current and widget is None:
            # Applying the same theme only needs to refresh the widget palette.
            self.apply(widget=widget)
            return
        self._current = name
        config = get_config()
        config.theme = name
        self.apply(widget=widget)
        self.themeChanged.emit(name)

    def install_menu(
        self,
        owner: Optional[QtWidgets.QWidget],
        parent_menu: QtWidgets.QMenu,
        *,
        title: str = "Theme",
        before: Optional[QtGui.QAction] = None,
    ) -> _ThemeMenuController:
        menu = QtWidgets.QMenu(title, parent_menu)
        if before is not None:
            parent_menu.insertMenu(before, menu)
        else:
            parent_menu.addMenu(menu)
        controller = _ThemeMenuController(owner, menu, self)
        return controller


theme_manager = ThemeManager()
