"""Test function in read_data.py."""

import os

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

    # @pytest.mark.slow
    # def test_read_nifti(self):
    #     """Test function read_nifti."""
    #     read_nifti(download_file("GG-853-GM-0.7mm.nii.gz",
    #                              astype='example_data'))
