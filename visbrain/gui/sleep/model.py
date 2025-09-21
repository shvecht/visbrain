"""Data model for the :mod:`visbrain.gui.sleep` package."""

from __future__ import annotations

import logging
from typing import Any, Callable, Dict, Iterable, Mapping, MutableMapping, Optional

import numpy as np

from visbrain.io.read_sleep import ReadSleepData

logger = logging.getLogger("visbrain")

DetectionMethod = Callable[[np.ndarray, float, np.ndarray, np.ndarray], Any]


class SleepDataset(ReadSleepData):
    """Container holding polysomnographic data and related metadata.

    Parameters are identical to :class:`visbrain.io.ReadSleepData`.  The class
    exposes lightweight accessors so the GUI layer can interact with the data
    without owning the raw arrays directly.
    """

    _VALID_DETECTIONS = ("spindle", "sw", "kc", "rem", "mt", "peak")

    def __init__(
        self,
        data: Any,
        channels: Optional[Iterable[str]],
        sf: Optional[float],
        hypno: Optional[np.ndarray],
        href: Optional[Iterable[str]],
        preload: bool,
        use_mne: bool,
        downsample: Optional[float],
        kwargs_mne: Mapping[str, Any],
        annotations: Any,
    ) -> None:
        super().__init__(
            data,
            channels,
            sf,
            hypno,
            href,
            preload,
            use_mne,
            downsample,
            kwargs_mne,
            annotations,
        )
        self._custom_detections: Dict[str, DetectionMethod] = {}
        self._datainfo: Dict[str, np.ndarray] = {}
        self.refresh_data_info()

    # ------------------------------------------------------------------
    # Basic information
    # ------------------------------------------------------------------
    def __len__(self) -> int:
        """Return the number of channels in the dataset."""

        return len(self._channels)

    def __getitem__(self, key: str) -> np.ndarray:
        """Return cached data statistics."""

        return self._datainfo[key]

    # ------------------------------------------------------------------
    # Properties forwarding the ``ReadSleepData`` attributes.
    # ------------------------------------------------------------------
    @property
    def data(self) -> np.ndarray:
        return self._data

    @data.setter
    def data(self, value: np.ndarray) -> None:
        self._data = value
        self.refresh_data_info()

    @property
    def hypno(self) -> np.ndarray:
        return self._hypno

    @hypno.setter
    def hypno(self, value: np.ndarray) -> None:
        self._hypno = value

    @property
    def time(self) -> np.ndarray:
        return self._time

    @time.setter
    def time(self, value: np.ndarray) -> None:
        self._time = value

    @property
    def channels(self) -> Iterable[str]:
        return self._channels

    @channels.setter
    def channels(self, value: Iterable[str]) -> None:
        self._channels = list(value)

    @property
    def href(self) -> Iterable[str]:
        return self._href

    @href.setter
    def href(self, value: Iterable[str]) -> None:
        self._href = list(value)

    @property
    def hconv(self) -> MutableMapping[int, int]:
        return self._hconv

    @hconv.setter
    def hconv(self, value: Mapping[int, int]) -> None:
        self._hconv = dict(value)

    @property
    def hconvinv(self) -> Dict[int, int]:
        return {v: k for k, v in self._hconv.items()}

    @property
    def sf(self) -> float:
        return self._sf

    @sf.setter
    def sf(self, value: float) -> None:
        self._sf = float(value)

    @property
    def sfori(self) -> float:
        return self._sfori

    @sfori.setter
    def sfori(self, value: float) -> None:
        self._sfori = float(value)

    @property
    def dsf(self) -> int:
        return self._dsf

    @dsf.setter
    def dsf(self, value: int) -> None:
        self._dsf = int(value)

    @property
    def n_points(self) -> int:
        return self._N

    @n_points.setter
    def n_points(self, value: int) -> None:
        self._N = int(value)

    @property
    def file(self) -> Optional[str]:
        return self._file

    @file.setter
    def file(self, value: Optional[str]) -> None:
        self._file = value

    @property
    def annotations(self) -> np.ndarray:
        return self._annot_file

    @annotations.setter
    def annotations(self, value: np.ndarray) -> None:
        self._annot_file = value

    @property
    def datainfo(self) -> Dict[str, np.ndarray]:
        return self._datainfo

    @datainfo.setter
    def datainfo(self, value: Dict[str, np.ndarray]) -> None:
        self._datainfo = value

    @property
    def custom_detections(self) -> Dict[str, DetectionMethod]:
        return self._custom_detections

    # ------------------------------------------------------------------
    # Derived helpers
    # ------------------------------------------------------------------
    def refresh_data_info(self) -> Dict[str, np.ndarray]:
        """Compute summary statistics for the loaded data."""

        data = self._data
        self._datainfo = {
            "min": data.min(1),
            "max": data.max(1),
            "std": data.std(1),
            "mean": data.mean(1),
            "dist": data.max(1) - data.min(1),
        }
        return self._datainfo

    # ------------------------------------------------------------------
    # Detection overrides
    # ------------------------------------------------------------------
    def replace_detection(self, dtype: str, method: DetectionMethod) -> None:
        """Register a user-provided detection algorithm."""

        if dtype not in self._VALID_DETECTIONS:
            raise ValueError(
                "dtype should be a string. Choose between %s"
                % ", ".join(self._VALID_DETECTIONS)
            )
        if not callable(method):
            raise AssertionError("method must be callable")
        self._custom_detections[dtype] = method
        logger.info("Method for %s detection has been successfully replaced", dtype)

    def get_detection(self, dtype: str) -> Optional[DetectionMethod]:
        """Return a custom detection if defined."""

        return self._custom_detections.get(dtype)

    def has_custom_detection(self, dtype: str) -> bool:
        """Check whether a custom detection exists for *dtype*."""

        return dtype in self._custom_detections


__all__ = ["SleepDataset"]
