"""Embedded binary assets for visbrain packaged resources."""
from __future__ import annotations

from io import BytesIO
from typing import Dict, Union, Callable

import numpy as np

__all__ = ["PACKAGE_REGISTRY"]


def _npz_bytes(**arrays: np.ndarray) -> bytes:
    """Serialize arrays into an in-memory ``.npz`` archive."""
    buffer = BytesIO()
    np.savez(buffer, **arrays)
    return buffer.getvalue()


def _npy_bytes(array: np.ndarray) -> bytes:
    """Serialize an array into an in-memory ``.npy`` file."""
    buffer = BytesIO()
    np.save(buffer, array)
    return buffer.getvalue()


_LABEL_DTYPE = np.dtype([("label", object), ("name", object)])


def _cube_template_bytes() -> bytes:
    vertices = np.array(
        [
            (-1.0, -1.0, -1.0),
            (1.0, -1.0, -1.0),
            (-1.0, 1.0, -1.0),
            (1.0, 1.0, -1.0),
            (-1.0, -1.0, 1.0),
            (1.0, -1.0, 1.0),
            (-1.0, 1.0, 1.0),
            (1.0, 1.0, 1.0),
        ],
        dtype=np.float32,
    )
    faces = np.array(
        [
            (0, 1, 2),
            (1, 3, 2),
            (4, 5, 6),
            (5, 7, 6),
            (0, 1, 4),
            (1, 5, 4),
            (2, 3, 6),
            (3, 7, 6),
            (0, 2, 4),
            (2, 6, 4),
            (1, 3, 5),
            (3, 7, 5),
        ],
        dtype=np.int32,
    )
    normals = np.zeros((8, 3), dtype=np.float32)
    lr_index = np.array([4], dtype=np.int32)
    return _npz_bytes(
        vertices=vertices,
        faces=faces,
        normals=normals,
        lr_index=lr_index,
    )


def _roi_bytes() -> bytes:
    vol = np.zeros((3, 3, 3), dtype=np.int16)
    vol[0, 0, 0] = 1
    vol[1, 1, 1] = 2
    vol[2, 2, 2] = 3
    hdr = np.eye(4, dtype=np.float32)
    labels = np.array(
        [
            ("R1", "Region 1"),
            ("R2", "Region 2"),
            ("R3", "Region 3"),
        ],
        dtype=_LABEL_DTYPE,
    )
    index = np.array([1, 2, 3], dtype=np.int16)
    return _npz_bytes(vol=vol, hdr=hdr, labels=labels, index=index)


def _eegref_bytes() -> bytes:
    chan = np.array(["fz", "cz", "pz"], dtype=object)
    xyz = np.array(
        [
            (0.0, 90.0, 1.0),
            (0.0, 0.0, 1.0),
            (0.0, -90.0, 1.0),
        ],
        dtype=np.float32,
    )
    return _npz_bytes(chan=chan, xyz=xyz)


def _px_bytes() -> bytes:
    return _npy_bytes(np.arange(10, dtype=np.float32))


ResourceNode = Union[bytes, Callable[[], bytes], "ResourceTree"]
ResourceTree = Dict[str, ResourceNode]


PACKAGE_REGISTRY: ResourceTree = {
    "templates": {
        "B1.npz": _cube_template_bytes,
        "B2.npz": _cube_template_bytes,
        "B3.npz": _cube_template_bytes,
    },
    "roi": {
        "aal.npz": _roi_bytes,
        "brodmann.npz": _roi_bytes,
        "talairach.npz": _roi_bytes,
    },
    "topo": {
        "eegref.npz": _eegref_bytes,
    },
    "example_data": {
        "Px.npy": _px_bytes,
    },
}
