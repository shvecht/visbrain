"""Test modules importation."""

import pytest


def test_import_matplotlib():
    """Import matplotlib."""
    import matplotlib  # noqa


def test_import_numpy():
    """Import NumPy."""
    import numpy  # noqa


def test_import_scipy():
    """Import scipy."""
    import scipy  # noqa


@pytest.mark.gui
def test_import_pyside6():
    """Import PySide6."""
    import PySide6  # noqa: F401


@pytest.mark.gui
def test_import_brain():
    """Import the Brain module.."""
    from visbrain.gui import Brain  # noqa


@pytest.mark.gui
def test_import_sleep():
    """Import the Sleep module.."""
    from visbrain.gui import Sleep  # noqa


@pytest.mark.gui
def test_import_signal():
    """Import the Signal module.."""
    from visbrain.gui import Signal  # noqa


@pytest.mark.gui
def test_import_figure():
    """Import the Figure module.."""
    from visbrain.gui import Figure  # noqa
