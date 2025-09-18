"""Pytest configuration for Visbrain.

This module centralizes headless Qt configuration and test markers so all
collected test modules behave consistently regardless of their location in the
repository.
"""
from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path
from typing import Iterable

import pytest

from _pytest.mark.expression import Expression


# -----------------------------------------------------------------------------
# Qt binding compatibility
# -----------------------------------------------------------------------------
# The modernized test matrix targets the PySide6 binding. Legacy modules still
# reference ``PyQt5`` directly, so expose a compatibility shim that maps those
# imports onto the PySide6 modules when PyQt5 is unavailable. This keeps the
# test suite runnable in environments that only install the new dependency
# while the runtime code continues to import the historic names.
try:  # pragma: no cover - exercised indirectly when PySide6 is installed
    import PySide6  # noqa: F401
except Exception:  # pragma: no cover - bindings missing entirely
    _QT_ALIAS_INSTALLED = False
else:
    _QT_ALIAS_INSTALLED = True


def _install_pyside6_alias() -> None:
    """Register ``PyQt5`` aliases backed by PySide6."""

    if not _QT_ALIAS_INSTALLED:
        return
    if "PyQt5" in sys.modules:
        return

    modules = {}
    for submodule in (
        "QtCore",
        "QtGui",
        "QtWidgets",
        "QtTest",
        "QtOpenGL",
        "QtOpenGLWidgets",
    ):
        modules[submodule] = importlib.import_module(f"PySide6.{submodule}")
        sys.modules[f"PyQt5.{submodule}"] = modules[submodule]

    # Replicate the ``PyQt5.Qt`` namespace for callers that expect it.
    qt_namespace = type(sys)("PyQt5.Qt")
    qt_namespace.QWidget = modules["QtWidgets"].QWidget
    qt_namespace.QRect = modules["QtCore"].QRect
    qt_namespace.QEvent = modules["QtCore"].QEvent
    qt_namespace.QSize = modules["QtCore"].QSize
    qt_namespace.QPoint = modules["QtCore"].QPoint
    qt_namespace.QOpenGLWidget = modules["QtOpenGLWidgets"].QOpenGLWidget
    sys.modules["PyQt5.Qt"] = qt_namespace

    shim = type(sys)("PyQt5")
    for name, module in modules.items():
        setattr(shim, name, module)
    shim.Qt = qt_namespace
    sys.modules["PyQt5"] = shim

    qtcore = modules["QtCore"]
    if not hasattr(qtcore, "PYQT_VERSION_STR"):
        qtcore.PYQT_VERSION_STR = qtcore.qVersion()
    if not hasattr(qtcore, "QT_VERSION_STR"):
        qtcore.QT_VERSION_STR = qtcore.qVersion()
    if not hasattr(qtcore, "QObjectCleanupHandler"):
        class _CleanupHandler:
            def __init__(self) -> None:
                self._objects: list[object] = []

            def add(self, obj: object) -> None:
                self._objects.append(obj)

            def clear(self) -> None:
                self._objects.clear()

        qtcore.QObjectCleanupHandler = _CleanupHandler

    # Reset VisPy's cached Qt backend so it can bind to the PySide6-backed
    # shims defined above.
    try:  # pragma: no cover - depends on vispy availability
        from vispy.app import backends as _vispy_backends
    except Exception:  # pragma: no cover - vispy not importable yet
        pass
    else:
        _vispy_backends.qt_lib = None
        for module_name in (
            "vispy.app.backends._pyqt5",
            "vispy.app.backends._pyside6",
            "vispy.app.backends._qt",
        ):
            sys.modules.pop(module_name, None)

    # ``sip`` is only used to toggle the global destroy-on-exit behaviour.
    if "sip" not in sys.modules:
        sip_module = type(sys)("sip")

        def _setdestroyonexit(_flag: bool) -> None:  # pragma: no cover - trivial
            return None

        sip_module.setdestroyonexit = _setdestroyonexit
        sys.modules["sip"] = sip_module


_install_pyside6_alias()


# -----------------------------------------------------------------------------
# Headless Qt configuration
# -----------------------------------------------------------------------------
# Force Qt to use an offscreen platform so GUI tests can run in headless
# environments (such as CI workers).
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("VISPY_BACKEND", "pyside6")

try:
    from visbrain.config import CONFIG
except Exception:  # pragma: no cover - defensive in CI without GUI libs
    CONFIG = None
else:
    # Prevent Visbrain from attempting to display PyQt applications during
    # tests when the GUI stack is available.
    CONFIG["SHOW_PYQT_APP"] = False

# Paths whose tests should automatically be marked as requiring a GUI stack.
_REPO_ROOT = Path(__file__).parent.resolve()
_GUI_MARKER_PATHS = (
    _REPO_ROOT / "visbrain" / "gui",
    _REPO_ROOT / "visbrain" / "objects" / "tests",
    _REPO_ROOT / "visbrain" / "utils" / "gui" / "tests",
    _REPO_ROOT / "visbrain" / "io" / "tests",
    _REPO_ROOT / "visbrain" / "utils" / "sleep" / "tests",
    _REPO_ROOT / "visbrain" / "utils" / "tests",
)


def _expression_allows_gui(config: pytest.Config) -> bool:
    expr = getattr(config.option, "markexpr", "") or ""
    if not expr:
        return True
    try:
        return Expression(expr).evaluate({"gui": True})
    except Exception:  # pragma: no cover - fallback for unexpected syntax
        lowered = expr.lower()
        if "not gui" in lowered and "gui" not in lowered.replace("not gui", ""):
            return False
        return True


_RUNNING_GUI_TESTS = True


def pytest_configure(config: pytest.Config) -> None:
    """Register the custom GUI marker."""
    config.addinivalue_line(
        "markers", "gui: tests that require a Qt/OpenGL stack"
    )
    global _RUNNING_GUI_TESTS
    _RUNNING_GUI_TESTS = _expression_allows_gui(config)


def _is_under(path: Path, parents: Iterable[Path]) -> bool:
    """Return ``True`` if *path* is located under any of *parents*."""
    for parent in parents:
        try:
            path.relative_to(parent)
        except ValueError:
            continue
        else:
            return True
    return False


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    """Mark tests under GUI-specific paths with the ``gui`` marker."""
    for item in items:
        item_path = Path(str(item.fspath)).resolve()
        if _is_under(item_path, _GUI_MARKER_PATHS):
            item.add_marker("gui")


def pytest_ignore_collect(
    collection_path: Path,
    path=None,
    config: pytest.Config | None = None,  # type: ignore[override]
):
    """Skip importing GUI-heavy test modules when they are deselected."""
    if config is None and path is not None:  # pragma: no branch - old pytest signature
        config = path  # type: ignore[assignment]
    if config is not None and _RUNNING_GUI_TESTS:
        return False
    if config is None and _RUNNING_GUI_TESTS:
        return False
    return _is_under(collection_path.resolve(), _GUI_MARKER_PATHS)
