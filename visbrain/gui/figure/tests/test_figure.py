"""Test command lines."""

import numpy as np
from PIL import Image

from visbrain.gui import Figure
from visbrain.tests._tests_visbrain import _TestVisbrain

# List of image files to test with :
_FILES = ['default.png', 'inside.png', 'count.png', 'density.png',
          'repartition.jpg', 'roi.jpg']

class TestFigure(_TestVisbrain):
    """Test figure.py."""

    ###########################################################################
    #                                 FIGURE
    ###########################################################################
    def test_figure(self):
        """Test function figure."""
        # Get files :
        files = []
        gradients = np.linspace(0, 255, num=16, dtype=np.uint8)
        for idx, name in enumerate(_FILES):
            img_path = self.to_tmp_dir(name)
            grid = np.outer(gradients, np.ones_like(gradients, dtype=np.uint8))
            rgb = np.stack([
                np.roll(grid, idx, axis=0),
                np.roll(grid, idx, axis=1),
                np.flipud(grid),
            ], axis=-1)
            Image.fromarray(rgb).save(img_path)
            files.append(img_path)

        # Titles :
        titles = ['Default', 'Sources inside', 'Connectivity',
                  'Connectivity', 'Repartition', 'Projection']

        # X-labels / Y-labels :
        xlabels = [None, None, 'Nice', 'Looks good', 'Repartition', 'ROI']
        ylabels = ['Dirty', 'Better', None, None, None, 'BA 4 and 6']

        # Background color of each axis :
        ax_bgcolor = ['slateblue', 'olive', 'black', 'darkgray', None, None]

        f = Figure(files, titles=titles, xlabels=xlabels, ylabels=ylabels,
                   figtitle='Brain module', grid=(3, 2), ax_bgcolor=ax_bgcolor,
                   y=1., fig_bgcolor='white', figsize=(12, 12),
                   text_color='black', subspace={'wspace': 0.1, 'left': 0.})
        # Colorbar to the first connectivity plot :
        f.colorbar_to_axis(2, (1, 5), 'viridis', title='Color by count',
                           ticks='minmax', fz_ticks=12)
        # Colorbar to the second connectivity plot :
        f.colorbar_to_axis(3, (0., 35.), 'magma', title='Color by density',
                           ticks='complete', vmax=30, over='darkred',
                           fz_ticks=12, vmin=10., under='gray')
        # Colorbar to the first projection plot :
        f.colorbar_to_axis(4, (1, 6), 'viridis', title='Contributing sources',
                           ticks=1., fz_ticks=10, orientation='horizontal',
                           vmin=2, under='gray', vmax=4, over='#ab4642')
        # Colorbar to the second projection plot :
        f.colorbar_to_axis(5, (.1, .5), 'inferno', title='ROI projection',
                           ticks=[.2, .3], fz_ticks=10,
                           orientation='horizontal')
        # Add a vertical shared colormap :
        f.shared_colorbar((-10, 10), 'inferno', fz_title=30, vmin=-7, vmax=6,
                          under='olive', over='firebrick', position='right',
                          title='Shared vertical colorbar', fz_ticks=20,
                          pltmargin=.1, figmargin=.1)
        # Add a horizontal shared colormap :
        f.shared_colorbar(cmap='magma', clim=(-17, 17), fz_title=25, vmin=-11,
                          vmax=12, under='olive', over='firebrick',
                          position='bottom', title='Shared horizontal',
                          fz_ticks=15, pltmargin=.1)

        # Save the picture :
        f.save(self.to_tmp_dir('figure.png'), dpi=100)

    def test_layout_persistence(self):
        """Ensure layout configurations can be saved and restored."""

        files = []
        gradients = np.linspace(0, 255, num=8, dtype=np.uint8)
        for idx in range(4):
            img_path = self.to_tmp_dir(f'layout_{idx}.png')
            grid = np.outer(gradients, np.ones_like(gradients, dtype=np.uint8))
            rgb = np.stack([
                np.roll(grid, idx, axis=0),
                np.roll(grid, idx, axis=1),
                np.flipud(grid),
            ], axis=-1)
            Image.fromarray(rgb).save(img_path)
            files.append(img_path)

        layout_path = self.to_tmp_dir('layout.json')
        subspace = {'left': 0.1, 'right': 0.95, 'bottom': 0.15, 'top': 0.85,
                    'wspace': 0.2, 'hspace': 0.25}
        figure = Figure(
            files,
            grid=(2, 2),
            figtitle='Persistence',
            figsize=(6.0, 4.0),
            subspace=subspace,
            y=1.1,
            rmax=False,
            autocrop=True,
            autoresize={'axis': 0},
        )
        saved_path = figure.save_layout(layout_path)
        assert saved_path.is_file()

        loaded = Figure.load_layout(saved_path)
        assert loaded['grid'] == (2, 2)
        assert loaded['figtitle'] == 'Persistence'
        assert loaded['subspace']['left'] == subspace['left']
        assert loaded['autocrop'] is True
        assert loaded['autoresize'] == {'axis': 0}

        restored = Figure.from_layout(files, saved_path, figtitle='Restored')
        assert restored._grid == (2, 2)
        assert restored._figtitle == 'Restored'
        assert restored._subspace['left'] == subspace['left']
        assert restored._autocrop is True
