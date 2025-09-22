Development workflow
====================

Qt interface regeneration
-------------------------

The Brain, Sleep, Signal, and Figure GUIs rely on Qt Designer assets stored
under ``visbrain/gui/*/interface``.  After adjusting a ``.ui`` file in any of
those modules, regenerate the corresponding Python wrappers with::

   make qt-ui

The command wraps :mod:`PySide6`'s ``pyside6-uic`` and ``pyside6-rcc`` tools and
touches every generated module under ``visbrain/gui/*/interface``.  Continuous
integration now executes ``python tools/generate_qt_ui.py --check`` as part of
:command:`make flake`, so linting fails whenever committed artifacts are
stale.  Run ``make qt-ui`` immediately after editing Qt resources and then
re-run ``make flake`` to verify that everything is up to date before sending a
pull request.
