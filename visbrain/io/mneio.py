"""Utility helpers bridging MNE readers with :mod:`visbrain` loaders."""

from __future__ import annotations

import datetime
import logging
import os
from typing import Any, Dict, Iterable, Mapping, Optional

import numpy as np

from ..utils import get_dsf

logger = logging.getLogger("visbrain")

__all__ = ["mne_switch", "finalize_raw", "build_sleep_payload"]


def build_sleep_payload(
    sf: float,
    downsample: Optional[float],
    dsf: int,
    data: np.ndarray,
    channels: Iterable[str],
    n: int,
    start_time: datetime.time,
    annotations: Any,
    *,
    metadata: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    """Bundle raw arrays and metadata into a normalized payload."""

    payload_metadata: Dict[str, Any] = {}
    if metadata:
        payload_metadata.update({str(key): value for key, value in metadata.items()})

    return {
        "sf": float(sf),
        "downsample": None if downsample is None else float(downsample),
        "dsf": int(dsf),
        "data": np.asarray(data),
        "channels": list(channels),
        "n": int(n),
        "start_time": start_time,
        "annotations": annotations,
        "metadata": payload_metadata,
    }


def mne_switch(file, ext, downsample, preload=True, **kwargs):
    """Read sleep datasets using mne.io.

    Parameters
    ----------
    file : string
        Filename (without extension).
    ext : string
        File extension (e.g. '.edf'').
    preload : bool | True
        Preload data in memory.
    kwargs : dict | {}
        Further arguments to pass to the mne.io.read function.

    Returns
    -------
    sf : float
        The original sampling-frequency.
    downsample : float
        The down-sampling frequency used.
    dsf : int
        The down-sampling factor.
    data : array_like
        The raw data of shape (n_channels, n_points)
    channels : list
        List of channel names.
    n : int
        Number of time points before down-sampling.
    start_time : datetime.time
        The time offset.
    """
    from mne import io

    # Get full path :
    path = file + ext
    abspath = os.path.abspath(path)

    # Preload :
    if preload is False:
        preload = 'temp.dat'
    kwargs['preload'] = preload

    if ext.lower() in ['.edf', '.bdf', '.gdf']:  # EDF / BDF / GDF
        raw = io.read_raw_edf(path, **kwargs)
    elif ext.lower == '.set':   # EEGLAB
        raw = io.read_raw_eeglab(path, **kwargs)
    elif ext.lower() in ['.egi', '.mff']:  # EGI / MFF
        raw = io.read_raw_egi(path, **kwargs)
    elif ext.lower() == '.cnt':  # CNT
        raw = io.read_raw_cnt(path, **kwargs)
    elif ext.lower() == '.vhdr':  # BrainVision
        raw = io.read_raw_brainvision(path, **kwargs)
    else:
        raise IOError("File not supported by mne-python.")

    return finalize_raw(raw, downsample, metadata={"source": abspath})


def _coerce_datetime(value: Any) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, datetime.datetime):
        return value.isoformat()
    if isinstance(value, datetime.date):
        combined = datetime.datetime.combine(value, datetime.time())
        return combined.isoformat()
    # mne may encode meas_date as (sec, usec)
    if isinstance(value, tuple) and len(value) == 2:
        try:
            timestamp = datetime.datetime.fromtimestamp(value[0])
            return timestamp.replace(microsecond=value[1]).isoformat()
        except Exception:  # pragma: no cover - defensive
            return str(value)
    return str(value)


def _normalize_mapping(mapping: Optional[Mapping[str, Any]]) -> Dict[str, Any]:
    normalized: Dict[str, Any] = {}
    if not mapping:
        return normalized
    for key, value in mapping.items():
        if isinstance(value, (str, int, float, bool)) or value is None:
            normalized[key] = value
        elif isinstance(value, datetime.datetime):
            normalized[key] = value.isoformat()
        elif isinstance(value, (list, tuple)):
            normalized[key] = tuple(value)
        elif isinstance(value, dict):
            normalized[key] = _normalize_mapping(value)
        else:
            normalized[key] = str(value)
    return normalized


def finalize_raw(raw, downsample, *, metadata: Optional[Mapping[str, Any]] = None):
    """Convert an :class:`mne.io.BaseRaw` instance to numpy arrays."""

    raw.pick_types(meg=True, eeg=True, ecg=True, emg=True)  # Remove stim lines
    sf = raw.info['sfreq']
    dsf, downsample = get_dsf(downsample, sf)
    channels = raw.info['ch_names']

    data = getattr(raw, '_data', None)
    if data is None:
        data = raw.get_data(picks=None)
    data = np.asarray(data)
    extras = getattr(raw, '_raw_extras', ())
    if extras and extras[0] is not None and 'units' in extras[0]:
        units = np.array(extras[0]['units'][0:data.shape[0]], dtype=float)
        # Ensure we do not mutate the Raw object scaling factors in-place.
        data = np.array(data, copy=True)
        data /= units.reshape(-1, 1)

    n = data.shape[1]
    start_time = datetime.time(0, 0, 0)
    anot = getattr(raw, 'annotations', None)

    raw_info = getattr(raw, "info", {})
    info_metadata: Dict[str, Any] = {}
    if isinstance(raw_info, Mapping):
        info_metadata = {
            "meas_date": _coerce_datetime(raw_info.get("meas_date")),
            "line_freq": raw_info.get("line_freq"),
            "subject_info": _normalize_mapping(raw_info.get("subject_info")),
            "description": raw_info.get("description"),
            "experimenter": raw_info.get("experimenter"),
            "project_name": raw_info.get("proj_name") or raw_info.get("project_name"),
            "device_info": _normalize_mapping(raw_info.get("device_info")),
            "bads": tuple(raw_info.get("bads", ())),
        }
        info_metadata = {k: v for k, v in info_metadata.items() if v not in (None, ())}

    combined_metadata: Dict[str, Any] = {
        "library": "mne",
        "loader": raw.__class__.__name__,
    }
    if info_metadata:
        combined_metadata["info"] = info_metadata
    if metadata:
        combined_metadata.update(dict(metadata))

    logger.debug(
        "Converted Raw object into payload with %d channels and %d samples",
        data.shape[0],
        n,
    )

    return build_sleep_payload(
        sf,
        downsample,
        dsf,
        data[:, ::dsf],
        channels,
        n,
        start_time,
        anot,
        metadata=combined_metadata,
    )
