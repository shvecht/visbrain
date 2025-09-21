Phase 3 legacy GUI inventory
============================

The notes below catalog the legacy Qt widgets, VisPy integration points and
related resources that still power the four GUI surface areas targeted in Phase
3.  Each module entry groups the generated ``.ui`` files, the Python helpers
that assemble the layouts at runtime, and the VisPy hooks that need to be
reworked during the modernization pass.

.. contents:: Module overview
   :local:

Brain module
------------

Legacy UI and layout sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``visbrain/gui/brain/interface/gui/brain_gui.ui`` — legacy Qt Designer export
  consumed via the auto-generated ``brain_gui.py`` wrapper produced by
  ``pyuic5`` 5.11.2.【F:visbrain/gui/brain/interface/gui/brain_gui.py†L1-L103】
* ``visbrain/gui/brain/interface/ui_init.py`` — creates the ``QMainWindow`` and
  embeds the VisPy canvases that fill the Designer placeholders for the brain
  and cross-section panes.【F:visbrain/gui/brain/interface/ui_init.py†L118-L140】
* ``visbrain/gui/brain/interface/ui_elements`` — mix-in package that wires the
  tab stacks, menus and tool panels exposed by the generated UI before handing
  control to the higher-level ``Brain`` class.【F:visbrain/gui/brain/interface/ui_elements/ui_elements.py†L1-L32】

VisPy entry points
^^^^^^^^^^^^^^^^^^

* ``Brain.__init__`` instantiates a ``TurntableCamera`` and binds it to the
  primary ``VisbrainCanvas`` node, forwarding shared camera handles to atlas,
  ROI and colorbar visuals.【F:visbrain/gui/brain/brain.py†L91-L129】
* ``UiInit`` builds the ``VisbrainCanvas`` instances for the main brain scene
  and cross-section viewer, exposing their native Qt widgets for layout
  insertion.【F:visbrain/gui/brain/interface/ui_init.py†L118-L140】
* ``BrainShortcuts`` attaches keyboard and mouse handlers directly to the VisPy
  canvas event system for transparency toggles, rotation aides and autoscaling
  actions.【F:visbrain/gui/brain/interface/ui_init.py†L18-L115】
* ``Visuals.__init__`` seeds a VisPy scene node hierarchy, attaching combined
  source, connectivity, time-series and auxiliary visuals (including the
  cross-section canvas and ROI) underneath the root node shared with the main
  window cameras.【F:visbrain/gui/brain/visuals.py†L15-L83】

Resource loaders
^^^^^^^^^^^^^^^^

* ``Brain`` requests the ``brain_icon.svg`` module icon through
  ``_PyQtModule``, which in turn resolves the asset via the shared icon loader
  before the Qt window is shown.【F:visbrain/gui/brain/brain.py†L91-L132】【F:visbrain/_pyqt_module.py†L12-L68】

Modernization flags
^^^^^^^^^^^^^^^^^^^

* ``UiInit`` still subclasses ``vispy.app.Canvas`` alongside ``QMainWindow``, a
  pattern that predates ``SceneCanvas`` embedding and should be replaced with a
  direct ``SceneCanvas`` wrapper for Qt 6 compatibility.【F:visbrain/gui/brain/interface/ui_init.py†L118-L140】
* The generated ``brain_gui.py`` targets PyQt5 and must be regenerated with a
  Qt 6 toolchain to match the roadmap baseline.【F:visbrain/gui/brain/interface/gui/brain_gui.py†L1-L105】

Signal module
-------------

Legacy UI and layout sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``visbrain/gui/signal/interface/gui/signal_gui.ui`` — Qt Designer definition
  compiled with the Qt 6 toolchain into ``signal_gui.py`` for runtime use.【F:visbrain/gui/signal/interface/gui/signal_gui.py†L1-L40】
* ``visbrain/gui/signal/ui_elements/ui_init.py`` — instantiates the main window
  shell, allocates grid and detail ``VisbrainCanvas`` widgets, and positions
  them inside the Designer placeholders.【F:visbrain/gui/signal/ui_elements/ui_init.py†L130-L158】
* ``visbrain/gui/signal/ui_elements`` — helper mix-ins that populate the tabbed
  controls, menus and settings tied to the generated UI skeleton.【F:visbrain/gui/signal/signal.py†L5-L188】

VisPy entry points
^^^^^^^^^^^^^^^^^^

* ``Signal.__init__`` bootstraps ``UiInit`` and routes the two VisPy canvases to
  the visualization layer so grid and single-signal scenes share the same data
  model.【F:visbrain/gui/signal/signal.py†L124-L163】
* ``UiInit`` wires ``PanZoomCamera`` instances to the grid, signal and colorbar
  canvases that power the viewer layouts.【F:visbrain/gui/signal/ui_elements/ui_init.py†L139-L154】
* ``GridShortcuts`` and ``SignalShortcuts`` bind mouse double-click and keyboard
  handlers on the VisPy canvases to drive selection navigation and annotation
  insertion.【F:visbrain/gui/signal/ui_elements/ui_init.py†L14-L128】
* ``Visuals.__init__`` constructs the VisPy visuals (grid plot, TF maps,
  annotations) and transforms that render inside the canvases exposed by
  ``UiInit``.【F:visbrain/gui/signal/visuals.py†L1-L180】

