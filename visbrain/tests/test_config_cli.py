"""Tests for :mod:`visbrain.config` command line parsing."""

from __future__ import annotations

import importlib
import logging
import sys


def _reload_config():
    sys.modules.pop("visbrain.config", None)
    return importlib.import_module("visbrain.config")


def test_init_config_accepts_boolean_flag(monkeypatch):
    """A valid ``--visbrain-show`` argument toggles the GUI flag."""

    cfg = _reload_config()
    cfg.CONFIG["SHOW_PYQT_APP"] = True

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", [
            "visbrain",
            "--visbrain-show=False",
        ])
        cfg.init_config(["--visbrain-show=False"])

    assert cfg.CONFIG["SHOW_PYQT_APP"] is False


def test_init_config_rejects_invalid_boolean(monkeypatch, caplog):
    """Invalid boolean arguments fall back to the default and log errors."""

    cfg = _reload_config()
    cfg.CONFIG["SHOW_PYQT_APP"] = True

    with monkeypatch.context() as m:
        m.setattr(sys, "argv", [
            "visbrain",
            "--visbrain-show=__import__('os').system('echo unsafe')",
        ])
        caplog.set_level(logging.ERROR, logger="visbrain")
        cfg.init_config(["--visbrain-show=__import__('os').system('echo unsafe')"])

    assert cfg.CONFIG["SHOW_PYQT_APP"] is True
    assert any(
        "Invalid value for --visbrain-show" in record.message
        for record in caplog.records
    )
