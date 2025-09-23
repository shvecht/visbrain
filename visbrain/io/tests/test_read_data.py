"""Test function in read_data.py."""

import csv
import json
import os
import pickle

import numpy as np
import pytest

from visbrain.io import path_to_visbrain_data
from visbrain.io.read_data import (read_mat, read_pickle, read_npy, read_npz,  # noqa
                                   read_txt, read_csv, read_json,
                                   read_stc, read_x3d, read_gii, read_obj)


class TestReadData(object):
    """Test functions in read_data.py."""

    @staticmethod
    def _test_mesh(vertices, faces):
        assert (vertices.ndim == 2) and (faces.ndim == 2)
        assert vertices.shape[1] == faces.shape[1] == 3
        assert faces.max() < vertices.shape[0]

    def test_read_stc(self):
        """Test function read_stc."""
        path = path_to_visbrain_data("meg_source_estimate-lh.stc",
                                     'example_data')
        if not os.path.isfile(path):
            pytest.skip(
                "STC example not installed. Run `python -m visbrain.io.download "
                "meg_source_estimate-lh.stc --type example_data` to fetch it."
            )
        read_stc(path)

    def test_read_x3d(self):
        """Test function read_x3d."""
        file = path_to_visbrain_data('ferret.x3d', 'example_data')
        if not os.path.isfile(file):
            pytest.skip(
                "X3D examples not installed. Run `python -m visbrain.io.download "
                "ferret.x3d --type example_data` to fetch them."
            )
        vert, faces = read_x3d(file)
        self._test_mesh(vert, faces)

    def test_read_gii(self):
        """Test function read_gii."""
        file = path_to_visbrain_data('lh.bert.inflated.gii', 'example_data')
        if not os.path.isfile(file):
            pytest.skip(
                "GIfTI example not installed. Run `python -m visbrain.io.download "
                "lh.bert.inflated.gii --type example_data` to fetch it."
            )
        vert, faces = read_gii(file)
        self._test_mesh(vert, faces)

    def test_read_obj(self):
        """Test function read_obj."""
        file = path_to_visbrain_data('brain.obj', 'example_data')
        if not os.path.isfile(file):
            pytest.skip(
                "OBJ example not installed. Run `python -m visbrain.io.download "
                "brain.obj --type example_data` to fetch it."
            )
        vert, faces = read_obj(file)
        self._test_mesh(vert, faces)

    def test_read_pickle(self, tmp_path):
        """Pickle files should round-trip plain Python structures."""
        payload = {'alpha': 1, 'beta': [1, 2, 3]}
        file = tmp_path / 'data.pkl'
        with file.open('wb') as fid:
            pickle.dump(payload, fid)

        assert read_pickle(file) == payload
        assert read_pickle(file, vars='alpha') == payload['alpha']
        subset = read_pickle(file, vars=('alpha', 'beta'))
        assert subset == payload

    def test_read_npz(self, tmp_path):
        """NPZ files should expose the stored NumPy arrays."""
        file = tmp_path / 'arrays.npz'
        reference = {
            'a': np.arange(3),
            'b': np.eye(2),
        }
        np.savez(file, **reference)

        result = read_npz(file)
        assert set(result) == set(reference)
        np.testing.assert_array_equal(result['a'], reference['a'])
        np.testing.assert_array_equal(read_npz(file, 'b'), reference['b'])

    def test_read_txt(self, tmp_path):
        """Text files should be returned as raw strings."""
        file = tmp_path / 'notes.txt'
        content = 'line one\nline two\n'
        file.write_text(content, encoding='utf-8')

        assert read_txt(file) == content

    def test_read_csv(self, tmp_path):
        """CSV files are returned as row-major lists of strings."""
        file = tmp_path / 'data.csv'
        rows = [['name', 'value'], ['alpha', '1'], ['beta', '2']]
        with file.open('w', newline='', encoding='utf-8') as fid:
            writer = csv.writer(fid)
            writer.writerows(rows)

        assert read_csv(file) == rows

    def test_read_json(self, tmp_path):
        """JSON files should be deserialised to native Python objects."""
        file = tmp_path / 'data.json'
        payload = {'alpha': 1, 'beta': ['x', 'y']}
        file.write_text(json.dumps(payload), encoding='utf-8')

        assert read_json(file) == payload

    # @pytest.mark.slow
    # def test_read_nifti(self):
    #     """Test function read_nifti."""
    #     read_nifti(download_file("GG-853-GM-0.7mm.nii.gz",
    #                              astype='example_data'))