Resource loaders
^^^^^^^^^^^^^^^^

* ``Signal`` relies on ``_PyQtModule`` for lifecycle management but does not yet
  request a dedicated module icon; assets are limited to Matplotlib exports via
  ``write_fig_canvas`` for screenshots.【F:visbrain/gui/signal/signal.py†L9-L188】

Modernization flags
^^^^^^^^^^^^^^^^^^^

* ``UiInit`` inherits the legacy ``vispy.app.Canvas`` base and should migrate to
  explicit ``SceneCanvas`` embedding under Qt 6, matching the modernization
  target shared with the other GUIs.【F:visbrain/gui/signal/ui_elements/ui_init.py†L130-L158】
* ``signal_gui.py`` now targets PySide6 and ships from the ``interface``
  namespace, aligning the Signal module with the modernization baseline.【F:visbrain/gui/signal/interface/gui/signal_gui.py†L1-L40】

Sleep module
------------

Legacy UI and layout sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``visbrain/gui/sleep/interface/gui/sleep_gui.ui`` — Designer layout compiled
  by PyQt5 5.8.2 for widget scaffolding consumed through ``sleep_gui.py``.【F:visbrain/gui/sleep/interface/gui/sleep_gui.py†L1-L120】
* ``visbrain/gui/sleep/interface/ui_init.py`` — initializes the ``QMainWindow``
  shell and exposes builder helpers (``TimeAxis``, ``AxisCanvas``) that attach
  additional VisPy canvases to the UI placeholders.【F:visbrain/gui/sleep/interface/ui_init.py†L19-L159】
* ``visbrain/gui/sleep/interface/ui_elements`` — mix-in package that assembles
  the stacked panels, detection widgets, menus and screenshots tabs declared in
  the generated UI.【F:visbrain/gui/sleep/interface/ui_elements/ui_elements.py†L1-L24】
* ``visbrain/gui/sleep/view.py`` — wraps ``UiInit`` into a higher-level view
  object and defers camera construction until the controller knows how many
  channel canvases to allocate.【F:visbrain/gui/sleep/view.py†L12-L58】

VisPy entry points
^^^^^^^^^^^^^^^^^^

* ``SleepView.create_cameras`` attaches ``FixedCam`` and ``PanZoomCamera``
  instances to each VisPy canvas (channel stack, spectrogram, hypnogram, topo
  map and global time axis).【F:visbrain/gui/sleep/view.py†L29-L54】
* ``TimeAxis`` constructs a standalone ``SceneCanvas`` with an ``AxisWidget``,
  shared camera and marker overlay used to track current time and annotations in
  the GUI.【F:visbrain/gui/sleep/interface/ui_init.py†L29-L104】
* ``AxisCanvas`` provisions the channel, spectrogram and topo canvases with
  optional axes and links their cameras back to the Qt controls.【F:visbrain/gui/sleep/interface/ui_init.py†L107-L159】
* ``Visuals`` layer objects (detections, channel plots, spectrogram meshes,
  hypnogram markers) on the canvases exported by the view helpers, maintaining
  references for controller-driven updates.【F:visbrain/gui/sleep/visuals/visuals.py†L1-L116】

Resource loaders
^^^^^^^^^^^^^^^^

* ``Sleep`` requests the ``sleep_icon.svg`` asset through ``_PyQtModule`` so the
  Qt window shows the module icon when launched.【F:visbrain/gui/sleep/sleep.py†L15-L77】【F:visbrain/_pyqt_module.py†L12-L68】

Modernization flags
^^^^^^^^^^^^^^^^^^^

* ``UiInit`` still subclasses ``vispy.app.Canvas`` instead of embedding
  ``SceneCanvas`` widgets through Qt-friendly wrappers, which complicates Qt 6
  adoption.【F:visbrain/gui/sleep/interface/ui_init.py†L19-L59】
* The generated ``sleep_gui.py`` targets PyQt5 and must be regenerated under the
  PySide6/Qt 6 toolchain noted in the roadmap.【F:visbrain/gui/sleep/interface/gui/sleep_gui.py†L1-L120】

Figure module
-------------

Legacy UI and layout sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The figure helper does not rely on Qt Designer; the entire API is implemented
  in ``visbrain/gui/figure/figure.py`` and constructs Matplotlib figures
  directly.【F:visbrain/gui/figure/figure.py†L1-L200】

VisPy entry points
^^^^^^^^^^^^^^^^^^

* No VisPy canvases are created in this module; it focuses on arranging static
  image grids through Matplotlib and NumPy helpers.【F:visbrain/gui/figure/figure.py†L1-L200】

Resource loaders
^^^^^^^^^^^^^^^^

* Picture assets are read from disk via Matplotlib's ``imread`` and optional
  helper utilities for cropping and resizing; no Qt resource system is involved
  yet.【F:visbrain/gui/figure/figure.py†L3-L120】

Modernization flags
^^^^^^^^^^^^^^^^^^^

* The module depends solely on Matplotlib and NumPy, so modernization should
  focus on harmonizing file I/O and color management with the refreshed Qt/VisPy
  stack rather than Qt 6 migration.
