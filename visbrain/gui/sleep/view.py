"""View layer for the Sleep GUI module."""

from __future__ import annotations

import vispy.scene.cameras as viscam

from visbrain.utils import FixedCam

from .interface import UiInit


class SleepView(UiInit):
    """Encapsulate construction of the Qt widgets for the Sleep GUI."""

    def __init__(self) -> None:
        super().__init__()
        self._allCams = ()

    # ------------------------------------------------------------------
    # UI helpers
    # ------------------------------------------------------------------
    def set_default_state(self) -> None:
        """Reset stacked widgets to their default page."""
        self._DetectionTab.setCurrentIndex(0)
        self._stacked_panels.setCurrentIndex(0)
        self._stacked_tools.setCurrentIndex(0)
        self._stacked_detections.setCurrentIndex(0)

    def create_cameras(self, n_channels: int) -> None:
        """Create and attach cameras to the different canvases."""
        chan_cams = [FixedCam() for _ in range(n_channels)]
        for canvas, camera in zip(self._chanCanvas, chan_cams):
            canvas.set_camera(camera)

        self._speccam = FixedCam()
        self._specCanvas.set_camera(self._speccam)

        self._hypcam = FixedCam()
        self._hypCanvas.set_camera(self._hypcam)

        self._topocam = viscam.PanZoomCamera()
        self._topoCanvas.set_camera(self._topocam)

        self._timecam = FixedCam()
        self._TimeAxis.set_camera(self._timecam)

        self._chanCam = chan_cams
        self._allCams = (
            self._chanCam,
            self._speccam,
            self._hypcam,
            self._topocam,
            self._timecam,
        )

    @property
    def all_cameras(self):
        """Return the tuple of cameras for controller usage."""
        return self._allCams
