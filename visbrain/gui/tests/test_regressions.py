"""Screenshot regression tests for the Qt-based GUI modules."""
from __future__ import annotations

import pytest

from visbrain.gui.tests._screenshot import (
    GuiSpec,
    SCREENSHOT_SPECS,
    UPDATE_BASELINES,
    load_png,
    max_pixel_delta,
    render_spec,
    save_png,
)


@pytest.mark.screenshot
@pytest.mark.parametrize("spec", SCREENSHOT_SPECS, ids=lambda spec: spec.name)
def test_gui_screenshots(spec: "GuiSpec") -> None:
    image = render_spec(spec)
    baseline_path = spec.baseline_path

    if UPDATE_BASELINES:
        save_png(baseline_path, image)
        pytest.skip(f"Updated screenshot baseline for {spec.name}.")

    if not baseline_path.exists():
        message = (
            f"Missing baseline screenshot for {spec.name!r} at {baseline_path}. "
            "Run the test suite with VISBRAIN_UPDATE_SCREENSHOTS=1 to record baselines."
        )
        pytest.fail(message)

    reference = load_png(baseline_path)
    delta = max_pixel_delta(reference, image)
    assert delta <= spec.tolerance, (
        f"Screenshot for {spec.name!r} diverged (max pixel delta {delta}, "
        f"allowed {spec.tolerance})."
    )
