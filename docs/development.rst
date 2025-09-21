Development workflow
====================

Qt interface regeneration
-------------------------

The Brain and Sleep GUIs rely on Qt Designer files stored under
``visbrain/gui/*/interface``. After adjusting a ``.ui`` file, regenerate the
corresponding Python module with::

   make qt-ui

The command wraps :mod:`PySide6`'s ``pyside6-uic`` and ``pyside6-rcc`` tools and
updates every generated module in place.  Continuous integration now executes
``python tools/generate_qt_ui.py --check`` as part of :command:`make flake`, so
linting fails whenever committed artifacts are stale.  Run ``make qt-ui`` after
editing Qt resources and re-run ``make flake`` to verify that everything is
up to date before sending a pull request.
