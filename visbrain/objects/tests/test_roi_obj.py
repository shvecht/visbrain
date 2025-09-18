"""Test RoiObj."""
import numpy as np

from visbrain.objects.tests._testing_objects import _TestVolumeObject
from visbrain.objects import SourceObj, RoiObj
from visbrain.io import path_to_visbrain_data, clean_tmp


roi_obj = RoiObj('brodmann')
roi_obj.select_roi([4, 6])
rnd = np.random.RandomState(0)
xyz = 100. * rnd.rand(50, 3)
xyz[:, 0] -= 50.
xyz[:, 1] -= 50.
s_obj = SourceObj('S1', xyz)

arch = np.load(path_to_visbrain_data('brodmann.npz', 'roi'))
vol = arch['vol']
hdr = arch['hdr']
roi_index = arch['index']
label = arch['labels']
n_roi = len(roi_index)


class TestRoiObj(_TestVolumeObject):
    """Test BrainObj."""

    OBJ = roi_obj

    def test_definition(self):
        """Test function definition."""
        # Default :
        _ = [RoiObj(k) for k in ['aal', 'talairach', 'brodmann']]  # noqa
        # MIST datasets now require an explicit fetch step
        import pytest

        levels = [7, 12, 20, 36, 64, 122, 'ROI']
        for level in levels:
            with pytest.raises(FileNotFoundError):
                RoiObj(f'mist_{level}')

    def test_get_labels(self):
        """Test function get_labels."""
        import pandas as pd
        labels = roi_obj.get_labels()
        assert isinstance(labels, pd.DataFrame)
        roi_obj.get_labels(self.to_tmp_dir())

    def test_where_is(self):
        """Test function where_is."""
        r = RoiObj('aal')
        r.where_is('Thalamus')
        r.where_is(['Thalamus', '(L)'], union=False)

    def test_localize_sources(self):
        """Test function localize_sources."""
        roi_obj.localize_sources(s_obj.xyz, source_name=s_obj.text)
        roi_obj.localize_sources(s_obj.xyz, distance=1000.)

    def test_get_centroids(self):
        """Test function get_centroids."""
        roi_obj.get_centroids([2, 4, 6])

    def test_project_sources(self):
        """Test function project_sources."""
        roi_obj.project_sources(s_obj, 'modulation')
        roi_obj.project_sources(s_obj, 'repartition')

    def test_properties(self):
        """Test function properties."""
        self.assert_and_test('translucent', True)
        self.assert_and_test('alpha', .03)
        assert isinstance(roi_obj.vertices, np.ndarray)
        assert isinstance(roi_obj.faces, np.ndarray)
        assert isinstance(roi_obj.normals, np.ndarray)
        assert isinstance(roi_obj.mask_color, np.ndarray)

    def test_select_roi(self):
        """Test function select_roi."""
        roi_obj.select_roi([1])
        roi_obj.select_roi(40.)
        roi_obj.select_roi([1, 2], unique_color=True)
        roi_obj.select_roi([1, 2], roi_to_color={1: 'red', 2: (1., 0., 0.)})

    def test_save_and_remove(self):
        """Test methods save, reload and remove."""
        # Define the ROI object and save it :
        roi_custom = RoiObj('mist_roi', vol=vol, labels=label, index=roi_index,
                            hdr=hdr)
        roi_custom.save()
        # Test reloading roi from name only :
        roi_sec = RoiObj('mist_roi')
        roi_sec.remove()

    def test_save_and_remove_tmp(self):
        """Test methods save, reload and remove for tmp files."""
        # Define the ROI object and save it :
        roi_custom = RoiObj('tmp_roi', vol=vol, labels=label, index=roi_index,
                            hdr=hdr)
        roi_custom.save(tmpfile=True)
        # Test reloading roi from name only :
        RoiObj('tmp_roi')
        clean_tmp()
