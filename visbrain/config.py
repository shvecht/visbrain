"""Configuration and runtime helpers for Visbrain."""
from __future__ import annotations

import getopt
import logging
import os
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Iterator, Mapping, MutableMapping, Optional, Sequence

from vispy import app as visapp

from visbrain.utils.logging import set_log_level
from visbrain.utils.others import Profiler

from .qt import QT_API, QtWidgets, guard_qapp_lifecycle


logger = logging.getLogger("visbrain")


@dataclass
class VisbrainConfig:
    """Container for runtime configuration and GUI application handles."""

    log_level: str = "info"
    log_search: str | None = None
    qt_api: str | None = QT_API
    vispy_backend: str | None = None
    show_gui: bool = True
    mpl_render: bool = False
    _pyqt_app: Optional[QtWidgets.QApplication] = field(
        default=None, init=False, repr=False
    )
    _vispy_app: Optional[visapp.Application] = field(
        default=None, init=False, repr=False
    )

    def __post_init__(self) -> None:
        if self.vispy_backend is None and isinstance(self.qt_api, str):
            self.vispy_backend = self.qt_api.lower()
        self.apply_logging()

    # ------------------------------------------------------------------
    # Logging helpers
    # ------------------------------------------------------------------
    def apply_logging(self) -> None:
        """Apply the stored logging configuration."""

        set_log_level(self.log_level, match=self.log_search)

    def set_logging(
        self, *, level: str | None = None, match: str | None = None
    ) -> None:
        """Update and apply logging preferences."""

        if level is not None:
            self.log_level = level
        if match is not None:
            self.log_search = match
        self.apply_logging()

    # ------------------------------------------------------------------
    # Copy helpers
    # ------------------------------------------------------------------
    def copy(self) -> VisbrainConfig:
        """Return a shallow copy of the configuration."""

        duplicate = VisbrainConfig(
            log_level=self.log_level,
            log_search=self.log_search,
            qt_api=self.qt_api,
            vispy_backend=self.vispy_backend,
            show_gui=self.show_gui,
            mpl_render=self.mpl_render,
        )
        duplicate._pyqt_app = self._pyqt_app
        duplicate._vispy_app = self._vispy_app
        return duplicate

    # ------------------------------------------------------------------
    # Backwards compatibility helpers
    # ------------------------------------------------------------------
    @property
    def show_pyqt_app(self) -> bool:
        """Return whether GUI resources should be created."""

        return self.show_gui

    @show_pyqt_app.setter
    def show_pyqt_app(self, enabled: bool) -> None:
        self.show_gui = bool(enabled)

    # ------------------------------------------------------------------
    # Qt application helpers
    # ------------------------------------------------------------------
    @property
    def pyqt_app(self) -> Optional[QtWidgets.QApplication]:
        """Return the cached Qt application instance."""

        return self._pyqt_app

    @pyqt_app.setter
    def pyqt_app(self, app: Optional[QtWidgets.QApplication]) -> None:
        self._pyqt_app = app

    def get_qt_app(
        self, *, create: bool = True, force: bool = False
    ) -> Optional[QtWidgets.QApplication]:
        """Return the active :class:`~QtWidgets.QApplication` instance."""

        app = QtWidgets.QApplication.instance()
        if app is None:
            if not create or (not self.show_gui and not force):
                self._pyqt_app = None
                return None
            app = QtWidgets.QApplication([""])

        self._pyqt_app = app
        guard_qapp_lifecycle()
        return app

    # ------------------------------------------------------------------
    # VisPy application helpers
    # ------------------------------------------------------------------
    @property
    def vispy_app(self) -> Optional[visapp.Application]:
        """Return the cached VisPy application instance."""

        return self._vispy_app

    @vispy_app.setter
    def vispy_app(self, app: Optional[visapp.Application]) -> None:
        self._vispy_app = app

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
                self._vispy_app = None

        if self._vispy_app is not None:
            return self._vispy_app

        if not create or (not self.show_gui and not force):
            return None

        self._vispy_app = visapp.application.Application(self.vispy_backend)
        return self._vispy_app

    def use_app(self, backend_name):
        """Force VisPy to use a specific backend."""

        normalized = (
            backend_name.lower() if isinstance(backend_name, str) else backend_name
        )
        self.vispy_backend = normalized
        self._vispy_app = visapp.application.Application(normalized)
        return self._vispy_app


