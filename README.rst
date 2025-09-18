========
Visbrain
========

.. image:: https://travis-ci.org/EtienneCmb/visbrain.svg?branch=master
    :target: https://travis-ci.org/EtienneCmb/visbrain

.. image:: https://ci.appveyor.com/api/projects/status/fdxhhmpagms1so8l/branch/master?svg=true
    :target: https://ci.appveyor.com/project/EtienneCmb/visbrain/branch/master

.. image:: https://circleci.com/gh/EtienneCmb/visbrain/tree/master.svg?style=svg
    :target: https://circleci.com/gh/EtienneCmb/visbrain/tree/master

.. image:: https://codecov.io/gh/EtienneCmb/visbrain/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/EtienneCmb/visbrain

.. image:: https://badge.fury.io/py/visbrain.svg
    :target: https://badge.fury.io/py/visbrain

.. image:: https://pepy.tech/badge/visbrain
    :target: https://pepy.tech/project/visbrain

.. image:: https://badges.gitter.im/visbrain-python/chatroom.svg
    :target: https://gitter.im/visbrain-python/chatroom?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge

.. figure::  https://github.com/EtienneCmb/visbrain/blob/master/docs/_static/ico/visbrain.png
    :align:  center

**Visbrain** is an open-source python 3 package dedicated to brain signals visualization. It is based on top of `VisPy <http://vispy.org/>`_ and the Qt 6 stack exposed through PySide6 and is distributed under the 3-Clause BSD license. We also provide an on line `documentation <http://visbrain.org>`_, `examples and datasets <http://visbrain.org/auto_examples/>`_ and can also be downloaded from `PyPi <https://pypi.python.org/pypi/visbrain/>`_.

Modernization roadmap
---------------------

Visbrain is currently undergoing a multi-phase modernization effort. Phase 0
has established the target execution environments and the development workflow
used by contributors while the code base is updated. The detailed plan lives in
``docs/modernization/phase-0.rst`` within the repository.

For day-to-day development work on this modernization track we recommend
creating a virtual environment that matches the Phase 0 baseline:

.. code-block:: console

   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\\Scripts\\activate
   python -m pip install --upgrade pip
   pip install -r requirements/dev.txt

These pins align with Python 3.9–3.12 on Windows, macOS, and Linux and will be
revisited during the packaging overhaul in Phase 1.

Important links
---------------

* Official source code repository : https://github.com/EtienneCmb/visbrain
* Online documentation : http://visbrain.org
* Visbrain `chat room <https://gitter.im/visbrain-python/chatroom?utm_source=share-link&utm_medium=link&utm_campaign=share-link>`_


Installation
------------

Dependencies
++++++++++++

Visbrain requires :

* NumPy >= 1.26.4
* SciPy >= 1.11.4
* VisPy >= 0.13.0
* Matplotlib >= 3.8.4
* PySide6 >= 6.7.1 (installs ``shiboken6``)
* Pillow >= 10.3.0
* PyOpenGL >= 3.1.7

User installation
+++++++++++++++++

Install Visbrain :

.. code-block:: console

    pip install -U visbrain

