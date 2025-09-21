"""Helpers for building VisPy scene graphs in a headless-friendly way."""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Iterator, Mapping, Optional, Sequence

from vispy import scene
import vispy.visuals.transforms as vist

from ..config import ensure_vispy_app, vispy_app

__all__ = [
    "SceneContext",
    "create_scene_canvas",
    "create_scene_node",
    "scene_canvas",
]


@dataclass
class SceneContext:
    """Bundle a :class:`~vispy.scene.SceneCanvas` and the attached view."""

    canvas: scene.SceneCanvas
    view: scene.widgets.viewbox.ViewBox

    @property
    def scene(self) -> scene.Node:
        """Return the root scene node backing the view."""

        return self.view.scene

    def create_node(
        self,
        *,
        name: str | None = None,
        transform: vist.BaseTransform | None = None,
        scale: Sequence[float] | float | None = None,
        translate: Sequence[float] | None = None,
    ) -> scene.Node:
        """Create a child node attached to this context's scene."""

        return create_scene_node(
            self.view,
            name=name,
            transform=transform,
            scale=scale,
            translate=translate,
        )


def _resolve_scene_parent(parent: Any) -> scene.Node:
    """Return the scene graph node associated with *parent*.

    Parameters
    ----------
    parent:
        Object exposing a ``scene`` attribute (``SceneCanvas``/``ViewBox``), a
        ``wc`` attribute (``VisbrainCanvas`` wrappers) or a :class:`SceneContext`.
    """

    if isinstance(parent, SceneContext):
        return parent.scene
    if isinstance(parent, scene.Node):
        return parent
    if hasattr(parent, "scene"):
        scene_graph = getattr(parent, "scene")
        if isinstance(scene_graph, scene.Node):
            return scene_graph
    if hasattr(parent, "wc"):
        wc = getattr(parent, "wc")
        return _resolve_scene_parent(wc)
    if hasattr(parent, "canvas"):
        canvas = getattr(parent, "canvas")
        if isinstance(canvas, scene.SceneCanvas):
            return canvas.scene
    raise TypeError(
        "Unable to resolve a scene graph node from %r" % (parent,)
    )


def create_scene_node(
    parent: Any,
    *,
    name: str | None = None,
    transform: vist.BaseTransform | None = None,
    scale: Sequence[float] | float | None = None,
    translate: Sequence[float] | None = None,
) -> scene.Node:
    """Create a :class:`~vispy.scene.Node` attached to *parent*.

    The helper resolves the appropriate parent node and ensures the global
    VisPy application exists using the Phase 2 lazy factories.
    """

    ensure_vispy_app()
    parent_node = _resolve_scene_parent(parent)
    node = scene.Node(name=name, parent=parent_node)

    if transform is None and (scale is not None or translate is not None):
        transform = vist.STTransform()

    if transform is not None:
        if scale is not None:
            transform.scale = scale
        if translate is not None:
            transform.translate = translate
        node.transform = transform

    return node


def create_scene_canvas(
    *,
    keys: str | None = "interactive",
    bgcolor: str | Sequence[float] = "black",
    size: Sequence[int] | None = None,
    show: bool = False,
    title: str | None = None,
    view_kwargs: Optional[Mapping[str, Any]] = None,
) -> SceneContext:
    """Instantiate a :class:`SceneCanvas` and return its context wrapper."""

    ensure_vispy_app()
    canvas = scene.SceneCanvas(
        keys=keys,
        bgcolor=bgcolor,
        show=show,
        title=title,
        size=size,
    )
    view = canvas.central_widget.add_view(**dict(view_kwargs or {}))
    return SceneContext(canvas=canvas, view=view)


@contextmanager
def scene_canvas(
    *,
    keys: str | None = "interactive",
    bgcolor: str | Sequence[float] = "black",
    size: Sequence[int] | None = None,
    show: bool = False,
    title: str | None = None,
    view_kwargs: Optional[Mapping[str, Any]] = None,
    force_app: bool = False,
) -> Iterator[SceneContext]:
    """Context manager yielding a :class:`SceneContext`.

    The manager cooperates with :func:`visbrain.config.vispy_app` so tests can
    request canvases without leaking global application state.
    """

    ensure_vispy_app(force=force_app)
    with vispy_app(force=force_app) as _:
        context = create_scene_canvas(
            keys=keys,
            bgcolor=bgcolor,
            size=size,
            show=show,
            title=title,
            view_kwargs=view_kwargs,
        )
        try:
            yield context
        finally:
            context.canvas.close()
