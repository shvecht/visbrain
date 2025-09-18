"""Qt binding compatibility layer for Visbrain.

This module centralizes access to Qt modules so that the rest of the codebase
can rely on a single import location while we transition away from the PyQt5
API.  It prefers the PySide6 binding but gracefully falls back to PyQt5 for
legacy environments.
"""
from __future__ import annotations

import importlib
import logging
from types import SimpleNamespace

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

__all__ = ["QtCore", "QtGui", "QtWidgets", "Qt", "QT_API"]
