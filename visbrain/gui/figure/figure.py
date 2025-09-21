"""Docstring."""

from __future__ import annotations

import json
import math
import os
import webbrowser
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Tuple

import numpy as np

from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
import matplotlib as mpl

from visbrain.utils import color2tuple, piccrop, picresize


__all__ = ['Figure', 'FigureGUI']


def _json_safe(value: Any) -> Any:
    """Convert *value* into a JSON serialisable structure."""

    if isinstance(value, np.generic):  # pragma: no cover - numpy scalar helper
        return value.item()
    if isinstance(value, dict):
        return {str(key): _json_safe(val) for key, val in value.items()}
    if isinstance(value, tuple):
        return [_json_safe(val) for val in value]
    if isinstance(value, list):
        return [_json_safe(val) for val in value]
    return value


def _write_layout_file(
    config: Dict[str, Any],
    layout_file: os.PathLike[str] | str,
) -> Path:
    """Persist a layout configuration to *layout_file*."""

    layout_path = Path(layout_file)
    layout_path.parent.mkdir(parents=True, exist_ok=True)
    layout_path.write_text(json.dumps(_json_safe(config), indent=2, sort_keys=True))
    return layout_path


def _read_layout_file(layout_file: os.PathLike[str] | str) -> Dict[str, Any]:
    """Load a layout configuration from *layout_file*."""

    layout_path = Path(layout_file)
    with layout_path.open('r', encoding='utf8') as fobj:
        return json.load(fobj)


