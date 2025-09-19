"""Tests for :mod:`visbrain.config` initialization helpers."""

from __future__ import annotations

import importlib
import logging
import sys

import vispy.app

from visbrain import qt as qt_mod


def _reload_config():
    sys.modules.pop("visbrain.config", None)
    return importlib.import_module("visbrain.config")


def test_import_has_no_side_effects(monkeypatch):
    """Importing :mod:`visbrain.config` must not create GUI applications."""

    class DummyQApplication:
        created = 0
        _instance: DummyQApplication | None = None

        @staticmethod
        def instance():
            return DummyQApplication._instance

        def __init__(self, *args, **kwargs):
            DummyQApplication.created += 1
            DummyQApplication._instance = self

    class DummyVispyApplication:
        created = 0

        def __init__(self, *args, **kwargs):
            DummyVispyApplication.created += 1

    monkeypatch.setattr(qt_mod.QtWidgets, "QApplication", DummyQApplication)
    monkeypatch.setattr(vispy.app.application, "Application", DummyVispyApplication)

    cfg = _reload_config()

    assert DummyQApplication.created == 0
    assert DummyVispyApplication.created == 0
    assert cfg.CONFIG.pyqt_app is None
    assert cfg.CONFIG.vispy_app is None


def test_ensure_helpers_respect_headless_flag(monkeypatch):
    """Application helpers must honour the ``show_pyqt_app`` toggle."""

    cfg = _reload_config()

    class DummyQApplication:
        created = 0
        _instance: DummyQApplication | None = None

        @staticmethod
        def instance():
            return DummyQApplication._instance

        def __init__(self, *args, **kwargs):
            DummyQApplication.created += 1
            DummyQApplication._instance = self

    class DummyVispyApplication:
        created = 0

        def __init__(self, backend=None):
            DummyVispyApplication.created += 1
            self.backend = backend

    monkeypatch.setattr(cfg.QtWidgets, "QApplication", DummyQApplication)
    monkeypatch.setattr(cfg.visapp.application, "Application", DummyVispyApplication)

    cfg.CONFIG.show_pyqt_app = False
    DummyQApplication._instance = None

    assert cfg.ensure_qt_app() is None
    assert DummyQApplication.created == 0

    forced_qapp = cfg.ensure_qt_app(force=True)
    assert isinstance(forced_qapp, DummyQApplication)
    assert DummyQApplication.created == 1
    assert cfg.CONFIG.pyqt_app is forced_qapp

    cfg.CONFIG.pyqt_app = None
    DummyVispyApplication.created = 0

    assert cfg.ensure_vispy_app() is None
    assert DummyVispyApplication.created == 0

    forced_vispy = cfg.ensure_vispy_app(force=True)
    assert isinstance(forced_vispy, DummyVispyApplication)
    assert forced_vispy.backend == cfg.CONFIG.vispy_backend


def test_parse_cli_uses_provided_arguments(monkeypatch, caplog):
    """CLI parsing should rely solely on the provided ``argv`` sequence."""

    cfg = _reload_config()

    baseline = cfg.CONFIG.copy()

    # Pretend the runtime was invoked with a conflicting flag and ensure it is
    # ignored when ``argv`` is empty.
    monkeypatch.setattr(sys, "argv", ["visbrain", "--visbrain-show=False"])
    untouched = cfg.parse_cli([], config=baseline.copy())
    assert untouched.show_pyqt_app is baseline.show_pyqt_app

    # Parsing explicit arguments must update the provided config in place.
    mutated = baseline.copy()
    result = cfg.parse_cli(["--visbrain-show=False"], config=mutated)
    assert result is mutated
    assert mutated.show_pyqt_app is False

    # Invalid boolean values should log an error and leave the flag unchanged.
    caplog.set_level(logging.ERROR, logger="visbrain")
    error_target = baseline.copy()
    cfg.parse_cli(["--visbrain-show=not-a-bool"], config=error_target)
    assert error_target.show_pyqt_app is baseline.show_pyqt_app
    assert any(
        "Invalid value for --visbrain-show" in rec.message
        for rec in caplog.records
    )
