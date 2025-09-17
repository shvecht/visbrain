Phase 1 — Packaging and Dependency Overhaul
===========================================

Overview
--------

Phase 1 focuses on modern packaging primitives so the project can build with
current Python toolchains. The guiding principles are:

* publish metadata through ``pyproject.toml`` rather than ``setup.py``;
* raise dependency floors to versions that support Python 3.9+; and
* codify PySide6 as the supported Qt binding across packaging inputs.

Key changes
-----------

``pyproject.toml`` now drives builds with ``setuptools`` >= 68. The
configuration pulls the version from :mod:`visbrain`, exposes extras that mirror
past ``setup.py`` options, and declares a modern Python range. ``setup.py`` is
retained as a thin shim so existing workflows that call ``python setup.py``
continue to function.

The pinned requirement files were refreshed to align with the metadata. PySide6
and its companion ``shiboken6`` package anchor the runtime stack, while the
optional extras mirror the ``pyproject.toml`` extras. ``MANIFEST.in`` will
continue to ship the resource files consumed at runtime.

Developer workflow
------------------

To build or install from a checkout::

   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   python -m pip install --upgrade pip
   python -m pip install -r requirements/dev.txt
   python -m build

The ``build`` command validates that the ``pyproject.toml`` metadata is
self-consistent and produces an sdist/wheel. Contributors can also install in
editable mode with ``pip install -e .`` when iterating locally.

Next steps
----------

* Convert continuous integration workflows to rely on ``pyproject.toml`` so
  future jobs no longer invoke ``setup.py`` directly.
* Begin extracting Qt-bound logic into dedicated adapters so Phase 2 can
  standardize on PySide6-friendly abstractions.
* Audit package data requirements and move any implicit resources into explicit
  ``tool.setuptools.package-data`` declarations.
