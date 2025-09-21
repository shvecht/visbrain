"""Accessibility helpers for Qt-based GUI widgets."""

from __future__ import annotations

from collections import defaultdict
from typing import List, Mapping, MutableMapping, Optional, Tuple

from visbrain.qt import QtCore, QtGui, QtWidgets


_Description = Tuple[str, str]

_DEFAULT_ACCESSIBLE: Mapping[str, _Description] = {
    "QuickSettings": (
        "Quick settings",
        "Tabbed container holding configuration panels for the active visualization.",
    ),
    "_stacked_panels": (
        "Visualization panel stack",
        "Switches between panel groups that expose visualization controls.",
    ),
    "_stacked_tools": (
        "Tool stack",
        "Groups advanced tools such as detections and processing controls.",
    ),
    "_stacked_detections": (
        "Detection stack",
        "Shows the configuration panels for automated detection workflows.",
    ),
    "statusbar": (
        "Status messages",
        "Displays contextual status updates for the active visualization.",
    ),
    "progressBar": (
        "Processing progress",
        "Indicates the completion state of long running computations.",
    ),
    "userRotationPanel": (
        "Camera orientation panel",
        "Reports the orientation and zoom state of the brain camera.",
    ),
    "userRotation": (
        "Camera orientation readout",
        "Current camera orientation expressed in azimuth and elevation degrees.",
    ),
}


def annotate_widget_accessibility(
    widget: QtWidgets.QWidget,
    *,
    extra: Optional[Mapping[str, _Description]] = None,
) -> None:
    """Attach human readable accessibility metadata to *widget* children.

    Parameters
    ----------
    widget:
        The root widget exposing attributes that map to child widgets.
    extra:
        Optional mapping of attribute names to ``(name, description)`` tuples.
        Entries override the default metadata for keys that already exist.
    """

    descriptions: MutableMapping[str, _Description]
    descriptions = dict(_DEFAULT_ACCESSIBLE)
    if extra:
        descriptions.update(extra)

    for attr, (name, description) in descriptions.items():
        target = getattr(widget, attr, None)
        if isinstance(target, QtWidgets.QWidget):
            if name and not target.accessibleName():
                target.setAccessibleName(name)
            if description and not target.accessibleDescription():
                target.setAccessibleDescription(description)


def install_action_shortcuts(
    widget: QtWidgets.QWidget,
    *,
    context: QtCore.Qt.ShortcutContext = QtCore.Qt.ApplicationShortcut,
    owner: Optional[Mapping[str, QtWidgets.QWidget]] = None,
) -> List[QtGui.QShortcut]:
    """Rebind QAction shortcuts to persistent :class:`QShortcut` objects.

    Parameters
    ----------
    widget:
        Widget that owns the actions.  The created shortcuts are stored on
        this widget via the ``_qt_action_shortcuts`` attribute to keep them
        alive for the lifetime of the widget.
    context:
        Shortcut context to assign to the generated shortcuts.
    owner:
        Optional mapping assigning alternative parent widgets for specific
        actions, keyed by the ``objectName`` of each :class:`QAction`.
    """

    grouped: MutableMapping[str, List[QtWidgets.QAction]] = defaultdict(list)
    for action in widget.findChildren(QtGui.QAction):
        sequence = action.shortcut()
        # ``QKeySequence`` exposes ``isEmpty`` starting with Qt6.
        if sequence.isEmpty():  # pragma: no cover - defensive
            continue
        text = sequence.toString(QtGui.QKeySequence.PortableText)
        if not text:
            continue
        action.setShortcut(QtGui.QKeySequence())
        grouped[text].append(action)

    shortcuts: List[QtGui.QShortcut] = []
    parent_map = owner or {}
    for text, actions in grouped.items():
        key_sequence = QtGui.QKeySequence(text)
        parent = parent_map.get(actions[0].objectName(), widget)
        shortcut = QtGui.QShortcut(key_sequence, parent)
        shortcut.setContext(context)
        for action in actions:
            shortcut.activated.connect(action.trigger)
        shortcuts.append(shortcut)

    setattr(widget, "_qt_action_shortcuts", shortcuts)
    return shortcuts
