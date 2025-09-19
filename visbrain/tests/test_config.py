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

    cfg_mod = _reload_config()
    cfg = cfg_mod.get_config()

    assert DummyQApplication.created == 0
    assert DummyVispyApplication.created == 0
    assert cfg.pyqt_app is None
    assert cfg.vispy_app is None


def test_ensure_helpers_respect_headless_flag(monkeypatch):
    """Application helpers must honour the ``show_pyqt_app`` toggle."""

    cfg_mod = _reload_config()
    cfg = cfg_mod.get_config()

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

    monkeypatch.setattr(cfg_mod.QtWidgets, "QApplication", DummyQApplication)
    monkeypatch.setattr(
        cfg_mod.visapp.application, "Application", DummyVispyApplication
    )

    cfg.show_pyqt_app = False
    DummyQApplication._instance = None

    assert cfg_mod.ensure_qt_app() is None
    assert DummyQApplication.created == 0

    forced_qapp = cfg_mod.ensure_qt_app(force=True)
    assert isinstance(forced_qapp, DummyQApplication)
    assert DummyQApplication.created == 1
    assert cfg.pyqt_app is forced_qapp

    cfg.pyqt_app = None
    DummyVispyApplication.created = 0

    assert cfg_mod.ensure_vispy_app() is None
    assert DummyVispyApplication.created == 0

    forced_vispy = cfg_mod.ensure_vispy_app(force=True)
    assert isinstance(forced_vispy, DummyVispyApplication)
    assert forced_vispy.backend == cfg.vispy_backend


def test_configure_from_argv_updates_runtime(monkeypatch, caplog):
    """CLI parsing should rely solely on the provided ``argv`` sequence."""

    cfg_mod = _reload_config()
    cfg = cfg_mod.get_config()

    baseline = cfg.copy()

    # Pretend the runtime was invoked with a conflicting flag and ensure it is
    # ignored when ``argv`` is empty.
    monkeypatch.setattr(sys, "argv", ["visbrain", "--visbrain-show=False"])
    untouched = cfg_mod.configure_from_argv([], config=baseline.copy())
    assert untouched.show_pyqt_app is baseline.show_pyqt_app

    # Parsing explicit arguments must update the provided config in place and
    # apply logging preferences.
    mutated = baseline.copy()
    caplog.set_level(logging.DEBUG, logger="visbrain")
    result = cfg_mod.configure_from_argv(
        ["--visbrain-show=False", "--visbrain-log=debug", "--visbrain-search=test"],
        config=mutated,
    )
    assert result is mutated
    assert mutated.show_pyqt_app is False
    assert mutated.log_level == "debug"
    assert mutated.log_search == "test"

    # Invalid boolean values should log an error and leave the flag unchanged.
    error_target = baseline.copy()
    cfg_mod.configure_from_argv(["--visbrain-show=not-a-bool"], config=error_target)
    assert error_target.show_pyqt_app is baseline.show_pyqt_app
    assert any(
        "Invalid value for --visbrain-show" in rec.message
        for rec in caplog.records
    )

    # Calling without an explicit config should mutate the shared singleton.
    cfg.show_pyqt_app = True
    cfg_mod.configure_from_argv(["--visbrain-show=False"])
    assert cfg.show_pyqt_app is False
