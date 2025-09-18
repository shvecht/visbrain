"""Headless safety checks for the application factories."""

from __future__ import annotations

import importlib
import sys

import vispy.app

from visbrain import qt as qt_mod


def test_config_import_has_no_side_effect(monkeypatch):
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

    with monkeypatch.context() as m:
        m.setattr(qt_mod.QtWidgets, "QApplication", DummyQApplication)
        m.setattr(vispy.app.application, "Application", DummyVispyApplication)
        sys.modules.pop("visbrain.config", None)
        cfg = importlib.import_module("visbrain.config")

        assert DummyQApplication.created == 0
        assert DummyVispyApplication.created == 0
        assert cfg.CONFIG["PYQT_APP"] is None
        assert cfg.CONFIG["VISPY_APP"] is None

    sys.modules.pop("visbrain.config", None)
    importlib.import_module("visbrain.config")


def test_app_factories_create_on_demand(monkeypatch):
    """Application factories should lazily instantiate applications."""

    sys.modules.pop("visbrain.config", None)
    cfg = importlib.import_module("visbrain.config")

    class DummyQApplication:
        created = 0
        _instance: DummyQApplication | None = None

        @staticmethod
        def instance():
            return DummyQApplication._instance

        def __init__(self, *args, **kwargs):
            DummyQApplication.created += 1
            DummyQApplication._instance = self

    with monkeypatch.context() as m:
        m.setattr(cfg, "_QT_APP", None)
        m.setitem(cfg.CONFIG, "PYQT_APP", None)
        m.setattr(cfg.QtWidgets, "QApplication", DummyQApplication)

        assert cfg.get_qt_app(create=False) is None
        app = cfg.get_qt_app()
        assert isinstance(app, DummyQApplication)
        assert DummyQApplication.created == 1
        assert cfg.CONFIG["PYQT_APP"] is app
        assert cfg.get_qt_app() is app

    class DummyVispyApplication:
        created = 0

        def __init__(self, backend=None):
            DummyVispyApplication.created += 1
            self.backend = backend

    with monkeypatch.context() as m:
        m.setattr(cfg, "_VISPY_APP", None)
        m.setitem(cfg.CONFIG, "VISPY_APP", None)
        m.setattr(cfg.visapp.application, "Application", DummyVispyApplication)

        app = cfg.get_vispy_app()
        assert isinstance(app, DummyVispyApplication)
        assert DummyVispyApplication.created == 1
        assert app.backend == cfg.CONFIG["VISPY_BACKEND"]
        assert cfg.CONFIG["VISPY_APP"] is app
        assert cfg.get_vispy_app() is app

    sys.modules.pop("visbrain.config", None)
    importlib.import_module("visbrain.config")