@dataclass
class _AppContextState:
    """Book-keeping helper for nested application contexts."""

    stack: list[tuple[bool, bool]] = field(default_factory=list)

    def push(self, owned: bool, reset: bool) -> None:
        self.stack.append((owned, reset))

    def pop(self) -> tuple[bool, bool]:
        if not self.stack:
            raise RuntimeError("Application context stack underflow")
        return self.stack.pop()

    def propagate_reset(self, reset: bool) -> None:
        if reset and self.stack:
            owned, parent_reset = self.stack[-1]
            if not parent_reset:
                self.stack[-1] = (owned, True)

    @property
    def depth(self) -> int:
        return len(self.stack)


# Global configuration handle exposed to consumers of :mod:`visbrain.config`.
_SHOW_GUI_ENVVAR = "VISBRAIN_SHOW_GUI"


def _parse_bool_flag(value: str) -> bool:
    """Return a boolean from a CLI or environment flag value."""

    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y", "on"}:
        return True
    if normalized in {"0", "false", "no", "n", "off"}:
        return False
    raise ValueError(f"Unsupported boolean value: {value!r}")


def _read_show_gui_flag(env_value: str) -> bool:
    """Parse an environment toggle for GUI visibility."""

    return _parse_bool_flag(env_value)


def configure_from_environ(
    *,
    environ: Mapping[str, str] | None = None,
    config: VisbrainConfig | None = None,
) -> VisbrainConfig:
    """Update configuration flags from environment variables."""

    env = environ if environ is not None else os.environ
    cfg = config if config is not None else get_config()

    raw_show = env.get(_SHOW_GUI_ENVVAR)
    if raw_show is not None:
        try:
            cfg.show_gui = _read_show_gui_flag(raw_show)
        except ValueError:
            logger.error(
                "Invalid value for %s: %s" % (_SHOW_GUI_ENVVAR, raw_show)
            )

    return cfg


def configure_headless(
    *,
    environ: MutableMapping[str, str] | None = None,
    config: VisbrainConfig | None = None,
    force: bool = False,
) -> VisbrainConfig:
    """Ensure GUI creation is disabled in automated environments.

    Parameters
    ----------
    environ:
        Mapping updated with the headless toggle. Defaults to :data:`os.environ`.
    config:
        Configuration instance to update. Defaults to :func:`get_config()`.
    force:
        When ``True`` the environment toggle is overwritten even if it already
        exists. When ``False`` an existing value takes precedence.
    """

    env = environ if environ is not None else os.environ
    if force or _SHOW_GUI_ENVVAR not in env:
        env[_SHOW_GUI_ENVVAR] = "0"
    return configure_from_environ(environ=env, config=config)


_CONFIG = VisbrainConfig()
_QT_CONTEXT_STATE = _AppContextState()
_VISPY_CONTEXT_STATE = _AppContextState()

configure_from_environ(config=_CONFIG)


def get_config() -> VisbrainConfig:
    """Return the global :class:`VisbrainConfig` instance."""

    return _CONFIG


# Backwards compatible alias
CONFIG = _CONFIG

# Visbrain profiler (derived from the VisPy profiler)
PROFILER = Profiler()


def get_qt_app(
    create: bool = True, *, force: bool = False
) -> Optional[QtWidgets.QApplication]:
    """Return (and optionally create) the Qt application instance."""

    return get_config().get_qt_app(create=create, force=force)


def ensure_qt_app(*, force: bool = False) -> Optional[QtWidgets.QApplication]:
    """Ensure a Qt application exists, respecting the headless flag."""

    return get_config().get_qt_app(create=True, force=force)


def get_vispy_app(
    backend: Optional[str] = None,
    *,
    create: bool = True,
    force: bool = False,
) -> Optional[visapp.Application]:
    """Return (and optionally create) the VisPy application instance."""

    return get_config().get_vispy_app(backend=backend, create=create, force=force)


def ensure_vispy_app(
    backend: Optional[str] = None, *, force: bool = False
) -> Optional[visapp.Application]:
    """Ensure a VisPy application exists, respecting the headless flag."""

    return get_config().get_vispy_app(backend=backend, create=True, force=force)


def use_app(backend_name):
    """Use a specific VisPy backend."""

    return get_config().use_app(backend_name)


