"""This script group the diffrent graphical components.

Grouped components :
    * Qt elements (window, Qt functions...)
    * Vispy canvas functions
    * User shortcuts
"""

from visbrain.qt import QtCore, QtWidgets

from vispy import app
from vispy.scene.cameras import TurntableCamera

from .gui import Ui_MainWindow
from visbrain.objects import VisbrainCanvas
from visbrain.gui._accessibility import annotate_widget_accessibility


class BrainShortcuts(object):
    """This class add some shortcuts to the main canvas of Brain."""

    def __init__(self, canvas):
        """Init."""
        self.sh = [('<space>', 'Brain transparency'),
                   ('<delete>', 'Reset camera'),
                   ('0', 'Top view'),
                   ('1', 'Bottom view'),
                   ('2', 'Left view'),
                   ('3', 'Right view'),
                   ('4', 'Front view'),
                   ('5', 'Back view'),
                   ('b', 'Display / hide brain'),
                   ('x', 'Display / hide cross-sections'),
                   ('v', 'Display / hide volume'),
                   ('s', 'Display / hide sources'),
                   ('t', 'Display / hide connectivity'),
                   ('r', 'Display / hide ROI'),
                   ('c', 'Display / hide colorbar'),
                   ('a', 'Auto-scale the colormap'),
                   ('+', 'Increase brain opacity'),
                   ('-', 'Decrease brain opacity'),
                   ('CTRL + p', 'Run the cortical projection'),
                   ('CTRL + r', 'Run the cortical repartition'),
                   ('CTRL + d', 'Display / hide setting panel'),
                   ('CTRL + e', 'Show the documentation'),
                   ('CTRL + t', 'Display shortcuts'),
                   ('CTRL + n', 'Screenshot of the main canvas'),
                   ('CTRL + n', 'Screenshot of the entire window'),
                   ('CTRL + q', 'Exit'),
                   ]

        # Add shortcuts to BrainCanvas :
        @canvas.events.key_press.connect
        def on_key_press(event):
            """Handle keyboard input that targets the Brain canvas.

            :event: the trigger event
            """
            # Internal / external view :
            if event.text == ' ':
                viz = self._brain_translucent.isChecked()
                self._brain_translucent.setChecked(not viz)
                self._fcn_brain_translucent()

            # Increase / decrease brain opacity :
            elif event.text in ['+', '-']:
                # Force to be transparent :
                self._brain_translucent.setChecked(True)
                self._fcn_brain_translucent()
                # Get slider value :
                sl = self._brain_alpha.value()
                step = 1 if event.text == '+' else -1
                self._brain_alpha.setValue(sl + step)
                self._fcn_brain_alpha()

                # Colormap :
            elif event.text == 'a':
                self.cbqt._fcn_cb_autoscale()

        @canvas.events.mouse_release.connect
        def on_mouse_release(event):
            """Executed function when the mouse is pressed over Brain canvas.

            :event: the trigger event
            """
            # Hide the rotation panel :
            self.userRotationPanel.setVisible(False)

        @canvas.events.mouse_double_click.connect
        def on_mouse_double_click(event):
            """Executed function when double click mouse over Brain canvas.

            :event: the trigger event
            """
            pass

        @canvas.events.mouse_move.connect
        def on_mouse_move(event):
            """Executed function when the mouse move over Brain canvas.

            :event: the trigger event
            """
            if isinstance(self.view.wc.camera, TurntableCamera):
                # Display the rotation panel and set informations :
                self._fcn_gui_rotation()

        @canvas.events.mouse_press.connect
        def on_mouse_press(event):
            """Executed function when single click mouse over Brain canvas.

            :event: the trigger event
            """
            if isinstance(self.view.wc.camera, TurntableCamera):
                # Display the rotation panel :
                self._fcn_gui_rotation()
                self.userRotationPanel.setVisible(True)


class UiInit(QtWidgets.QMainWindow, Ui_MainWindow, app.Canvas, BrainShortcuts):
    """Group and initialize the graphical elements and interactions."""

    def __init__(self, bgcolor=(0.1, 0.1, 0.1)):
        """Init."""
        # Create the main window :
        super(UiInit, self).__init__(None)
        self.setupUi(self)
        self.setAccessibleName("Brain window")
        self.setAccessibleDescription(
            "Interactive 3D brain visualization with keyboard accessible controls."
        )
        annotate_widget_accessibility(
            self,
            extra={
                "_objsPage": (
                    "Visualization panels",
                    (
                        "Stacked configuration panels controlling brain, sources, "
                        "and derived visualizations."
                    ),
                ),
            },
        )

        #######################################################################
        #                            BRAIN CANVAS
        #######################################################################
        cdict = {'bgcolor': bgcolor, 'cargs': {'size': (800, 600), 'dpi': 600,
                 'fullscreen': True, 'resizable': True}}
        self.view = VisbrainCanvas(name='MainCanvas', camera=self._camera,
                                   **cdict)
        self.vBrain.addWidget(self.view.canvas.native)
        self.view.canvas.native.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.view.canvas.native.setAccessibleName("Brain canvas")
        self.view.canvas.native.setAccessibleDescription(
            "Primary 3D canvas displaying the brain surface and overlays."
        )

        #######################################################################
        #                         CROSS-SECTIONS CANVAS
        #######################################################################
        self._csView = VisbrainCanvas(name='SplittedCrossSections', **cdict)
        self._axialLayout.addWidget(self._csView.canvas.native)
        self._csView.canvas.native.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._csView.canvas.native.setAccessibleName("Cross-sections canvas")
        self._csView.canvas.native.setAccessibleDescription(
            "Orthogonal cross-section views linked to the main brain canvas."
        )

        # Initialize shortcuts :
        BrainShortcuts.__init__(self, self.view.canvas)
