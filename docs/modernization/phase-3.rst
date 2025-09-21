Phase 3 — Widget regeneration and Qt 6 alignment
================================================

Overview
--------

Phase 3 focuses on regenerating the Qt widget stack so the GUI matches the
runtime guarantees introduced earlier in the roadmap.  Legacy PyQt5 code paths
are rewritten against Qt 6 idioms, packaging assets that were previously baked
into ``*.ui`` files, and layering new view/controller helpers on top of the
configuration facade delivered in Phase 2.  The deliverables keep automated
testing headless-friendly while ensuring interactive launches feel native on the
current desktop platforms.

Baseline dependencies
---------------------

The regeneration effort continues to target the platform assumptions ratified in
Phase 0 and codified throughout Phase 1:

* **Qt binding**: PySide6 >= 6.7.1 remains the official GUI backend.  It ships
  ``shiboken6`` wheels for every supported OS and tracks Qt 6 API behavior
  closely, reducing the amount of adapter code the team must maintain.
* **Python**: 3.9 through 3.12, ensuring alignment with NumPy, PySide6 and the
  scientific stack we ship to end users.
* **Operating systems**: Windows 10/11 (x86_64), macOS 12 Monterey or newer
  (arm64 and x86_64), and Ubuntu 22.04 LTS or newer on x86_64.
* **VisPy**: 0.13.0 or newer, matching the renderer minimum already pinned in
  ``pyproject.toml`` and the requirements sets.

Widget regeneration strategy
----------------------------

The regenerated widgets embrace Qt 6 patterns directly rather than layering
compatibility shims.  Designers export fresh ``.ui`` definitions that PySide6 can
consume without the ``pyside2-uic`` backport scripts, and controllers migrate to
Qt's type-hinted signal/slot API.  ``VisbrainConfig`` continues to own feature
flags (Matplotlib rendering, telemetry opt-ins and GUI visibility) so newly
ported dialogs and editors respect the same toggles that Phase 2 introduced for
tests and automation.

Hosting regenerated applications
--------------------------------

Phase 2's lazy application factories now provide the execution surface for the
Qt 6 widgets.  ``ensure_qt_app()`` and ``ensure_vispy_app()`` create
``QApplication`` and VisPy ``Application`` instances on demand, so the refreshed
GUIs register themselves by requesting the handles from the shared configuration
rather than building their own globals.  The factories expose context managers
and ``force`` flags, allowing regenerated widgets to request an interactive host
in desktop sessions while remaining inert during headless test runs.  This keeps
the event loop lifecycle centralized and prepares the ground for future plugins
that will drop widgets into the same app container.

Rollout and testing
-------------------

* Update GUI packages module-by-module, validating each rewrite with pytest
  suites that exercise the lazy factories in headless mode.
* Ship Sphinx gallery examples that open the rebuilt widgets via
  ``ensure_qt_app(force=True)`` so documentation captures the new APIs.
* Refresh contributor guides once the regenerated stack lands, highlighting the
  PySide6 workflow, the supported Python/OS matrix and the VisPy baseline so
  developers verify patches on the official matrix before submitting changes.

Supporting inventory
--------------------

* :doc:`phase-3-inventory`
