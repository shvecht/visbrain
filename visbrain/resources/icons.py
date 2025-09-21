"""Helpers for working with bundled Visbrain icon assets."""
from __future__ import annotations

import logging
from importlib import resources
from typing import Optional

from ..qt import Qt, QtCore, QtGui

logger = logging.getLogger("visbrain")

_ICON_PACKAGE = "visbrain.resources.icons"


def _render_svg_icon(data: bytes) -> Optional[QtGui.QIcon]:
    """Render an SVG *data* payload into a :class:`~QtGui.QIcon`.

    Some Qt builds require the :mod:`QtSvg` module for SVG support.  When the
    direct :func:`~QtGui.QPixmap.loadFromData` path fails we fall back to
    :class:`~Qt.QSvgRenderer` so that icons bundled in the Visbrain wheel work
    across bindings.
    """

    renderer_cls = getattr(Qt, "QSvgRenderer", None)
    if renderer_cls is None:  # pragma: no cover - optional Qt module
        return None

    byte_array = QtCore.QByteArray(data)
    renderer = renderer_cls(byte_array)
    if not renderer.isValid():  # pragma: no cover - defensive guard
        return None

    default_size = renderer.defaultSize()
    if not default_size.isValid():
        default_size = QtCore.QSize(256, 256)

    image = QtGui.QImage(default_size, QtGui.QImage.Format_ARGB32)
    image.fill(0)

    painter = QtGui.QPainter(image)
    try:
        renderer.render(painter)
    finally:
        painter.end()

    return QtGui.QIcon(QtGui.QPixmap.fromImage(image))


def load_icon(icon_name: str) -> Optional[QtGui.QIcon]:
    """Return a :class:`~QtGui.QIcon` for *icon_name* or ``None`` if missing."""

    if not icon_name:
        logger.debug("No icon requested.")
        return None

    try:
        icon_resource = resources.files(_ICON_PACKAGE)
    except ModuleNotFoundError:  # pragma: no cover - packaging error
        logger.debug("Icon package missing for %s", icon_name)
        return None

    icon_path = icon_resource.joinpath(icon_name)
    if not icon_path.is_file():
        logger.debug("No icon found (%s)", icon_name)
        return None

    try:
        icon_bytes = icon_path.read_bytes()
    except FileNotFoundError:  # pragma: no cover - zip importer
        logger.debug("Unable to access icon resource (%s)", icon_name)
        return None

    pixmap = QtGui.QPixmap()
    if pixmap.loadFromData(icon_bytes):
        return QtGui.QIcon(pixmap)

    # Attempt to render SVG payloads via QtSvg when available.
    icon = _render_svg_icon(icon_bytes)
    if icon is not None:
        return icon

    logger.debug("Failed to create icon from %s", icon_name)
    return None


__all__ = ["load_icon"]
