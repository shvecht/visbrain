"""Pytest configuration for Visbrain.

This module centralizes headless Qt configuration and test markers so all
collected test modules behave consistently regardless of their location in the
repository.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

import pytest

from _pytest.mark.expression import Expression


# -----------------------------------------------------------------------------
# Headless Qt configuration
# -----------------------------------------------------------------------------
# Force Qt to use an offscreen platform so GUI tests can run in headless
# environments (such as CI workers).
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

try:
    from visbrain.config import CONFIG
except Exception:  # pragma: no cover - defensive in CI without GUI libs
    CONFIG = None
else:
    # Prevent Visbrain from attempting to display PyQt applications during
    # tests when the GUI stack is available.
    CONFIG.show_pyqt_app = False

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
