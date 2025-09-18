"""Visbrain configurations."""
import sys
import getopt
import logging
import os

try:
    from PySide6 import QtWidgets
except ImportError:  # pragma: no cover - legacy fallback
    from PyQt5 import QtWidgets  # type: ignore
from vispy import app as visapp

from visbrain.utils.others import Profiler
from visbrain.utils.logging import set_log_level


# Set 'info' as the default logging level
logger = logging.getLogger('visbrain')
set_log_level('info')

# Configuration dict
CONFIG = {}

# Visbrain profiler (derived from the VisPy profiler)
PROFILER = Profiler()

# PyQt application
PYQT_APP = QtWidgets.QApplication.instance()
if PYQT_APP is None:
    PYQT_APP = QtWidgets.QApplication([''])
CONFIG['PYQT_APP'] = PYQT_APP
CONFIG['SHOW_PYQT_APP'] = True

# VisPy application
_VISPY_BACKEND = os.environ.get("VISPY_BACKEND") or "pyside6"
try:
    CONFIG['VISPY_APP'] = visapp.use_app(_VISPY_BACKEND)
except Exception:  # pragma: no cover - fallback when backend missing
    try:
        CONFIG['VISPY_APP'] = visapp.use_app('pyqt5')
    except Exception:
        class _StubVispyApp:
            def __init__(self, backend: str) -> None:
                self.backend = backend

            def run(self) -> None:  # pragma: no cover - simple stub
                return None

            def quit(self) -> None:  # pragma: no cover - simple stub
                return None

        CONFIG['VISPY_APP'] = _StubVispyApp(_VISPY_BACKEND)


def use_app(backend_name):
    """Use a specific backend."""
    CONFIG['VISPY_APP'] = visapp.application.Application(backend_name)


# MPL render :
CONFIG['MPL_RENDER'] = False

# Jupyter / iPython :
try:
    ip = get_ipython()
    CONFIG['MPL_RENDER'] = True
    import vispy
    try:
        vispy.use('pyside6')
    except Exception:  # pragma: no cover - fallback to legacy backend
        vispy.use('PyQt5')
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
                CONFIG['SHOW_PYQT_APP'] = eval(a)
                logger.debug("Show PyQt app : %r" % CONFIG['SHOW_PYQT_APP'])
            if o == '--visbrain-search':
                set_log_level(match=a)

init_config(sys.argv[1:])  # noqa
