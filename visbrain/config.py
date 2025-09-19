"""Configuration and runtime helpers for Visbrain."""
from __future__ import annotations

import getopt
import logging
from typing import Optional, Sequence

from vispy import app as visapp

from visbrain.utils.logging import set_log_level
from visbrain.utils.others import Profiler

from .qt import QT_API, QtWidgets


logger = logging.getLogger("visbrain")
set_log_level("info")


class ConfigManager:
    """Container for runtime configuration and GUI application handles."""

    qt_api: str | None
    vispy_backend: str | None
    show_pyqt_app: bool
    mpl_render: bool
    pyqt_app: Optional[QtWidgets.QApplication]
    vispy_app: Optional[visapp.Application]

    def __init__(self, qt_api: str | None = QT_API) -> None:
        self.qt_api = qt_api
        self.vispy_backend = qt_api.lower() if isinstance(qt_api, str) else qt_api
        self.show_pyqt_app = True
        self.mpl_render = False
        self.pyqt_app = None
        self.vispy_app = None

    def copy(self) -> ConfigManager:
        """Return a shallow copy of the configuration manager."""

        duplicate = ConfigManager(self.qt_api)
        duplicate.vispy_backend = self.vispy_backend
        duplicate.show_pyqt_app = self.show_pyqt_app
        duplicate.mpl_render = self.mpl_render
        duplicate.pyqt_app = self.pyqt_app
        duplicate.vispy_app = self.vispy_app
        return duplicate

    # ------------------------------------------------------------------
    # Qt application helpers
    # ------------------------------------------------------------------
    def get_qt_app(
        self, *, create: bool = True, force: bool = False
    ) -> Optional[QtWidgets.QApplication]:
        """Return the active :class:`~QtWidgets.QApplication` instance."""

        app = QtWidgets.QApplication.instance()
        if app is None:
            if not create or (not self.show_pyqt_app and not force):
                self.pyqt_app = None
                return None
            app = QtWidgets.QApplication([""])

        self.pyqt_app = app
        return app

    # ------------------------------------------------------------------
    # VisPy application helpers
    # ------------------------------------------------------------------
    def get_vispy_app(
        self,
        backend: Optional[str] = None,
        *,
        create: bool = True,
        force: bool = False,
    ) -> Optional[visapp.Application]:
        """Return the active :class:`vispy.app.Application` instance."""

        if backend is not None:
            normalized = backend.lower() if isinstance(backend, str) else backend
            if normalized != self.vispy_backend:
                self.vispy_backend = normalized
                self.vispy_app = None

        if self.vispy_app is not None:
            return self.vispy_app

        if not create or (not self.show_pyqt_app and not force):
            return None

        self.vispy_app = visapp.application.Application(self.vispy_backend)
        return self.vispy_app

    def use_app(self, backend_name):
        """Force VisPy to use a specific backend."""

        normalized = (
            backend_name.lower() if isinstance(backend_name, str) else backend_name
        )
        self.vispy_backend = normalized
        self.vispy_app = visapp.application.Application(normalized)
        return self.vispy_app


# Global configuration handle exposed to consumers of :mod:`visbrain.config`.
CONFIG = ConfigManager()

# Visbrain profiler (derived from the VisPy profiler)
PROFILER = Profiler()


def _parse_bool_flag(value: str) -> bool:
    """Return a boolean from a CLI flag value."""

    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y", "on"}:
        return True
    if normalized in {"0", "false", "no", "n", "off"}:
        return False
    raise ValueError(f"Unsupported boolean value: {value!r}")


def get_qt_app(
    create: bool = True, *, force: bool = False
) -> Optional[QtWidgets.QApplication]:
    """Return (and optionally create) the Qt application instance."""

    return CONFIG.get_qt_app(create=create, force=force)


def ensure_qt_app(*, force: bool = False) -> Optional[QtWidgets.QApplication]:
    """Ensure a Qt application exists, respecting the headless flag."""

    return CONFIG.get_qt_app(create=True, force=force)


def get_vispy_app(
    backend: Optional[str] = None,
    *,
    create: bool = True,
    force: bool = False,
) -> Optional[visapp.Application]:
    """Return (and optionally create) the VisPy application instance."""

    return CONFIG.get_vispy_app(backend=backend, create=create, force=force)


def ensure_vispy_app(
    backend: Optional[str] = None, *, force: bool = False
) -> Optional[visapp.Application]:
    """Ensure a VisPy application exists, respecting the headless flag."""

    return CONFIG.get_vispy_app(backend=backend, create=True, force=force)


def use_app(backend_name):
    """Use a specific VisPy backend."""

    return CONFIG.use_app(backend_name)


# Matplotlib rendering defaults to disabled until explicitly enabled.
CONFIG.mpl_render = False

# Jupyter / iPython detection enables Matplotlib rendering automatically.
try:
    ip = get_ipython()
except NameError:
    ip = None  # pragma: no cover - IPython not available
else:
    if ip is not None:  # pragma: no branch - executed only in notebooks
        CONFIG.mpl_render = True
        import vispy

        vispy.use(CONFIG.vispy_backend)


VISBRAIN_HELP = """
Visbrain command line arguments:

  --visbrain-log=(profiler|debug|info|warning|error|critical)
    Sets the verbosity of logging output. The default is 'info'.

  --visbrain-search=[search string]
    Search string in logs.

  --visbrain-show=(True|False)
    Control if GUI have to be displayed.

  --visbrain-help
    Display help Visbrain command line help.

"""


def parse_cli(
    argv: Sequence[str], config: ConfigManager | None = None
) -> ConfigManager:
    """Parse Visbrain CLI flags from *argv* and return the resulting config."""

    cfg = config if config is not None else ConfigManager()
    argnames = [
        "visbrain-log=",
        "visbrain-show=",
        "visbrain-help",
        "visbrain-search=",
    ]
    try:
        opts, _ = getopt.getopt(list(argv), "", argnames)
    except getopt.GetoptError:
        opts = []

    for option, argument in opts:
        if not option.startswith("--visbrain"):
            continue
        if option == "--visbrain-help":
            print(VISBRAIN_HELP)
            continue
        if option == "--visbrain-log":
            set_log_level(argument)
            continue
        if option == "--visbrain-show":
            try:
                cfg.show_pyqt_app = _parse_bool_flag(argument)
            except ValueError:
                logger.error("Invalid value for --visbrain-show: %s", argument)
            else:
                logger.debug("Show PyQt app : %r", cfg.show_pyqt_app)
            continue
        if option == "--visbrain-search":
            set_log_level(match=argument)

    return cfg


def init_config(argv: Sequence[str]) -> ConfigManager:
    """Backward compatible wrapper around :func:`parse_cli`."""

    logger.warning(
        "init_config is deprecated; call parse_cli(...) instead.",
    )
    return parse_cli(argv, CONFIG)

