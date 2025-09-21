"""Unit tests targeting the Sleep controller using synthetic fixtures."""

from __future__ import annotations

import numpy as np
import pytest

try:  # pragma: no cover - optional Qt bindings
    from visbrain.qt import QtWidgets
except ImportError:  # pragma: no cover - Qt not installed
    QtWidgets = None


pytestmark = [
    pytest.mark.skipif(QtWidgets is None, reason="Qt bindings are unavailable"),
]


def test_slider_signals_trigger_slots(sleep_controller, qtbot, monkeypatch):
    """Changing the slider emits the connected slot without manual calls."""

    called = []
    original = sleep_controller._fcn_slider_settings

    def tracker():
        called.append(True)
        return original()

    monkeypatch.setattr(sleep_controller, "_fcn_slider_settings", tracker)
    sleep_controller._SigSlStep.setValue(
        sleep_controller._SigSlStep.value() + 1
    )
    qtbot.waitUntil(lambda: called, timeout=1000)


def test_detection_workflow_and_persistence(sleep_controller, tmp_path):
    """Custom detections populate the table and can be saved/loaded."""

    def fake_detection(data, sf, time, hypno):
        return np.array([[10, 15], [20, 25]])

    sleep_controller.replace_detections("spindle", fake_detection)
    index = sleep_controller._ToolDetectType.findText("Spindles")
    sleep_controller._ToolDetectType.setCurrentIndex(index)
    sleep_controller._ToolDetectChan.setCurrentIndex(0)
    sleep_controller._ToolRdSelected.setChecked(True)
    sleep_controller._ToolDetectApply.click()
    assert sleep_controller._DetectLocations.rowCount() == 2

    file_all = tmp_path / "detections.npy"
    sleep_controller._save_all_detect(filename=str(file_all))
    assert file_all.exists()
    sleep_controller._load_detect_all(filename=str(file_all))

    sleep_controller._DetectLocations.selectRow(0)
    file_select = tmp_path / "selected_detect_Cz-Spindles.csv"
    sleep_controller._save_select_detect(filename=str(file_select))
    assert file_select.exists()
    sleep_controller._load_detect_select(filename=str(file_select))


def test_annotation_signals_update_table(sleep_controller, qtbot, monkeypatch):
    """Annotation buttons drive their slots via Qt signals."""

    called = []
    original = sleep_controller._fcn_annotate_add

    def tracker(*args, **kwargs):
        called.append(True)
        return original(*args, **kwargs)

    monkeypatch.setattr(sleep_controller, "_fcn_annotate_add", tracker)
    sleep_controller._AnnotateAdd.click()
    qtbot.waitUntil(lambda: called, timeout=1000)
    assert sleep_controller._AnnotateTable.rowCount() == 1

    sleep_controller._AnnotateRm.click()
    assert sleep_controller._AnnotateTable.rowCount() == 0


def test_save_and_load_helpers(sleep_controller, tmp_path):
    """Saving hypnograms and annotations works with synthetic data."""

    yes = QtWidgets.QMessageBox.Yes
    hyp_path = tmp_path / "hyp_data.txt"
    sleep_controller.saveHypData(filename=str(hyp_path), reply=yes)
    assert hyp_path.exists()

    anno_path = tmp_path / "annotations.csv"
    sleep_controller._save_annotation_table(filename=str(anno_path))
    assert anno_path.exists()

    numpy_annotations = np.array([5.0, 10.0, 15.0])
    sleep_controller._load_annotation_table(filename=numpy_annotations)
    assert sleep_controller._AnnotateTable.rowCount() == numpy_annotations.size
