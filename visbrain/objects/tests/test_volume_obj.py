"""Test VolumeObj."""
import numpy as np
import pytest

from visbrain.objects.tests._testing_objects import _TestVolumeObject
from visbrain.objects import VolumeObj
from visbrain.io import clean_tmp


v_obj = VolumeObj('aal')


class TestVolumeObj(_TestVolumeObject):
    """Test BrainObj."""

    OBJ = v_obj

    def test_definition(self):
        """Test function definition."""
        for k in ['aal', 'brodmann', 'talairach']:
            VolumeObj(k)
        VolumeObj('vol', vol=np.random.rand(10, 20, 30))

    def test_properties(self):
        """Test function properties."""
        for k in ['mip', 'translucent', 'additive', 'iso']:
            self.assert_and_test('method', k)
        for k in ['OpaqueGrays', 'TransFire', 'OpaqueFire', 'TransGrays']:
            self.assert_and_test('cmap', k)
        self.assert_and_test('threshlod', 5)

    def test_extract_activity(self):
        """Test function extract_activity."""
        xyz = np.random.uniform(-20, 20, (100, 3))
        v_obj.extract_activity(xyz, radius=10.)

    def test_nii_definition(self):
        """Test function nii_definition."""
        nib = pytest.importorskip('nibabel')
        img = nib.Nifti1Image(np.random.rand(4, 4, 4), np.eye(4))
        path = self.to_tmp_dir('synthetic.nii.gz')
        nib.save(img, path)
        VolumeObj(path)

    def test_save(self):
        """Test function save."""
        nib = pytest.importorskip('nibabel')
        img = nib.Nifti1Image(np.random.rand(4, 4, 4), np.eye(4))
        path = self.to_tmp_dir('synthetic_save.nii.gz')
        nib.save(img, path)
        v_obj = VolumeObj(path)
        v_obj.save()
        v_obj.save(tmpfile=True)

    def test_remove(self):
        """Test function remove."""
        nib = pytest.importorskip('nibabel')
        img = nib.Nifti1Image(np.random.rand(4, 4, 4), np.eye(4))
        path = self.to_tmp_dir('synthetic_remove.nii.gz')
        nib.save(img, path)
        v_obj = VolumeObj(path)
        v_obj.save()
        v_obj.remove()
        clean_tmp()
