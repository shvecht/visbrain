"""Visbrain configurations."""
from __future__ import annotations

import getopt
import logging
import sys
from typing import Optional

from vispy import app as visapp

from visbrain.utils.logging import set_log_level
from visbrain.utils.others import Profiler
from .qt import QT_API, QtWidgets


# Set 'info' as the default logging level
logger = logging.getLogger('visbrain')
set_log_level('info')

# Configuration dict
CONFIG: dict[str, object] = {}

# Visbrain profiler (derived from the VisPy profiler)
PROFILER = Profiler()

# Lazily created application instances
_QT_APP: Optional[QtWidgets.QApplication] = None
_VISPY_APP: Optional[visapp.Application] = None

# Backend metadata
CONFIG['QT_API'] = QT_API
CONFIG['VISPY_BACKEND'] = QT_API.lower() if QT_API else None
CONFIG['SHOW_PYQT_APP'] = True
CONFIG['PYQT_APP'] = None
CONFIG['VISPY_APP'] = None


def _parse_bool_flag(value: str) -> bool:
    """Return a boolean from a CLI flag value.

    Accepted truthy values are ``'1'``, ``'true'``, ``'yes'``, ``'y'`` and
    ``'on'`` (case insensitive). Accepted falsey values are the counterparts
    ``'0'``, ``'false'``, ``'no'``, ``'n'`` and ``'off'``.

    Parameters
    ----------
    value : str
        The string representation of the desired boolean.

    Raises
    ------
    ValueError
        If *value* does not match any of the accepted representations.
    """

    normalized = value.strip().lower()
    if normalized in {'1', 'true', 'yes', 'y', 'on'}:
        return True
    if normalized in {'0', 'false', 'no', 'n', 'off'}:
        return False
    raise ValueError(f"Unsupported boolean value: {value!r}")


def get_qt_app(create: bool = True) -> Optional[QtWidgets.QApplication]:
    """Return the active :class:`~QtWidgets.QApplication` instance.

    Parameters
    ----------
    create : bool
        When ``True`` (the default) a new :class:`~QtWidgets.QApplication`
        instance is created if none exists. When ``False`` the function returns
        ``None`` if a Qt application has not been created yet.
    """

    global _QT_APP

    app = QtWidgets.QApplication.instance()
    if app is None and create:
        app = QtWidgets.QApplication([''])

    if app is not None:
        _QT_APP = app
        CONFIG['PYQT_APP'] = app
    return app


def get_vispy_app(backend: Optional[str] = None) -> visapp.Application:
    """Return the global :class:`vispy.app.Application` instance."""

    global _VISPY_APP

    if backend is not None:
        use_app(backend)

    if _VISPY_APP is None:
        backend_name = CONFIG.get('VISPY_BACKEND')
        _VISPY_APP = visapp.application.Application(backend_name)
        CONFIG['VISPY_APP'] = _VISPY_APP
    return _VISPY_APP


def use_app(backend_name):
    """Use a specific backend."""
    backend = backend_name.lower() if isinstance(backend_name, str) else backend_name
    CONFIG['VISPY_BACKEND'] = backend
    global _VISPY_APP
    _VISPY_APP = visapp.application.Application(backend)
    CONFIG['VISPY_APP'] = _VISPY_APP
    return _VISPY_APP


# MPL render :
CONFIG['MPL_RENDER'] = False

# Jupyter / iPython :
try:
    ip = get_ipython()
    CONFIG['MPL_RENDER'] = True
    import vispy

    vispy.use(CONFIG['VISPY_BACKEND'])
except NameError:
    pass

# Input command line arguments
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


def init_config(argv):
    """Initialize visbrain configuration."""
    global CONFIG

    argnames = ['visbrain-log=', 'visbrain-show=', 'visbrain-help',
                'visbrain-search=']
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', argnames)
    except getopt.GetoptError:
        opts = []

    for o, a in opts:
        if o.startswith('--visbrain'):
            if o == '--visbrain-help':
                print(VISBRAIN_HELP)
            if o == '--visbrain-log':
                set_log_level(a)
            if o == '--visbrain-show':
                try:
                    CONFIG['SHOW_PYQT_APP'] = _parse_bool_flag(a)
                except ValueError:
                    logger.error(
                        f"Invalid value for --visbrain-show: {a}"
                    )
                else:
                    logger.debug(
                        "Show PyQt app : %r", CONFIG['SHOW_PYQT_APP']
                    )
            if o == '--visbrain-search':
                set_log_level(match=a)

init_config(sys.argv[1:])  # noqa
