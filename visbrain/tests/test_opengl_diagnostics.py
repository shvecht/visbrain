"""Tests for VisPy/OpenGL diagnostics and fallback behaviour."""

from __future__ import annotations

import importlib
import logging
import sys
import types

import pytest

def _reload_config():
    sys.modules.pop("visbrain.config", None)
    return importlib.import_module("visbrain.config")


def _clear_vispy_modules():
    for name in list(sys.modules):
        if name == "vispy" or name.startswith("vispy."):
            sys.modules.pop(name, None)


def _install_runtime_stubs(monkeypatch: pytest.MonkeyPatch) -> None:
    """Install lightweight stubs for utility and Qt dependencies."""

    logging_mod = types.ModuleType("visbrain.utils.logging")
    logging_mod.set_log_level = lambda level, match=None: None

    others_mod = types.ModuleType("visbrain.utils.others")

    class DummyProfiler:
        def __call__(self, *args, **kwargs):  # pragma: no cover - compatibility
            return None

    others_mod.Profiler = DummyProfiler

    utils_pkg = types.ModuleType("visbrain.utils")
    utils_pkg.__path__ = []  # Mark as package for submodule imports

    monkeypatch.setitem(sys.modules, "visbrain.utils", utils_pkg)
    monkeypatch.setitem(sys.modules, "visbrain.utils.logging", logging_mod)
    monkeypatch.setitem(sys.modules, "visbrain.utils.others", others_mod)

    class _DummySignal:
        def connect(self, *_args, **_kwargs):  # pragma: no cover - compatibility
            return None

    class DummyQObject:
        destroyed = _DummySignal()

    class DummyQCoreApplication:
        @staticmethod
        def closingDown() -> bool:
            return False

    class DummyQApplication:
        _instance: "DummyQApplication | None" = None

        def __init__(self, *_args, **_kwargs):
            DummyQApplication._instance = self

        @staticmethod
        def instance() -> "DummyQApplication | None":
            return DummyQApplication._instance

        @staticmethod
        def setQuitOnLastWindowClosed(_flag: bool) -> None:
            return None

        def quit(self) -> None:  # pragma: no cover - compatibility
            return None

        def deleteLater(self) -> None:  # pragma: no cover - compatibility
            return None

    dummy_qt = types.ModuleType("visbrain.qt")
    dummy_qt.QT_API = "stub"
    dummy_qt.QtCore = types.SimpleNamespace(
        QCoreApplication=DummyQCoreApplication, QObject=DummyQObject
    )
    dummy_qt.QtWidgets = types.SimpleNamespace(QApplication=DummyQApplication)
    dummy_qt.guard_qapp_lifecycle = lambda: None

    monkeypatch.setitem(sys.modules, "visbrain.qt", dummy_qt)


def test_vispy_import_failure_emits_warning(monkeypatch, caplog, recwarn):
    """Import errors from :mod:`vispy.app` should surface as warnings."""

    _clear_vispy_modules()
    _install_runtime_stubs(monkeypatch)
    real_import_module = importlib.import_module

    def fake_import(name, *args, **kwargs):
        if name == "vispy.app":
            raise OSError("GL implementation missing")
        return real_import_module(name, *args, **kwargs)

    monkeypatch.setattr(importlib, "import_module", fake_import)
    caplog.set_level(logging.INFO, logger="visbrain")

    cfg_mod = _reload_config()
    cfg = cfg_mod.get_config()

    assert cfg.vispy_diagnostics.available is False
    assert cfg.vispy_diagnostics.context_available is False
    assert "GL implementation missing" in (cfg.vispy_diagnostics.error or "")
    assert any("vispy.probe" in record.message for record in caplog.records)
    assert any(
        "VisPy backend unavailable" in str(w.message) for w in recwarn.list
    )


def test_headless_backend_fallback_prefers_egl(monkeypatch, caplog, recwarn):
    """Headless startup should configure an offscreen backend when available."""

    _clear_vispy_modules()
    _install_runtime_stubs(monkeypatch)
    monkeypatch.setenv("VISBRAIN_SHOW_GUI", "0")

    class DummyConfig(dict):
        def __getitem__(self, key):
            return super().get(key, "")

        def __setitem__(self, key, value):
            super().__setitem__(key, value)

    attempts: list[str] = []

    class DummyApplication:
        def __init__(self, backend=None):
            backend_name = (backend or "egl").lower()
            attempts.append(backend_name)
            if backend_name != "egl":
                raise RuntimeError(f"Backend {backend_name} unavailable")
            self._backend = backend_name

        @property
        def backend_name(self):
            return self._backend

    class DummyGLInfo:
        have_context = True

        def get_version(self):
            return "4.5 Dummy"

        def get_renderer(self):
            return "DummyGPU"

    dummy_config = DummyConfig()
    dummy_app = types.ModuleType("vispy.app")
    dummy_app.application = types.SimpleNamespace(Application=DummyApplication)
    dummy_app.use_app = lambda backend=None: DummyApplication(backend)

    dummy_vispy = types.ModuleType("vispy")
    dummy_vispy.config = dummy_config

    dummy_gl = types.SimpleNamespace(gl_info=DummyGLInfo())
    dummy_gloo = types.SimpleNamespace(gl=dummy_gl)

    monkeypatch.setitem(sys.modules, "vispy", dummy_vispy)
    monkeypatch.setitem(sys.modules, "vispy.app", dummy_app)
    monkeypatch.setitem(sys.modules, "vispy.gloo", dummy_gloo)
    monkeypatch.setitem(sys.modules, "vispy.gloo.gl", dummy_gl)

    caplog.set_level(logging.INFO, logger="visbrain")

    cfg_mod = _reload_config()
    cfg = cfg_mod.get_config()

    assert cfg.show_gui is False
    assert cfg.vispy_backend == "egl"
    assert dummy_config["default_backend"] == "egl"
    assert cfg.vispy_diagnostics.available is True
    assert cfg.vispy_diagnostics.context_available is True
    assert cfg.vispy_diagnostics.gl_version == "4.5 Dummy"
    assert cfg.vispy_diagnostics.renderer == "DummyGPU"
    assert "egl" in attempts
    assert any("vispy.headless" in record.message for record in caplog.records)
    assert any("vispy.probe" in record.message for record in caplog.records)
    assert not recwarn.list
