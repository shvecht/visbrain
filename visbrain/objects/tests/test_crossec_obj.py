"""Test CrossSecObj."""
import numpy as np
import pytest

from visbrain.objects import CrossSecObj
from visbrain.objects.tests._testing_objects import _TestObjects
from visbrain.io import clean_tmp


cs_obj = CrossSecObj('brodmann')


class TestCrossSecObj(_TestObjects):
    """Test CrossSecObj."""

    OBJ = cs_obj

    def test_definition(self):
        """Test class definition."""
        for k in ['brodmann', 'aal', 'talairach']:
            CrossSecObj(k)
        CrossSecObj('test', vol=np.random.rand(100, 100, 100))

    def test_cut_coords(self):
        """Test method cut_coords."""
        cs_obj.cut_coords((14, 15, 50))

    def test_localize_source(self):
        """Test function localize_source."""
        cs_obj.localize_source((15., 12., 23.))

    def test_nii_definition(self):
        """Test function nii_definition."""
        nib = pytest.importorskip('nibabel')
        img = nib.Nifti1Image(np.random.rand(4, 4, 4), np.eye(4))
        path = self.to_tmp_dir('synthetic_cross.nii.gz')
        nib.save(img, path)
        CrossSecObj(path)

    def test_set_activation(self):
        """Test function set_activation."""
        nib = pytest.importorskip('nibabel')
        img = nib.Nifti1Image(np.random.rand(4, 4, 4), np.eye(4))
        path = self.to_tmp_dir('synthetic_activation.nii.gz')
        nib.save(img, path)
        cs_obj.set_activation(path)

    def test_highlight_sources(self):
        """Test function highlight_sources."""
        cs_obj.highlight_sources(np.random.uniform(-20, 20, (100, 3)))

    def test_save(self):
        """Test function save."""
        nib = pytest.importorskip('nibabel')
        img = nib.Nifti1Image(np.random.rand(4, 4, 4), np.eye(4))
        path = self.to_tmp_dir('synthetic_cross_save.nii.gz')
        nib.save(img, path)
        v_obj = CrossSecObj(path)
        v_obj.save()
        v_obj.save(tmpfile=True)

    def test_remove(self):
        """Test function remove."""
        nib = pytest.importorskip('nibabel')
        img = nib.Nifti1Image(np.random.rand(4, 4, 4), np.eye(4))
        path = self.to_tmp_dir('synthetic_cross_remove.nii.gz')
        nib.save(img, path)
        v_obj = CrossSecObj(path)
        v_obj.save()
        v_obj.remove()
        clean_tmp()
