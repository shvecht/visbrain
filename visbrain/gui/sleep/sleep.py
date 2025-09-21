"""Top level Sleep class."""
import logging

import numpy as np

import vispy.scene.cameras as viscam

from .interface import UiInit, UiElements
from .model import SleepDataset
from .visuals import Visuals
from visbrain._pyqt_module import _PyQtModule
from visbrain.utils import (FixedCam, color2vb, MouseEventControl)
from visbrain.config import PROFILER

logger = logging.getLogger('visbrain')


class Sleep(_PyQtModule, UiInit, Visuals, UiElements, MouseEventControl):
    """Visualize and edit sleep data.

    Use this module to :

        * Load and visualize polysomnographic data and spectrogram.
        * Load, edit and save hypnogram from the interface
        * Perform automatic events detection
        * Further signal processing tools (de-mean, de-trend and filtering)
        * Topographic data visualization

    Sleep has been developped in collaboration with Raphael Vallat.

    Parameters
    ----------
    data : string, array_like | None
        Polysomnographic data. Must either be a path to a supported file (see
        notes) or an array of raw data of shape (n_channels, n_pts). If None,
        a dialog window to load the file should appear.
    hypno : array_like | None
        Hypnogram data. Should be a raw vector of shape (n_pts,)
    config_file : string | None
        Path to the configuration file (.txt)
    annotations : string | None
        Path to the annotation file (.txt, .csv). Alternatively, you can pass
        an annotation instance of MNE or simply an (N,) array describing
        the onset.
    channels : list | None
        List of channel names. The length of this list must be n_channels.
    sf : float | None
        The sampling frequency of raw data.
    downsample : float | 100.
        The downsampling frequency for the data and hypnogram raw data.
    axis : bool | False
        Specify if each axis have to contains its own axis. Be carefull
        with this option, the rendering can be much slower.
    href : list | ['art', 'wake', 'rem', 'n1', 'n2', 'n3']
        List of sleep stages. This list can be used to changed the display
        order into the GUI.
    preload : bool | True
        Preload data into memory. For large datasets, turn this parameter to
        True.
    use_mne : bool | False
        Force to load the file using mne.io functions.
    kwargs_mne : dict | {}
        Dictionary to pass to the mne.io loading function.

    Notes
    -----
    .. note::
        * Supported polysomnographic files : by default, Sleep support .vhdr
          (BrainVision), .eeg (Elan), .trc (Micromed) and .edf (European Data
          Format). If mne-python is installed, this default list of supported
          files is extended to .cnt, .egi, .mff, .edf, .bdf, .gdf, .set, .vhdr.
        * Supported hypnogram files : by default, Sleep support .txt, .csv and
          .hyp hypnogram files.

    .. deprecated:: 0.3.4
        Input arguments `file` and `hypno_file` has been deprecated in 0.3.4
        release. Use instead the `data` and `hypno` inputs.
    """

    def __init__(self, data=None, hypno=None, config_file=None,
                 annotations=None, channels=None, sf=None, downsample=100.,
                 axis=True, href=['art', 'wake', 'rem', 'n1', 'n2', 'n3'],
                 preload=True, use_mne=False, kwargs_mne={}, verbose=None,
                 model=None):
        """Init."""
        _PyQtModule.__init__(self, verbose=verbose, icon='sleep_icon.svg')
        # ====================== APP CREATION ======================
        UiInit.__init__(self)

        # Set default GUI state :
        self._set_default_state()

        # Mouse control :
        MouseEventControl.__init__(self)

        # ====================== LOAD FILE ======================
        PROFILER("Import file", as_type='title')
        if model is None:
            model = SleepDataset(data, channels, sf, hypno, href, preload,
                                 use_mne, downsample, kwargs_mne,
                                 annotations)
        elif not isinstance(model, SleepDataset):
            raise TypeError("model must be an instance of SleepDataset")
        self._model = model

        # ====================== VARIABLES ======================
        # Check all data :
        self._config_file = config_file
        self._annot_mark = np.array([])
        self._ax = axis
        # ---------- Default line width ----------
        self._lw = 1.
        self._lwhyp = 2
        self._defwin = 30.
        self._defstd = 5.
        # ---------- Default colors ----------
        self._chancolor = '#292824'
        # self._hypcolor = '#292824'
        # Hypnogram color :
        self._hypcolor = {-1: '#8bbf56', 0: '#56bf8b', 1: '#aabcce',
                          2: '#405c79', 3: '#0b1c2c', 4: '#bf5656'}
        # Convert color :
        hconvinv = self._model.hconvinv
        if self._model.hconv != hconvinv:
            hypc = self._hypcolor.copy()
            for k in self._model.hconv.keys():
                self._hypcolor[k] = hypc[hconvinv[k]]
        self._indicol = '#e74c3c'
        # Default spectrogram colormap :
        self._defcmap = 'viridis'
        # Spindles / REM / Peaks colors :
        self._defspin = color2vb('#d73737')
        self._defsw = color2vb('#56bf8b')
        self._defkc = color2vb('#b45a3c')
        self._defrem = color2vb('#6684e1')
        self._defmt = color2vb('#FE8625')
        self._defpeaks = '#b854d4'
        # ---------- Symbol ----------
        self._spinsym = 'x'
        self._swsym = 'o'
        self._kcsym = 'diamond'
        self._remsym = 'triangle_down'
        self._mtsym = 'star'
        self._peaksym = 'disc'
        # ---------- Custom detections ----------
        # Get some data info (min / max / std / mean)
        self._get_data_info()
        PROFILER("Data info")

        # ====================== USER & GUI INTERACTION  ======================
        # User <-> GUI :
        PROFILER("Initialize GUI interactions", as_type='title')
        UiElements.__init__(self)

        # ====================== CAMERAS ======================
        self._cam_creation()

        # ====================== OBJECTS CREATION ======================
        PROFILER("Initialize visual elements", as_type='title')
        Visuals.__init__(self)

        # ====================== FUNCTIONS ON LOAD ======================
        self._fcns_on_creation()
        PROFILER("Functions on creation")

    def __len__(self):
        """Return the number of channels."""
        return len(self._model)

    def __getitem__(self, key):
        """Return corresponding data info."""
        return self._model[key]

    def replace_detections(self, dtype, method):
        """Replace the default detection methods.

        Parameters
        ----------
        dtype : string
            Name of the method to replace. Should be 'spindle', 'sw' (slow
            waves), 'kc' (k-complexes), 'rem' (rapid eye movements), 'mt'
            (muscle twitches) or 'peak'.
        method : function
            Function to replace the detection. The function should take as an
            input :

                * A vector array of data of shape (n_time_points,)
                * The sampling frequency (float)
                * The time vector of shape (n_time_points,)
                * A vector array for the hypnogram of shape (n_time_points,)

            Then, the function should return indices of relevant events.
            Returned indices should either be :

                *  An array of shape (n_events, 2) where `n_events` describe
                   the number of detected events. The first and second columns
                   of the array respectively describe where detected events
                   start and finished.
                * A boolean vector of shape (n_time_points,) where True values
                  refer to detected events.
                * An array which contains consecutive indices of detected
                  events.

        Examples
        --------
        >>> def method(data, sf, hypno):
        >>>     # Do stuff
        >>>     indices = ...
        >>>     return indices
        """
        # Type checking :
        meth_names = ('spindle', 'sw', 'kc', 'rem', 'mt', 'peak')
        if dtype not in meth_names:
            raise ValueError("dtype should be a string. Choose between "
                             "%s" % ', '.join(meth_names))
        assert hasattr(method, '__call__')
        # Save the method :
        self._model.replace_detection(dtype, method)
        # Set stack detections enable / disable :
        self._fcn_switch_detection()

    ###########################################################################
    # SUB-FONCTIONS
    ###########################################################################
    def _get_data_info(self):
        """Get some info about data (min, max, std, mean, dist)."""
        return self._model.refresh_data_info()

    # ------------------------------------------------------------------
    # Data accessors proxying to the model layer
    # ------------------------------------------------------------------
    @property
    def _data(self):
        return self._model.data

    @_data.setter
    def _data(self, value):
        self._model.data = value

    @property
    def _hypno(self):
        return self._model.hypno

    @_hypno.setter
    def _hypno(self, value):
        self._model.hypno = value

    @property
    def _time(self):
        return self._model.time

    @_time.setter
    def _time(self, value):
        self._model.time = value

    @property
    def _channels(self):
        return self._model.channels

    @_channels.setter
    def _channels(self, value):
        self._model.channels = value

    @property
    def _href(self):
        return self._model.href

    @_href.setter
    def _href(self, value):
        self._model.href = value

    @property
    def _hconv(self):
        return self._model.hconv

    @_hconv.setter
    def _hconv(self, value):
        self._model.hconv = value

    @property
    def _hconvinv(self):
        return self._model.hconvinv

    @property
    def _sf(self):
        return self._model.sf

    @_sf.setter
    def _sf(self, value):
        self._model.sf = value

    @property
    def _sfori(self):
        return self._model.sfori

    @_sfori.setter
    def _sfori(self, value):
        self._model.sfori = value

    @property
    def _dsf(self):
        return self._model.dsf

    @_dsf.setter
    def _dsf(self, value):
        self._model.dsf = value

    @property
    def _N(self):
        return self._model.n_points

    @_N.setter
    def _N(self, value):
        self._model.n_points = value

    @property
    def _file(self):
        return self._model.file

    @_file.setter
    def _file(self, value):
        self._model.file = value

    @property
    def _annot_file(self):
        return self._model.annotations

    @_annot_file.setter
    def _annot_file(self, value):
        self._model.annotations = value

    @property
    def _datainfo(self):
        return self._model.datainfo

    @_datainfo.setter
    def _datainfo(self, value):
        self._model.datainfo = value

    @property
    def _custom_detections(self):
        return self._model.custom_detections

    def _set_default_state(self):
        """Set the default window state."""
        # ================= TAB =================
        self._DetectionTab.setCurrentIndex(0)
        self._stacked_panels.setCurrentIndex(0)
        self._stacked_tools.setCurrentIndex(0)
        self._stacked_detections.setCurrentIndex(0)

    def _cam_creation(self):
        """Create a set of cameras."""
        # ------------------- Channels -------------------
        self._chanCam = []
        for k in range(len(self)):
            self._chanCam.append(FixedCam())  # viscam.PanZoomCamera()
        # ------------------- Spectrogram -------------------
        self._speccam = FixedCam()  # viscam.PanZoomCamera()
        self._specCanvas.set_camera(self._speccam)
        # ------------------- Hypnogram -------------------
        self._hypcam = FixedCam()  # viscam.PanZoomCamera()
        self._hypCanvas.set_camera(self._hypcam)
        # ------------------- Topoplot -------------------
        self._topocam = viscam.PanZoomCamera()
        self._topoCanvas.set_camera(self._topocam)
        # ------------------- Time axis -------------------
        self._timecam = FixedCam()
        self._TimeAxis.set_camera(self._timecam)

        # Keep all cams :
        self._allCams = (self._chanCam, self._speccam, self._hypcam,
                         self._topocam, self._timecam)

    def _fcns_on_creation(self):
        """Applied on creation."""
        self._fcn_grid_toggle()
        self._fcn_scorwin_indicator_toggle()
        self._fcn_sigwin_settings()
        self._fcn_slider_move()
        self._chanChecks[0].setChecked(True)
        self._hypLabel.setVisible(self.menuDispHypno.isChecked())
        self._fcn_chan_viz()
        self._fcn_chan_sym_amp()
        self._fcn_info_update()
        self._fcn_hypno_to_score()
        # Set objects visible :
        self._SpecW.setVisible(True)
        self._HypW.setVisible(True)
        self._TimeAxisW.setVisible(True)
        # File to load :
        if self._config_file is not None:  # Config file
            self._load_config(filename=self._config_file)
        if self._annot_file is not None:   # Annotation file
            self._load_annotation_table(filename=self._annot_file)
