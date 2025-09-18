"""
Hardware accelerated graphics for neuscientific data
====================================================

visbrain is an open-source Python software mainly dedicated to the
visualization of neuroscientific data. It's developped on top of VisPy which
provides graphic renderings offloaded to the GPU.

Right now, visbrain contains five modules :
* Brain : visualize EEG/MEG/Intracranial data and connectivity in a standard
  MNI 3D brain.
* Sleep : visualize polysomnographic data and hypnogram edition.
* Signal : data mining module for signal inspection.
* Figure : figure-layout for high-quality publication-like figures.
* Topo : topographic representations

See http://visbrain.org/ for a complete and step-by step documentation
"""
import sys as _sys

__version__ = "0.4.6"


# Qt bindings can crash if an error occurs. This small function fixes it for
# all modules to retrieve the original PyQt4 behavior:


def _qt_behavior(type, value, tback):
    """Preserve the legacy Qt exception hook behaviour."""
    _sys.__excepthook__(type, value, tback)


_sys.excepthook = _qt_behavior