def _shutdown_qt_application(
    config: VisbrainConfig, app: QtWidgets.QApplication
) -> None:
    """Attempt to gracefully close a Qt application instance."""

    try:
        quit_method = getattr(app, "quit", None)
        if callable(quit_method):
            quit_method()
        else:
            close_all = getattr(app, "closeAllWindows", None)
            if callable(close_all):  # pragma: no branch - best effort fallback
                close_all()
        delete_later = getattr(app, "deleteLater", None)
        if callable(delete_later):  # pragma: no branch - optional Qt API
            delete_later()
    finally:
        config.pyqt_app = None


def _shutdown_vispy_application(
    config: VisbrainConfig, app: visapp.Application
) -> None:
    """Attempt to gracefully close a VisPy application instance."""

    try:
        quit_method = getattr(app, "quit", None)
        if callable(quit_method):
            quit_method()
    finally:
        config.vispy_app = None


@contextmanager
def qt_app(
    *, create: bool = True, force: bool = False, reset: bool = False
) -> Iterator[Optional[QtWidgets.QApplication]]:
    """Context manager yielding the active Qt application instance."""

    config = get_config()
    previous = config.pyqt_app
    app = config.get_qt_app(create=create, force=force)
    if app is None:
        yield None
        return

    owned = app is not previous
    _QT_CONTEXT_STATE.push(owned, reset)
    try:
        yield app
    finally:
        owned_state, reset_state = _QT_CONTEXT_STATE.pop()
        _QT_CONTEXT_STATE.propagate_reset(reset_state)
        if _QT_CONTEXT_STATE.depth == 0 and (owned_state or reset_state):
            _shutdown_qt_application(config, app)


@contextmanager
def vispy_app(
    backend: Optional[str] = None,
    *,
    create: bool = True,
    force: bool = False,
    reset: bool = False,
) -> Iterator[Optional[visapp.Application]]:
    """Context manager yielding the active VisPy application instance."""

    config = get_config()
    previous = config.vispy_app
    app = config.get_vispy_app(
        backend=backend, create=create, force=force
    )
    if app is None:
        yield None
        return

    owned = app is not previous
    _VISPY_CONTEXT_STATE.push(owned, reset)
    try:
        yield app
    finally:
        owned_state, reset_state = _VISPY_CONTEXT_STATE.pop()
        _VISPY_CONTEXT_STATE.propagate_reset(reset_state)
        if _VISPY_CONTEXT_STATE.depth == 0 and (owned_state or reset_state):
            _shutdown_vispy_application(config, app)


# Matplotlib rendering defaults to disabled until explicitly enabled.
get_config().mpl_render = False

# Jupyter / iPython detection enables Matplotlib rendering automatically.
try:  # pragma: no cover - optional dependency
    ip = get_ipython()
except NameError:  # pragma: no cover - IPython not available
    ip = None
else:
    if ip is not None:  # pragma: no branch - executed only in notebooks
        cfg = get_config()
        cfg.mpl_render = True
        import vispy

        vispy.use(cfg.vispy_backend)


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


def configure_from_argv(
    argv: Sequence[str], *, config: VisbrainConfig | None = None
) -> VisbrainConfig:
    """Parse Visbrain CLI flags from *argv* and return the resulting config."""

    cfg = config if config is not None else get_config()
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
            cfg.set_logging(level=argument)
            continue
        if option == "--visbrain-show":
            try:
                cfg.show_gui = _parse_bool_flag(argument)
            except ValueError:
                logger.error(
                    "Invalid value for --visbrain-show: %s" % argument
                )
            else:
                logger.debug("Show GUI resources : %s" % cfg.show_gui)
            continue
        if option == "--visbrain-search":
            cfg.set_logging(match=argument)

    return cfg


def parse_cli(
    argv: Sequence[str], config: VisbrainConfig | None = None
) -> VisbrainConfig:
    """Backward compatible wrapper around :func:`configure_from_argv`."""

    logger.warning(
        "parse_cli is deprecated; call configure_from_argv(...) instead.",
    )
    return configure_from_argv(argv, config=config)


def init_config(argv: Sequence[str]) -> VisbrainConfig:
    """Backward compatible wrapper around :func:`parse_cli`."""

    logger.warning(
        "init_config is deprecated; call parse_cli(...) instead.",
    )
    return parse_cli(argv, CONFIG)

