"""All visbrain modules based on Qt should inherit from _PyQtModule."""
from __future__ import annotations

import atexit
import logging
from importlib import resources

from .qt import QtGui, QtWidgets, QT_API

try:  # pragma: no cover - optional dependency during transition
    if QT_API == "PyQt5":
        import sip  # type: ignore
    else:  # pragma: no branch - PySide environments skip sip
        sip = None
except ImportError:  # pragma: no cover - sip missing
    sip = None

try:  # pragma: no cover - optional dependency during transition
    if QT_API and QT_API.startswith("PySide"):
        import shiboken6  # type: ignore
    else:  # pragma: no branch - not needed on PyQt5
        shiboken6 = None
except ImportError:  # pragma: no cover - shiboken missing
    shiboken6 = None

from .utils import set_widget_size, set_log_level
from .config import PROFILER, get_config, qt_app, vispy_app
from .io import path_to_tmp, clean_tmp, path_to_visbrain_data

logger = logging.getLogger('visbrain')


def _guard_qapp_lifecycle() -> None:
    """Apply the appropriate guard for the active Qt binding."""
    if QT_API == "PyQt5" and sip is not None:
        sip.setdestroyonexit(False)
        return

    if QT_API and QT_API.startswith("PySide") and shiboken6 is not None:
        # PySide bindings historically crashed when the QApplication was torn
        # down while widgets were still alive. Requesting a graceful shutdown
        # prevents this without relying on PyQt's sip module.
        def _cleanup_qapp() -> None:
            app = QtWidgets.QApplication.instance()
            if app is not None and shiboken6.isValid(app):
                app.quit()

        atexit.register(_cleanup_qapp)


_guard_qapp_lifecycle()


class _PyQtModule(object):
    """Shared methods across PyQt based Visbrain modules.

    Parameters
    ----------
    verbose : logging.level | None
        Verbosity level.
    to_describe : string | None
        The parent node to describe. Only available if verbose level is on
        debug.
    icon : str | None
        Name of the icon to use.
    """

    def __init__(self, verbose=None, to_describe=None, icon=None,
                 show_settings=True):
        """Init."""
        # Log level and profiler creation (if verbose='debug')
        set_log_level(verbose)
        path_to_visbrain_data(create=True, allow_bundled=False)
        self._create_tmp_folder()
        if logger.level == 10:
            import faulthandler
            faulthandler.enable()
            logger.debug("Faulthandler enabled")
        self._need_description = to_describe
        if isinstance(self._need_description, str):
            self._need_description = [self._need_description]
        self._module_icon = icon
        self._show_settings = show_settings

    ###########################################################################
    #                               TMP FOLDER
    ###########################################################################

    def _path_to_tmp_folder(self):
        return path_to_tmp()

    def _create_tmp_folder(self):
        tmp_path = path_to_tmp()
        logger.debug("tmp folder created (%s)." % tmp_path)

    def _clean_tmp_folder(self):
        tmp_path = clean_tmp()
        logger.debug("tmp folder cleaned (%s)." % tmp_path)

    ###########################################################################
    #                            SHOW // CLOSE
    ###########################################################################
    def _pyqt_title(self, title, msg, symbol='='):
        """Define a PyQt title."""
        assert isinstance(title, str) and isinstance(symbol, str)
        n_symbol = 60
        start_title = int((n_symbol / 2) - (len(title) / 2)) - 1
        upper_bar = symbol * n_symbol
        title_bar = ' ' * start_title + title
        title_template = "\n%s\n%s\n\n{msg}" % (upper_bar, title_bar)
        logger.profiler(title_template.format(msg=msg))

    def show(self):
        """Display the graphical user interface."""
        with qt_app() as app:
            if hasattr(self, 'q_widget') and app is not None:
                set_widget_size(app, self.q_widget, 23)
                self.q_widget.setVisible(self._show_settings)
            # Force the quick settings tab to be on the first tab :
            if hasattr(self, 'QuickSettings'):
                self.QuickSettings.setCurrentIndex(0)
            # Set icon (if possible) :
            if isinstance(self._module_icon, str):
                try:
                    icon_resource = resources.files("visbrain.resources.icons")
                except ModuleNotFoundError:  # pragma: no cover - packaging error
                    logger.debug("Icon package missing for %s", self._module_icon)
                else:
                    icon_path = icon_resource.joinpath(self._module_icon)
                    if icon_path.is_file():
                        try:
                            with resources.as_file(icon_path) as icon_file:
                                app_icon = QtGui.QIcon()
                                app_icon.addFile(str(icon_file))
                                self.setWindowIcon(app_icon)
                        except FileNotFoundError:  # pragma: no cover - zip importer
                            logger.debug("No icon found (%s)" % self._module_icon)
                    else:  # don't crash just for an icon...
                        logger.debug("No icon found (%s)" % self._module_icon)
            else:
                logger.debug("No icon passed as an input.")
            # Tree description if log level is on debug :
            if isinstance(self._need_description, list):
                for k in self._need_description:
                    self._pyqt_title('Tree', eval('self.%s.describe_tree()' % k))
            # Show and maximized the window :
            if PROFILER and logger.level == 1:
                self._pyqt_title('Profiler', '')
                PROFILER.finish()
            # If PyQt GUI :
            cfg = get_config()
            if cfg.show_pyqt_app:
                self.showMaximized()
                with vispy_app() as active_vispy:
                    if active_vispy is not None:
                        active_vispy.run()
        # Finally clean the tmp folder :
        self._clean_tmp_folder()

    def closeEvent(self, event):  # noqa
        """Executed method when the GUI closed."""
        cfg = get_config()
        app = cfg.get_qt_app(create=False)
        if app is not None:
            app.quit()
        logger.debug("App closed.")
