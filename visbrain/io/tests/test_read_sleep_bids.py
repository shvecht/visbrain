import datetime
import os
import sys
import types

import numpy as np
import pytest

from visbrain.io.mneio import build_sleep_payload
from visbrain.io.read_sleep import (
    _discover_bids_files,
    _match_bids_candidate,
    _load_bids_directory,
    sleep_switch,
)


@pytest.fixture(autouse=True)
def _fake_mne_bids(monkeypatch):
    """Provide a lightweight stub of :mod:`mne_bids` for tests."""

    class FakeBIDSPath:
        def __init__(self, check=False, **entities):
            self.entities = dict(entities)

        def copy(self):
            return FakeBIDSPath(**self.entities)

        def update(self, **updates):
            data = dict(self.entities)
            data.update(updates)
            return FakeBIDSPath(**data)

        def __str__(self):
            root = self.entities.get('root', '')
            parts = [
                f"{key}-{value}"
                for key, value in sorted(self.entities.items())
                if key != 'root'
            ]
            basename = '_'.join(parts)
            return os.path.join(root, basename)

    class FakeRaw:
        def __init__(self):
            self._data = np.arange(20.0).reshape(2, 10)
            self.info = {'sfreq': 100.0, 'ch_names': ['C3', 'C4'], 'bads': []}
            self.annotations = None
            self._raw_extras = ()

        def pick_types(self, **kwargs):
            return self

        def get_data(self, picks=None):
            return self._data

    def read_raw_bids(bids_path, extra_params=None, verbose=None):
        return FakeRaw()

    module = types.SimpleNamespace(BIDSPath=FakeBIDSPath, read_raw_bids=read_raw_bids)
    monkeypatch.setitem(sys.modules, 'mne_bids', module)
    monkeypatch.setattr(
        'visbrain.io.read_sleep.is_mne_bids_installed',
        lambda raise_error=False: True,
    )
    return module


@pytest.fixture
def bids_root(tmp_path):
    root = tmp_path / 'bids'
    eeg_dir = root / 'sub-01' / 'eeg'
    eeg_dir.mkdir(parents=True)
    (eeg_dir / 'sub-01_task-rest_run-01_eeg.edf').write_bytes(b'')
    (eeg_dir / 'sub-01_task-rest_run-02_eeg.edf').write_bytes(b'')
    return root


def test_match_bids_candidate_resolve_last(bids_root):
    candidates = _discover_bids_files(str(bids_root))
    _, summary = _match_bids_candidate(candidates, {}, str(bids_root), resolve='last')
    assert summary['selected'].endswith('run-02_eeg.edf')
    assert summary['strategy'] == 'last'


def test_match_bids_candidate_reports_available(bids_root):
    candidates = _discover_bids_files(str(bids_root))
    with pytest.raises(FileNotFoundError) as err:
        _match_bids_candidate(candidates, {'run': '99'}, str(bids_root))
    message = str(err.value)
    assert 'run-01' in message
    assert 'run-02' in message


def test_load_bids_directory_metadata(bids_root):
    payload = _load_bids_directory(
        str(bids_root),
        downsample=50.0,
        kwargs_mne={'bids_entities': {'run': '01'}, 'bids_resolve': 'first'},
    )
    metadata = payload['metadata']
    assert metadata['bids']['selected'].endswith('run-01_eeg.edf')
    assert metadata['bids']['strategy'] in {'first', 'unique-match'}
    assert metadata['source'].endswith('.edf')


def test_sleep_switch_bids_fallback(monkeypatch, bids_root):
    def failing_loader(*args, **kwargs):  # pragma: no cover - invoked in test
        raise RuntimeError('forced failure')

    monkeypatch.setattr(
        'visbrain.io.read_sleep._load_bids_directory',
        failing_loader,
    )

    def fake_mne_switch(file, ext, downsample, **kwargs):
        data = np.ones((1, 8))
        return build_sleep_payload(
            100.0,
            100.0,
            1,
            data,
            ['Cz'],
            data.shape[1],
            datetime.time(0, 0, 0),
            None,
            metadata={'source': os.path.abspath(file + ext)},
        )

    monkeypatch.setattr(
        'visbrain.io.read_sleep.mne_switch',
        fake_mne_switch,
    )

    payload = sleep_switch(
        str(bids_root),
        '',
        100.0,
        kwargs_mne={'bids_entities': {'run': '01'}},
    )
    metadata = payload['metadata']
    assert 'fallback' in metadata
    assert metadata['fallback']['selected'].endswith('run-01_eeg.edf')
    assert metadata['fallback']['reason'] == 'forced failure'