def _normalize_layout_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Normalise a layout configuration loaded from disk."""

    normalised = dict(config)
    grid = normalised.get('grid')
    if isinstance(grid, Iterable):
        normalised['grid'] = tuple(int(v) for v in grid)
    figsize = normalised.get('figsize')
    if isinstance(figsize, Iterable) and figsize is not None:
        normalised['figsize'] = tuple(float(v) for v in figsize)
    subspace = normalised.get('subspace')
    if isinstance(subspace, dict):
        normalised['subspace'] = {
            str(key): float(value) for key, value in subspace.items()
        }
    return normalised


_DEFAULT_SUBSPACE: Dict[str, float] = {
    'left': 0.05,
    'right': 1.0,
    'bottom': 0.1,
    'top': 0.9,
    'wspace': 0.0,
    'hspace': 0.3,
}


class Figure(object):
    """Automatically arange pictures in a grid and save a paper ready figure.

    This class can be used to generate figures to be then used in a paper. For
    example, if you export 10 pictures, you may want to concatenate them in a
    (5, 2) grid and add a colorbar.

    Parameters
    ----------
    files : str/list/tuple
        Files to load. If it's a string, only one file will be loaded.
        Otherwise, if files is a iterable object of strings (list, tuple)
        all the files will be loaded.
    path : str | None
        Specify where files are located. If all files are in separate
        folders, use the files variable : files = ['path1/file1.png',
        'path2/file2.jpg', ...]. If all pictures are in the same folder,
        use path='path2myfolder/' and files=['file1.png', 'file2.jpg', ...]
    grid : tuple | None
        Tuple of integers describing how to arange figures. The grid
        describe (n_rows, n_columns) of the final figure. If grid is None
        all pictures will be displayed on a line. For example, if 12
        pictures are loaded, grid could be (6, 2), (4, 3)...
    figtitle : str | None
        Title of the entire figure.
    y : float | 1.02
        Distance between top and title of each axis (if title displayed).
    titles : str/list/tuple | None
        Specify the title of each figure. If titles is None, no title will
        be added. If titles is a string, the same title will be applied to
        all figures. If titles is a list/tuple of strings, the strings
        inside will be used to set the title of each picture independantly
        (must have the same length as files.)
    xlabels : str/list/tuple | None
        Specify the x-axis label of each figure. If xlabels is None,
        no label will be added. If xlabels is a string, the same label will
        be applied to all figures. If xlabels is a list/tuple of strings,
        the strings inside will be used to set the label of each picture
        independantly (must have the same length as files.)
    ylabels : str/list/tuple | None
        Specify the y-axis label of each figure. If ylabels is None,
        no label will be added. If ylabels is a string, the same label will
        be applied to all figures. If ylabels is a list/tuple of strings,
        the strings inside will be used to set the label of each picture
        independantly (must have the same length as files.)
    figsize : tuple | None
        The size of the figure. Should be a tuple of integers.
    subspace : dict | {}
        Control margins and the distance between subplots. By default :
        {'left': 0., 'right': 1., 'bottom': 0., 'top': .9, 'wspace': 0.,
        'hspace': 0.05}. Use:

            * 'left' (default 0.): left side of subplots
            * 'right' (default 1.): right side of subplots
            * 'bottom' (default 0.): bottom side of subplots
            * 'top' (default .9): top of subplots
            * 'hspace' (default .05): amount of height reserved for white space
              between subplots, expressed as a fraction of the average axis
              height.
            * 'wspace' (default 0.): amount of width reserved for blank space
              between subplots, expressed as a fraction of the average axis
              width.

    rmax : bool | True
        Remove borders of each axis.
    fig_bgcolor : str/tuple/list | None
        Background color of the figure. By default, no background is used.
    ax_bgcolor : str/tuple/list | None
        Background color of each axis. If None, no background will be used.
        If ax_bgcolor is a string, the same background will be used for all
        axes. Finally, use a list of colors to control the background color
        of each axis. This is a very important parameter for transparent
        pictures (like png or tiff files).
    text_color : str/tuple/list | 'black'
        Color of text elements (figure title, axes titles, x and y labels.)
    autocrop : bool | False
        Specify if each picture has to be automatically cropped.
    autoresize : bool | False
        Specify if all pictures have to be resized. If True, all pictures
        will be resized according to the minimum size along row axis. For
        further controls, define autoresize as a dictionary. Use the
        key 'axis' to specify if pictures have to share the same height (0)
        or width (1). Use 'extend' if the smallest (False) or the largest
        have to be considered as the reference.
    """

    def __init__(self, files, path=None, grid=None, figtitle=None, y=1.02,
                 titles=None, xlabels=None, ylabels=None, figsize=None,
                 subspace={'left': 0.05, 'right': 1., 'bottom': 0.1, 'top': .9,
                           'wspace': 0., 'hspace': 0.3}, rmax=True,
                 fig_bgcolor=None, ax_bgcolor=None, text_color='black',
                 autocrop=False, autoresize=False):
        """Init."""
        self._data = []
        self._im = []
        self._ax = []
        self._figure = None
        self._figtitle = figtitle
        self._figsize = figsize
        self._subspace = subspace
        self._y = y
        self._rmax = rmax
        self._autocrop = autocrop
        self._autoresize = autoresize

        # ================ CHECKING ================
        # Files / path :
        if isinstance(files, str):
            files = [files]
        if path is not None:
            files = [os.path.join(path, k) for k in files]
        for k in files:
            if not os.path.isfile(k):
                raise ValueError(k + " is not a file.")
        self._files = files

        # Grid :
        if grid is None:
            grid = (1, len(self))
        else:
            # Type checking :
            if not isinstance(grid, (list, tuple)):
                raise ValueError("The grid parameter must be a list/tuple of"
                                 "integers.")
            else:
                ngrid = np.product(grid)
                if ngrid < len(self):
                    raise ValueError("The number of subplots is n_rows x "
                                     "n_columns = " + str(ngrid) + ". But "
                                     "there's " + str(len(self)) + " pictures"
                                     " loaded so it can not be aranged in a"
                                     " " + str(grid) + " grid.")
        self._grid = grid
        self._index = np.arange(np.product(grid)).reshape(*grid)

        # Color :
        self._figcol = color2tuple(fig_bgcolor)
        self._tcol = color2tuple(text_color)
        if ax_bgcolor is None:
            ax_bgcolor = [None] * len(self)
        elif isinstance(ax_bgcolor, (str, tuple)):
            ax_bgcolor = [color2tuple(ax_bgcolor)] * len(self)
        elif isinstance(ax_bgcolor, list):
            if len(ax_bgcolor) != len(self):
                raise ValueError("The length of the ax_bgcolor parameter must "
                                 "be the same as the number of loaded files.")
            else:
                ax_bgcolor = [color2tuple(k) for k in ax_bgcolor]
        self._axcol = ax_bgcolor

        # Titles / xlabels / ylabels :
        self._titles = self._replicate(titles, 'titles')
        self._xlabels = self._replicate(xlabels, 'xlabels')
        self._ylabels = self._replicate(ylabels, 'ylabels')

        # ================ MAKE ================
        self._make()

    def __len__(self):
        """Get the number of loaded pictures."""
        return len(self._files)

    def __iter__(self):
        """Loop over loaded pictures."""
        for k in self._data:
            yield k

    def layout_config(self) -> Dict[str, Any]:
        """Return the layout configuration associated with the figure."""

        config: Dict[str, Any] = {
            'grid': tuple(self._grid) if self._grid is not None else None,
            'subspace': dict(self._subspace) if self._subspace else {},
            'figsize': tuple(self._figsize) if self._figsize else None,
            'figtitle': self._figtitle,
            'y': self._y,
            'rmax': self._rmax,
            'autocrop': self._autocrop,
            'autoresize': self._autoresize,
        }
        return config

    def save_layout(self, layout_file: os.PathLike[str] | str) -> Path:
        """Save the current layout to *layout_file* as JSON."""

        return _write_layout_file(self.layout_config(), layout_file)

    @staticmethod
    def load_layout(layout_file: os.PathLike[str] | str) -> Dict[str, Any]:
        """Load a layout configuration from *layout_file*."""

        return _normalize_layout_config(_read_layout_file(layout_file))

    @classmethod
    def from_layout(cls, files, layout_file: os.PathLike[str] | str, **overrides):
        """Instantiate a :class:`Figure` using a saved layout configuration."""

        config = cls.load_layout(layout_file)
        config.update(overrides)
        return cls(files, **config)

    ##########################################################################
    # METHODS
    ##########################################################################
    def show(self):
        """Display the figure."""
        plt.show()

    def save(self, saveas, dpi=300):
        """Save the figure.

        Parameters
        ----------
        saveas : string
            Name of the saved figure.
        dpi : int | 300
            The resolution of the exported figure.
        """
        self._fig.savefig(saveas, bbox_inches='tight', dpi=dpi,
                          facecolor=self._figcol)

    def colorbar_to_axis(self, toaxis, clim, cmap, vmin=None, under='gray',
                         vmax=None, over='red', title=None, ycb=10.,
                         fz_title=15, ticks='complete', fz_ticks=10,
                         outline=False, orientation='vertical'):
        """Add a colorbar to a particular axis.

        Parameters
        ----------
        toaxis : int
            Integer to specify the axis to which add the colorbar.
        clim : tuple/list
            A tuple of float/int describing the limit of the colorbar.

        cmap : str
            The colormap to use ('viridis', 'jet', 'Spectral'...)
        vmin : float | None
            Minimum threshold. See the under parameter for further details.
        under : string/tuple/list | 'gray'
            Every values bellow vmin will be set to the under color.
        vmax : float | None
            Maximum threshold. See the over parameter for further details.
        over : string/tuple/list | 'red'
            Every values over vmax will be set to the over color.
        title : string | None
            Title of the colorbar.
        ycb : float | 10.
            Distance between the colorbar and it title (if defined).
        fz_title : int/float | 15
            The fontsize of colorbar title.
        ticks : string/int/float/np.ndarray | 'complete'
            Ticks of the colorbar. This parameter is only active if clim
            is defined. Use 'complete' to see only the minimum,
            maximum, vmin and vmax (if defined). Use 'minmax' to only see
            the maximum and minimum. If ticks is a float, an linear
            interpolation between the maximum and minimum will be used.
            Finally, if ticks is a NumPy array, it will be used as colorbar
            ticks directly.
        fz_ticks : int/float | 10
            Fontsize of tick labels.
        outline : bool | False
            Specify if the box arround the colorbar have to be displayed.
        orientation : string | 'vertical'
            Colorbar orientation. Use either 'vertical' or 'horizontal'.

        See also
        --------
        shared_colorbar : colorbar shared by multiple subplots.
        """
        # ----------------- CHECKING -----------------
        if orientation not in ['vertical', 'horizontal']:
            raise ValueError("Colorbar orientation must either be 'vertical' "
                             "or 'horizontal'")

        # ----------------- CURRENT AXIS -----------------
        cim = self._im[toaxis]
        plt.sca(self._ax[toaxis])

        # ----------------- COLORMAP -----------------
        # Manually create the colormap :
        cmap = self._customcmap(cmap, clim, vmin, under, vmax, over)
        cim.set_cmap(cmap)

        # ----------------- COLORBAR -----------------
        cb = plt.colorbar(cim, shrink=0.7, pad=0.01, aspect=10,
                          orientation=orientation)

        # # ----------------- CLIM -----------------
        cim.set_clim(*clim)
        cb.set_clim(*clim)

        # ----------------- CBAR -----------------
        self._cbar(cb, cmap, clim, vmin, under, vmax, over, title, ycb,
                   fz_title, ticks, fz_ticks, outline, orientation, self._tcol)

    def shared_colorbar(self, clim, cmap, position='right', height=.5,
                        width=.02, pltmargin=.02, figmargin=.07, vmin=None,
                        under='gray', vmax=None, over='red', title=None,
                        ycb=10., fz_title=15, ticks='complete', fz_ticks=10,
                        outline=False):
        """Add a colorbar to a particular axis.

        Parameters
        ----------
        toaxis : int
            Integer to specify the axis to which add the colorbar.
        clim : tuple/list
            A tuple of float/int describing the limit of the colorbar.
        cmap : str
            The colormap to use ('viridis', 'jet', 'Spectral'...)
        position : str | 'right'
            Position of the shared colorbar. Use either 'left', 'right',
            or 'bottom'.
        height : float | .5
            Height of the colorbar.
        width : float | .02
            Width of the colorbar.
        pltmargin : float | .05
            Margin between plots and the colorbar.
        figmargin : float | .07
            Margin between the edge of the figure and the colorbar.
        vmin : float | None
            Minimum threshold. See the under parameter for further details.
        under : string/tuple/list | 'gray'
            Every values bellow vmin will be set to the under color.
        vmax : float | None
            Maximum threshold. See the over parameter for further details.
        over : string/tuple/list | 'red'
            Every values over vmax will be set to the over color.
        title : string | None
            Title of the colorbar.
        ycb : float | 10.
            Distance between the colorbar and it title (if defined).
        fz_title : int/float | 15
            The fontsize of colorbar title.
        ticks : string/int/float/np.ndarray | 'complete'
            Ticks of the colorbar. This parameter is only active if clim
            is defined. Use 'complete' to see only the minimum,
            maximum, vmin and vmax (if defined). Use 'minmax' to only see
            the maximum and minimum. If ticks is a float, an linear
            interpolation between the maximum and minimum will be used.
            Finally, if ticks is a NumPy array, it will be used as colorbar
            ticks directly.
        fz_ticks : int/float | 10
            Fontsize of tick labels.
        outline : bool | False
            Specify if the box arround the colorbar have to be displayed.

        See also
        --------
        colorbar_to_axis : add a specific colorbar to an axis.
        """
        # ================ POSITION ================
        if position == 'right':
            plt.subplots_adjust(right=1. - width - figmargin - pltmargin)
            cax = plt.axes([1. - width - figmargin, height / 2, width, height])
            orientation = 'vertical'
        elif position == 'left':
            plt.subplots_adjust(left=figmargin + width + pltmargin)
            cax = plt.axes([figmargin, height / 2, width, height])
            orientation = 'vertical'
        elif position == 'bottom':
            plt.subplots_adjust(bottom=figmargin + width + pltmargin)
            cax = plt.axes([height / 2, figmargin, height, width])
            orientation = 'horizontal'

        cmap = self._customcmap(cmap, clim, vmin, under, vmax, over)
        cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, orientation=orientation,
                                       norm=mpl.colors.Normalize(*clim))

        # ----------------- CBAR -----------------
        self._cbar(cb, cmap, clim, vmin, under, vmax, over, title, ycb,
                   fz_title, ticks, fz_ticks, outline, orientation, self._tcol)

    ##########################################################################
    # SUB-METHODS
    ##########################################################################
    def _replicate(self, arg, name):
        """Replicate a argument if string."""
        if arg is None:
            arg = [None] * len(self)
        elif isinstance(arg, str):
            arg = [arg] * len(self)
        elif isinstance(arg, (list, tuple)):
            if len(arg) != len(self):
                raise ValueError("The '" + name + "' must have the same length"
                                 " as the number of loaded files")
        return arg

    def _make(self):
        """Make the figure."""
        # ================ LOAD / RESIZE ================
        # Load files :
        for k in self._files:
            _dat = imread(k) if not self._autocrop else piccrop(imread(k))
            self._data.append(_dat)
        # Resize :
        if isinstance(self._autoresize, bool) and self._autoresize:
            self._data = picresize(self._data)
        elif isinstance(self._autoresize, dict):
            self._data = picresize(self._data, **self._autoresize)

        # ================ FIGURE ================
        # Figure creation :
        if self._figcol is not None:
            plt.rcParams['figure.facecolor'] = self._figcol
        self._fig = plt.figure(figsize=self._figsize)
        if self._figtitle is not None:
            self._fig.suptitle(self._figtitle, fontsize=14, fontweight='bold',
                               color=self._tcol)
        if self._subspace:
            self._fig.subplots_adjust(**self._subspace)

        # ================ SUBPLOTS ================
        for num, k in enumerate(self):
            # --------- Display ---------
            plt.subplot(self._grid[0], self._grid[1], num + 1)
            im = plt.imshow(k)
            self._im.append(im)
            ax = plt.gca()
            self._ax.append(ax)
            # --------- Background color ---------
            if self._axcol[num] is not None:
                ax.patch.set_facecolor(self._axcol[num])
            # --------- Labels / title ---------
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_xticklabels('')
            ax.set_yticklabels('')
            if self._xlabels[num]:
                ax.set_xlabel(self._xlabels[num], color=self._tcol)
            if self._ylabels[num]:
                ax.set_ylabel(self._ylabels[num], color=self._tcol)
            if self._titles[num]:
                ax.set_title(self._titles[num], y=self._y, color=self._tcol)
            # --------- Remove borders ---------
            if self._rmax:
                for loc, spine in ax.spines.items():
                    if loc in ['left', 'right', 'top', 'bottom']:
                        spine.set_color('none')
                        ax.tick_params(**{loc: False})

    @staticmethod
    def _cbar(cb, cmap, clim, vmin, under, vmax, over, title, ycb, fz_title,
              ticks, fz_ticks, outline, orientation, tcol):
        """Colorbar creation."""
        # ----------------- TITLE -----------------
        if title is not None:
            cb.set_label(title, labelpad=ycb, color=tcol,
                         fontsize=fz_title)

        # ----------------- TICKS -----------------
        if clim is not None:
            # Display only (min, max) :
            if ticks == 'minmax':
                ticks = [clim[0], clim[1]]
            # Display (min, vmin, vmax, max) :
            elif ticks == 'complete':
                ticks = [clim[0]]
                if vmin:
                    ticks.append(vmin)
                if vmax:
                    ticks.append(vmax)
                ticks.append(clim[1])
            # Use linearly spaced ticks :
            elif isinstance(ticks, (int, float)):
                ticks = np.arange(clim[0], clim[1] + ticks, ticks)
            # Set ticks and ticklabels :
            cb.set_ticks(ticks)
            cb.set_ticklabels(ticks)
            cb.ax.tick_params(labelsize=fz_ticks)
            # Change ticks color :
            tic = 'y' if (orientation == 'vertical') else 'x'
            cbytick_obj = plt.getp(cb.ax.axes, tic + 'ticklabels')
            plt.setp(cbytick_obj, color=tcol)

        # ----------------- OUTLINE -----------------
        cb.outline.set_visible(outline)

    @staticmethod
    def _customcmap(cmap, clim, vmin=None, under='gray', vmax=None,
                    over='red', n=1000):
        # Generate linearly spaced data :
        data = np.linspace(clim[0], clim[1], n)
        # Create the colormap and apply to data :
        sc = mpl.cm.ScalarMappable(cmap=cmap)
        data_sc = np.array(sc.to_rgba(data))[:, 0:-1]
        # Vmin / Vmax :
        if vmin is not None:
            data_sc[data < vmin] = color2tuple(under)
        if vmax is not None:
            data_sc[data > vmax] = color2tuple(over)
        # Generate the colormap :
        return mpl.colors.ListedColormap(data_sc, N=n)


class FigureGUI:
    """Qt based interface for building :class:`Figure` layouts."""

    def __init__(
        self,
        figure: Optional[Figure] = None,
        files: Optional[Iterable[str]] = None,
        parent: Optional[Any] = None,
    ) -> None:
        from PySide6 import QtCore, QtGui, QtWidgets
        from PySide6.QtWidgets import QFileDialog, QMessageBox

        from .interface import Ui_FigureMainWindow

        self._QtCore = QtCore
        self._QtGui = QtGui
        self._QtWidgets = QtWidgets
        self._QFileDialog = QFileDialog
        self._QMessageBox = QMessageBox
        self._layout_y = 1.02
        self._layout_rmax = True
        self._layout_autocrop = False
        self._layout_autoresize: Any = False

        self._app = QtWidgets.QApplication.instance()
        self._owns_app = False
        if self._app is None:
            self._app = QtWidgets.QApplication([])
            self._owns_app = True

        self._window = QtWidgets.QMainWindow(parent)
        self._ui = Ui_FigureMainWindow()
        self._ui.setupUi(self._window)
        self._figure = figure

        if figure is not None and files is None:
            files = getattr(figure, '_files', None)

        self._connect_actions()
        if figure is not None:
            self.apply_layout(figure.layout_config())
        else:
            self._reset_layout()

        self._load_files(files or [])
        self._refresh_preview()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def show(self) -> None:
        """Show the interface."""

        self._window.show()

    def exec(self) -> int:
        """Execute the Qt event loop."""

        self.show()
        if self._owns_app:
            return self._app.exec()
        return 0

    def close(self) -> None:
        """Close the interface and stop the event loop if needed."""

        self._window.close()
        if self._owns_app and self._app is not None:
            self._app.quit()

    # ------------------------------------------------------------------
    # Layout helpers
    # ------------------------------------------------------------------
    def apply_layout(self, config: Dict[str, Any]) -> None:
        """Apply a layout configuration to the interface."""

        normalised = _normalize_layout_config(config)
        grid = normalised.get('grid')
        if grid:
            self._ui.rowsSpin.setValue(int(grid[0]))
            self._ui.colsSpin.setValue(int(grid[1]))
        subspace = dict(_DEFAULT_SUBSPACE)
        subspace.update(normalised.get('subspace', {}))
        self._ui.leftMarginSpin.setValue(subspace['left'])
        self._ui.rightMarginSpin.setValue(subspace['right'])
        self._ui.bottomMarginSpin.setValue(subspace['bottom'])
        self._ui.topMarginSpin.setValue(subspace['top'])
        self._ui.wspaceSpin.setValue(subspace['wspace'])
        self._ui.hspaceSpin.setValue(subspace['hspace'])
        figsize = normalised.get('figsize')
        if isinstance(figsize, tuple):
            self._ui.figWidthSpin.setValue(float(figsize[0]))
            self._ui.figHeightSpin.setValue(float(figsize[1]))
        self._ui.figureTitleEdit.setText(normalised.get('figtitle') or '')
        self._layout_y = float(normalised.get('y', self._layout_y))
        self._layout_rmax = bool(normalised.get('rmax', self._layout_rmax))
        self._layout_autocrop = bool(normalised.get('autocrop', self._layout_autocrop))
        self._layout_autoresize = normalised.get('autoresize', self._layout_autoresize)

    def collect_layout(self) -> Dict[str, Any]:
        """Collect the layout configuration from the interface widgets."""

        config: Dict[str, Any] = {
            'grid': (
                int(self._ui.rowsSpin.value()),
                int(self._ui.colsSpin.value()),
            ),
            'subspace': {
                'left': float(self._ui.leftMarginSpin.value()),
                'right': float(self._ui.rightMarginSpin.value()),
                'bottom': float(self._ui.bottomMarginSpin.value()),
                'top': float(self._ui.topMarginSpin.value()),
                'wspace': float(self._ui.wspaceSpin.value()),
                'hspace': float(self._ui.hspaceSpin.value()),
            },
            'figsize': (
                float(self._ui.figWidthSpin.value()),
                float(self._ui.figHeightSpin.value()),
            ),
            'figtitle': self._ui.figureTitleEdit.text() or None,
            'y': self._layout_y,
            'rmax': self._layout_rmax,
            'autocrop': self._layout_autocrop,
            'autoresize': self._layout_autoresize,
        }
        return config

    # ------------------------------------------------------------------
    # Slots
    # ------------------------------------------------------------------
    def _connect_actions(self) -> None:
        ui = self._ui
        ui.addImagesButton.clicked.connect(self._add_images_dialog)
        ui.removeSelectedButton.clicked.connect(self._remove_selected)
        ui.saveLayoutButton.clicked.connect(self._save_layout_dialog)
        ui.loadLayoutButton.clicked.connect(self._load_layout_dialog)
        ui.exportButton.clicked.connect(self._export_current)
        ui.refreshPreviewButton.clicked.connect(self._refresh_preview)
        ui.clearPreviewButton.clicked.connect(self._clear_files)

        ui.actionAddImages.triggered.connect(self._add_images_dialog)
        ui.actionSaveLayout.triggered.connect(self._save_layout_dialog)
        ui.actionLoadLayout.triggered.connect(self._load_layout_dialog)
        ui.actionExportFigure.triggered.connect(self._export_current)
        ui.actionApplyGrid.triggered.connect(self._auto_grid)
        ui.actionResetLayout.triggered.connect(self._reset_layout)
        ui.actionClose.triggered.connect(self.close)

    def _add_images_dialog(self) -> None:
        paths, _ = self._QFileDialog.getOpenFileNames(
            self._window,
            'Select images',
            str(Path.cwd()),
            'Images (*.png *.jpg *.jpeg *.tif *.tiff *.bmp *.gif);;All files (*)',
        )
        if paths:
            self._add_files(paths)

    def _add_files(self, paths: Iterable[str]) -> None:
        paths_list = list(paths)
        for path in paths_list:
            item = self._QtWidgets.QListWidgetItem(os.path.basename(path))
            item.setData(self._QtCore.Qt.UserRole, path)
            self._ui.imageList.addItem(item)
        if paths_list:
            self._status_message(f"Added {len(paths_list)} image(s).")
        self._refresh_preview()

    def _load_files(self, paths: Iterable[str]) -> None:
        self._ui.imageList.clear()
        paths_list = list(paths)
        if paths_list:
            self._add_files(paths_list)

    def _remove_selected(self) -> None:
        selected = self._ui.imageList.selectedItems()
        for item in selected:
            row = self._ui.imageList.row(item)
            self._ui.imageList.takeItem(row)
        if selected:
            self._status_message(f"Removed {len(selected)} image(s).")
        self._refresh_preview()

    def _files_from_list(self) -> Tuple[str, ...]:
        files = []
        for index in range(self._ui.imageList.count()):
            item = self._ui.imageList.item(index)
            path = item.data(self._QtCore.Qt.UserRole) or item.text()
            files.append(str(path))
        return tuple(files)

    def _clear_files(self) -> None:
        self._ui.imageList.clear()
        self._refresh_preview()
        self._status_message('Image list cleared.')

    def _refresh_preview(self) -> None:
        files = self._files_from_list()
        if not files:
            self._ui.previewLabel.setPixmap(self._QtGui.QPixmap())
            self._ui.previewLabel.setText('Drop images here or use “Add Images…”')
            return
        pixmap = self._QtGui.QPixmap(files[-1])
        if pixmap.isNull():
            self._ui.previewLabel.setPixmap(self._QtGui.QPixmap())
            self._ui.previewLabel.setText(os.path.basename(files[-1]))
            return
        target_size = self._ui.previewLabel.size()
        scaled = pixmap.scaled(
            target_size,
            self._QtCore.Qt.KeepAspectRatio,
            self._QtCore.Qt.SmoothTransformation,
        )
        self._ui.previewLabel.setPixmap(scaled)
        self._ui.previewLabel.setText('')

    def _save_layout_dialog(self) -> None:
        path, _ = self._QFileDialog.getSaveFileName(
            self._window,
            'Save figure layout',
            str(Path.cwd() / 'figure_layout.json'),
            'Layout (*.json)',
        )
        if not path:
            return
        layout_path = _write_layout_file(self.collect_layout(), path)
        self._status_message(f"Saved layout to {layout_path}.")

    def _load_layout_dialog(self) -> None:
        path, _ = self._QFileDialog.getOpenFileName(
            self._window,
            'Load figure layout',
            str(Path.cwd()),
            'Layout (*.json)',
        )
        if not path:
            return
        config = Figure.load_layout(path)
        self.apply_layout(config)
        self._status_message(f"Loaded layout from {path}.")

    def _prepare_export_path(self) -> Optional[Path]:
        text = self._ui.exportPathEdit.text().strip()
        fmt = self._ui.formatCombo.currentText()
        if not text:
            path, _ = self._QFileDialog.getSaveFileName(
                self._window,
                'Export figure',
                str(Path.cwd() / f'figure.{fmt}'),
                f'Images (*.{fmt})',
            )
            if not path:
                return None
            text = path
            self._ui.exportPathEdit.setText(text)
        path = Path(text)
        if path.suffix.lower() != f'.{fmt.lower()}':
            path = path.with_suffix(f'.{fmt}')
            self._ui.exportPathEdit.setText(str(path))
        return path

    def _export_current(self) -> None:
        files = self._files_from_list()
        if not files:
            self._warn('Please add at least one image before exporting the figure.')
            return
        export_path = self._prepare_export_path()
        if export_path is None:
            return
        figure = Figure(files, **self.collect_layout())
        dpi = int(self._ui.dpiSpin.value())
        figure.save(str(export_path), dpi=dpi)
        self._status_message(f"Exported figure to {export_path}.")
        if self._ui.openAfterExportCheck.isChecked():
            webbrowser.open(export_path.as_uri())

    def _auto_grid(self) -> None:
        files = self._files_from_list()
        if not files:
            self._status_message('No images available to compute a grid.')
            return
        rows = int(math.ceil(math.sqrt(len(files))))
        cols = int(math.ceil(len(files) / rows))
        self._ui.rowsSpin.setValue(rows)
        self._ui.colsSpin.setValue(cols)
        self._status_message(f'Grid set to {rows} × {cols}.')

    def _reset_layout(self) -> None:
        self._ui.rowsSpin.setValue(1)
        self._ui.colsSpin.setValue(1)
        self._ui.leftMarginSpin.setValue(_DEFAULT_SUBSPACE['left'])
        self._ui.rightMarginSpin.setValue(_DEFAULT_SUBSPACE['right'])
        self._ui.bottomMarginSpin.setValue(_DEFAULT_SUBSPACE['bottom'])
        self._ui.topMarginSpin.setValue(_DEFAULT_SUBSPACE['top'])
        self._ui.wspaceSpin.setValue(_DEFAULT_SUBSPACE['wspace'])
        self._ui.hspaceSpin.setValue(_DEFAULT_SUBSPACE['hspace'])
        self._ui.figWidthSpin.setValue(10.0)
        self._ui.figHeightSpin.setValue(10.0)
        self._ui.figureTitleEdit.clear()
        self._layout_y = 1.02
        self._layout_rmax = True
        self._layout_autocrop = False
        self._layout_autoresize = False
        self._status_message('Layout reset to defaults.')

    def _warn(self, message: str) -> None:
        self._QMessageBox.warning(self._window, 'Figure export', message)

    def _status_message(self, message: str) -> None:
        self._ui.statusbar.showMessage(message, 5000)
