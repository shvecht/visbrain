"""Bundled data access helpers for Visbrain."""
from __future__ import annotations

import atexit
import tempfile
from contextlib import ExitStack
from importlib import resources
from importlib.resources.abc import Traversable
from pathlib import Path, PurePosixPath
from typing import Callable, Iterable, Iterator, Mapping, MutableMapping, Union

from ._package_data import PACKAGE_REGISTRY

__all__ = [
    "bundled_path",
    "iter_bundled_files",
]


ResourceNode = Union[bytes, Callable[[], bytes], "ResourceTree"]
ResourceTree = Mapping[str, "ResourceNode"]


_STACK = ExitStack()
atexit.register(_STACK.close)

_DATA_PACKAGE = __name__
_CACHE: MutableMapping[PurePosixPath, Path] = {}


def _as_file(traversable: Traversable) -> Path:
    """Return a filesystem path for a resource, keeping temporary dirs alive."""

    return Path(_STACK.enter_context(resources.as_file(traversable)))


def _flatten(parts: Iterable[Union[str, Iterable[str]]]) -> Iterator[str]:
    for part in parts:
        if part is None:
            continue
        if isinstance(part, (list, tuple)):
            yield from _flatten(part)
        else:
            yield str(part)


def _lookup_registry(path: PurePosixPath) -> ResourceNode | None:
    node: ResourceNode = PACKAGE_REGISTRY
    for piece in path.parts:
        if isinstance(node, Mapping) and piece in node:
            node = node[piece]
        else:
            return None
    return node


def _resolve_bytes(value: ResourceNode) -> bytes:
    if isinstance(value, Mapping):
        raise TypeError("Expected byte payload, received a mapping")
    if callable(value):
        data = value()
    else:
        data = value
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Bundled payload must resolve to bytes")
    return bytes(data)


def _write_tree(base: Path, rel_path: PurePosixPath, tree: Mapping[str, ResourceNode]) -> None:
    for name, value in tree.items():
        child_rel = rel_path / name
        dest = base / name
        if isinstance(value, Mapping):
            dest.mkdir(parents=True, exist_ok=True)
            _CACHE[child_rel] = dest
            _write_tree(dest, child_rel, value)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(_resolve_bytes(value))
            _CACHE[child_rel] = dest


def _materialize(path: PurePosixPath, node: ResourceNode) -> Path:
    if isinstance(node, Mapping):
        temp_root = Path(_STACK.enter_context(tempfile.TemporaryDirectory(prefix="visbrain_data_")))
        target = temp_root.joinpath(*path.parts) if path.parts else temp_root
        target.mkdir(parents=True, exist_ok=True)
        _CACHE[path] = target
        _write_tree(target, path, node)
        return target

    # Ensure parent directories exist if part of the registry tree
    parent = path.parent
    if parent != PurePosixPath('.'):
        parent_node = _lookup_registry(parent)
        if isinstance(parent_node, Mapping):
            base = _ensure_materialized(parent, parent_node)
            candidate = base / path.name
            if not candidate.exists():
                candidate.parent.mkdir(parents=True, exist_ok=True)
                candidate.write_bytes(_resolve_bytes(node))
            _CACHE[path] = candidate
            return candidate

    temp_root = Path(_STACK.enter_context(tempfile.TemporaryDirectory(prefix="visbrain_data_")))
    target = temp_root.joinpath(*path.parts) if path.parts else temp_root
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(_resolve_bytes(node))
    _CACHE[path] = target
    return target


def _ensure_materialized(path: PurePosixPath, node: ResourceNode) -> Path:
    if path in _CACHE:
        return _CACHE[path]

    for ancestor in path.parents:
        if ancestor in _CACHE and ancestor != PurePosixPath('.'):
            base = _CACHE[ancestor]
            rel = path.relative_to(ancestor)
            candidate = base.joinpath(*rel.parts)
            if candidate.exists():
                _CACHE[path] = candidate
                return candidate

    return _materialize(path, node)


_def_parts = Union[str, Iterable[str]]


def bundled_path(*parts: _def_parts) -> Path:
    """Return the filesystem path to a bundled data resource.

    Parameters
    ----------
    parts:
        Path components inside the :mod:`visbrain.data` package.

    Returns
    -------
    pathlib.Path
        Path to a real file on disk, extracted from the package if needed.
    """

    flattened = tuple(_flatten(parts))
    if not flattened:
        raise ValueError("At least one path component is required")

    traversable: Traversable = resources.files(_DATA_PACKAGE)
    for piece in flattened:
        traversable = traversable.joinpath(piece)
    if traversable.exists():
        return _as_file(traversable)

    rel_path = PurePosixPath(*flattened)
    node = _lookup_registry(rel_path)
    if node is None:
        joined = "/".join(flattened)
        raise FileNotFoundError(f"Bundled data file not found: {joined}")
    return _ensure_materialized(rel_path, node)


def _iter_registry_files(tree: Mapping[str, ResourceNode], prefix: PurePosixPath) -> Iterator[PurePosixPath]:
    for name, value in tree.items():
        rel = prefix / name
        if isinstance(value, Mapping):
            yield from _iter_registry_files(value, rel)
        else:
            yield rel


def iter_bundled_files() -> Iterator[Path]:
    """Yield filesystem paths for all bundled resources."""

    root = resources.files(_DATA_PACKAGE)
    for traversable in root.rglob('*'):
        if traversable.is_file():
            yield _as_file(traversable)
    for rel_path in _iter_registry_files(PACKAGE_REGISTRY, PurePosixPath()):
        node = _lookup_registry(rel_path)
        if node is None:  # pragma: no cover - defensive, registry is static
            continue
        yield _ensure_materialized(rel_path, node)
