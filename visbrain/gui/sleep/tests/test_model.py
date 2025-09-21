"""Tests for :mod:`visbrain.gui.sleep.model`."""

from __future__ import annotations

import logging

import numpy as np
import pytest


def test_dataset_initial_statistics(sleep_dataset):
    """Summary statistics are computed on initialisation."""

    info = sleep_dataset.datainfo
    np.testing.assert_allclose(info["mean"], sleep_dataset.data.mean(1))
    np.testing.assert_allclose(info["min"], sleep_dataset.data.min(1))
    np.testing.assert_allclose(info["max"], sleep_dataset.data.max(1))


def test_dataset_len_and_types(sleep_dataset):
    """Channels and arrays keep their expected size and dtype."""

    assert len(sleep_dataset) == 2
    assert sleep_dataset.data.dtype == np.float32
    assert sleep_dataset.hypno.dtype == np.float32
    step = sleep_dataset.time[1] - sleep_dataset.time[0]
    assert step == pytest.approx(1.0 / sleep_dataset.sf)


def test_refresh_data_info(sleep_dataset):
    """Updating ``data`` recomputes cached statistics."""

    new_data = np.zeros_like(sleep_dataset.data)
    new_data[0, :] = 3.0
    new_data[1, :] = -1.0
    sleep_dataset.data = new_data
    info = sleep_dataset.datainfo
    assert info["mean"][0] == pytest.approx(3.0)
    assert info["mean"][1] == pytest.approx(-1.0)


def test_detection_override(sleep_dataset):
    """Custom detection hooks are stored in the dataset."""

    def custom(data, sf, time, hypno):  # pragma: no cover - simple hook
        return np.array([[0, 10]])

    logger = logging.getLogger("visbrain")
    original_handlers = list(logger.handlers)
    logger.handlers = [logging.NullHandler()]
    try:
        sleep_dataset.replace_detection("spindle", custom)
    finally:
        logger.handlers = original_handlers
    assert sleep_dataset.has_custom_detection("spindle")
    assert sleep_dataset.get_detection("spindle") is custom

    with pytest.raises(ValueError):
        sleep_dataset.replace_detection("invalid", custom)

    with pytest.raises(AssertionError):
        sleep_dataset.replace_detection("sw", None)
