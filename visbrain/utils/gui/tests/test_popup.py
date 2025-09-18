"""Test functions in popup.py."""
import pytest

try:  # pragma: no cover - optional Qt bindings
    from visbrain.qt import QtWidgets
except ImportError:  # pragma: no cover - Qt not installed
    QtWidgets = None

from visbrain.utils.gui.popup import (ShortcutPopup, ScreenshotPopup, HelpMenu)


pytestmark = pytest.mark.skipif(
    QtWidgets is None, reason="Qt bindings are unavailable"
)


class TestPopup(object):
    """Test functions in popup.py."""

    @pytest.mark.skip('Too much app creation => segmentation fault')
    def test_shortcut_popup(self):
        """Test function ShortcutPopup."""
        sh = [('key1', 'Action1'), ('key2', 'Action2')]
        app = QtWidgets.QApplication([])  # noqa
        pop = ShortcutPopup()
        pop.set_shortcuts(sh)
        # app.quit()

    @pytest.mark.skip('Too much app creation => segmentation fault')
    def test_screenshot_popup(self):
        """Test function ScreenshotPopup."""
        def fcn():
            pass
        app = QtWidgets.QApplication([])  # noqa
        sc = ScreenshotPopup(fcn)
        sc._fcn_select_render()
        sc._fcn_resolution()
        sc.to_kwargs()
        sc._fcn_enable_bgcolor()
        # app.quit()

    @pytest.mark.skip('Too much app creation => segmentation fault')
    def test_help_menu(self):
        """Test function HelpMenu."""
        HelpMenu()
