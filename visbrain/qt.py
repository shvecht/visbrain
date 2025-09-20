"""Qt binding compatibility layer for Visbrain.

This module centralizes access to Qt modules so that the rest of the codebase
can rely on a single import location while we transition away from the PyQt5
API.  It prefers the PySide6 binding but gracefully falls back to PyQt5 for
legacy environments.
"""
from __future__ import annotations

import atexit
import importlib
import logging
import weakref
from types import SimpleNamespace
from typing import Optional

logger = logging.getLogger("visbrain")

# Exposed names; they are populated once a binding is found.
QtCore = None  # type: ignore[assignment]
QtGui = None  # type: ignore[assignment]
QtWidgets = None  # type: ignore[assignment]
Qt = None  # type: ignore[assignment]

QT_API = None

_REQUIRED_MODULES = ("QtCore", "QtGui", "QtWidgets")
_OPTIONAL_MODULES = ("QtSvg", "QtPrintSupport")
_BINDINGS = ("PySide6", "PyQt5")


def _build_qt_namespace(modules: dict[str, object]) -> SimpleNamespace:
    """Aggregate Qt classes into a PyQt5-like ``Qt`` namespace."""
    namespace = SimpleNamespace()
    for module in modules.values():
        if module is None:
            continue
        for attr in dir(module):
            if attr.startswith("_"):
                continue
            value = getattr(module, attr)
            # Limit ourselves to Qt enums, classes and helper namespaces.
            if attr[0].isupper() or attr.startswith("Qt"):
                setattr(namespace, attr, value)
    return namespace


def _import_binding() -> None:
    """Import the preferred Qt binding and populate module globals."""
    global QtCore, QtGui, QtWidgets, Qt, QT_API

    for binding in _BINDINGS:
        modules: dict[str, object] = {}
        try:
            for name in _REQUIRED_MODULES:
                modules[name] = importlib.import_module(f"{binding}.{name}")
        except ImportError:
            continue

        for name in _OPTIONAL_MODULES:
            try:
                modules[name] = importlib.import_module(f"{binding}.{name}")
            except ImportError:
                modules[name] = None

        QtCore = modules["QtCore"]
        QtGui = modules["QtGui"]
        QtWidgets = modules["QtWidgets"]
        Qt = _build_qt_namespace(modules)
        QT_API = binding
        logger.debug("Using %s Qt binding", binding)
        return

    raise ImportError(
        "Unable to import a supported Qt binding. Install PySide6 (preferred) "
        "or PyQt5."
    )


_import_binding()

_QAPP_CLEANUP_REGISTERED = False


class _QObjectLifecycle:
    """Track whether a :class:`~QtCore.QObject` is still alive."""

    def __init__(self) -> None:
        self._ref: weakref.ReferenceType[QtCore.QObject] | None = None
        self._alive = False

    def watch(self, obj: QtCore.QObject) -> None:
        """Start tracking *obj* and mark it as alive."""

        if obj is None:
            return
        current = self._ref() if self._ref is not None else None
        if current is obj and self._alive:
            return

        def _mark_dead(*_args: object) -> None:
            self._alive = False
            self._ref = None

        try:
            obj.destroyed.connect(_mark_dead)  # type: ignore[union-attr]
        except Exception:  # pragma: no cover - defensive fallback
            pass
        self._ref = weakref.ref(obj)
        self._alive = True

    def get(self) -> Optional[QtCore.QObject]:
        """Return the tracked object if it is still alive."""

        if not self._alive or self._ref is None:
            return None
        instance = self._ref()
        if instance is None:
            self._alive = False
            self._ref = None
            return None
        return instance


_QAPP_LIFECYCLE = _QObjectLifecycle()


def _shutdown_qapplication() -> None:
    """Attempt to gracefully close the tracked Qt application."""

    if QtCore.QCoreApplication.closingDown():  # pragma: no cover - during exit
        return

    tracked = _QAPP_LIFECYCLE.get()
    app = tracked if isinstance(tracked, QtWidgets.QApplication) else None
    if app is None:
        app = QtWidgets.QApplication.instance()
    if app is None:
        return

    set_quit = getattr(QtWidgets.QApplication, "setQuitOnLastWindowClosed", None)
    if callable(set_quit):  # pragma: no branch - guard missing Qt API
        try:
            set_quit(True)
        except Exception:  # pragma: no cover - best effort cleanup
            pass

    quit_method = getattr(app, "quit", None)
    if callable(quit_method):
        quit_method()


def guard_qapp_lifecycle() -> None:
    """Configure the Qt application for deterministic shutdown semantics."""

    set_quit = getattr(QtWidgets.QApplication, "setQuitOnLastWindowClosed", None)
    if callable(set_quit):  # pragma: no branch - guard missing Qt API
        try:
            set_quit(False)
        except Exception:  # pragma: no cover - best effort cleanup
            pass
    app = QtWidgets.QApplication.instance()
    if app is not None:
        _QAPP_LIFECYCLE.watch(app)

    global _QAPP_CLEANUP_REGISTERED
    if not _QAPP_CLEANUP_REGISTERED:
        atexit.register(_shutdown_qapplication)
        _QAPP_CLEANUP_REGISTERED = True


__all__ = ["QtCore", "QtGui", "QtWidgets", "Qt", "QT_API", "guard_qapp_lifecycle"]
