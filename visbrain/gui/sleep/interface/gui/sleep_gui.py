# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sleep_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QSplitter,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1359, 1116)
        font = QFont()
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionCortical_repartition = QAction(MainWindow)
        self.actionCortical_repartition.setObjectName(u"actionCortical_repartition")
        self.actionCortical = QAction(MainWindow)
        self.actionCortical.setObjectName(u"actionCortical")
        self.actionSagittal = QAction(MainWindow)
        self.actionSagittal.setObjectName(u"actionSagittal")
        self.actionAxial = QAction(MainWindow)
        self.actionAxial.setObjectName(u"actionAxial")
        self.actionCamera = QAction(MainWindow)
        self.actionCamera.setObjectName(u"actionCamera")
        self.actionLeft = QAction(MainWindow)
        self.actionLeft.setObjectName(u"actionLeft")
        self.actionRight = QAction(MainWindow)
        self.actionRight.setObjectName(u"actionRight")
        self.menuDispSettings = QAction(MainWindow)
        self.menuDispSettings.setObjectName(u"menuDispSettings")
        self.menuDispSettings.setCheckable(True)
        self.menuDispSettings.setChecked(True)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionProjection = QAction(MainWindow)
        self.actionProjection.setObjectName(u"actionProjection")
        self.actionRepartition = QAction(MainWindow)
        self.actionRepartition.setObjectName(u"actionRepartition")
        self.actionShortcuts = QAction(MainWindow)
        self.actionShortcuts.setObjectName(u"actionShortcuts")
        self.actionShortcuts.setCheckable(True)
        self.actionUi_settings = QAction(MainWindow)
        self.actionUi_settings.setObjectName(u"actionUi_settings")
        self.actionUi_settings.setCheckable(True)
        self.actionUi_settings.setChecked(False)
        self.actionNdPlt = QAction(MainWindow)
        self.actionNdPlt.setObjectName(u"actionNdPlt")
        self.actionNdPlt.setCheckable(True)
        self.actionOnedPlt = QAction(MainWindow)
        self.actionOnedPlt.setObjectName(u"actionOnedPlt")
        self.actionOnedPlt.setCheckable(True)
        self.actionImage = QAction(MainWindow)
        self.actionImage.setObjectName(u"actionImage")
        self.actionImage.setCheckable(True)
        self.actionColormap = QAction(MainWindow)
        self.actionColormap.setObjectName(u"actionColormap")
        self.actionColormap.setCheckable(True)
        self.menuShortcut = QAction(MainWindow)
        self.menuShortcut.setObjectName(u"menuShortcut")
        self.menuDocumentation = QAction(MainWindow)
        self.menuDocumentation.setObjectName(u"menuDocumentation")
        self.actionScreenshot = QAction(MainWindow)
        self.actionScreenshot.setObjectName(u"actionScreenshot")
        self.actionSave_hypnogram = QAction(MainWindow)
        self.actionSave_hypnogram.setObjectName(u"actionSave_hypnogram")
        self.actionSave_infos = QAction(MainWindow)
        self.actionSave_infos.setObjectName(u"actionSave_infos")
        self.actionSave_scoring = QAction(MainWindow)
        self.actionSave_scoring.setObjectName(u"actionSave_scoring")
        self.actionSave_detection = QAction(MainWindow)
        self.actionSave_detection.setObjectName(u"actionSave_detection")
        self.actionSave_all = QAction(MainWindow)
        self.actionSave_all.setObjectName(u"actionSave_all")
        self.menuExit = QAction(MainWindow)
        self.menuExit.setObjectName(u"menuExit")
        self.actionLoad_hypnogram = QAction(MainWindow)
        self.actionLoad_hypnogram.setObjectName(u"actionLoad_hypnogram")
        self.menuSaveInfoTable = QAction(MainWindow)
        self.menuSaveInfoTable.setObjectName(u"menuSaveInfoTable")
        self.menuSaveScoringTable = QAction(MainWindow)
        self.menuSaveScoringTable.setObjectName(u"menuSaveScoringTable")
        self.actionAll = QAction(MainWindow)
        self.actionAll.setObjectName(u"actionAll")
        self.menuLoadHypno = QAction(MainWindow)
        self.menuLoadHypno.setObjectName(u"menuLoadHypno")
        self.menuLoadData = QAction(MainWindow)
        self.menuLoadData.setObjectName(u"menuLoadData")
        self.menuLoadData.setEnabled(False)
        self.actionHypnogram_figure = QAction(MainWindow)
        self.actionHypnogram_figure.setObjectName(u"actionHypnogram_figure")
        self.menuLoadConfig = QAction(MainWindow)
        self.menuLoadConfig.setObjectName(u"menuLoadConfig")
        self.menuSaveConfig = QAction(MainWindow)
        self.menuSaveConfig.setObjectName(u"menuSaveConfig")
        self.menuDownload_pdf_doc = QAction(MainWindow)
        self.menuDownload_pdf_doc.setObjectName(u"menuDownload_pdf_doc")
        self.menuSaveHypnogramFigure = QAction(MainWindow)
        self.menuSaveHypnogramFigure.setObjectName(u"menuSaveHypnogramFigure")
        self.menuSaveHypnogramData = QAction(MainWindow)
        self.menuSaveHypnogramData.setObjectName(u"menuSaveHypnogramData")
        self.menuSaveDetectAll = QAction(MainWindow)
        self.menuSaveDetectAll.setObjectName(u"menuSaveDetectAll")
        self.menuSaveDetectSelected = QAction(MainWindow)
        self.menuSaveDetectSelected.setObjectName(u"menuSaveDetectSelected")
        self.menuSaveScreenshotEntire = QAction(MainWindow)
        self.menuSaveScreenshotEntire.setObjectName(u"menuSaveScreenshotEntire")
        self.menuSaveScreenshotSelected = QAction(MainWindow)
        self.menuSaveScreenshotSelected.setObjectName(u"menuSaveScreenshotSelected")
        self.menuSaveScreenshotSelected.setEnabled(False)
        self.menuLoadDetectAll = QAction(MainWindow)
        self.menuLoadDetectAll.setObjectName(u"menuLoadDetectAll")
        self.menuLoadDetectSelect = QAction(MainWindow)
        self.menuLoadDetectSelect.setObjectName(u"menuLoadDetectSelect")
        self.menuDispSpec = QAction(MainWindow)
        self.menuDispSpec.setObjectName(u"menuDispSpec")
        self.menuDispSpec.setCheckable(True)
        self.menuDispSpec.setChecked(True)
        self.menuDispHypno = QAction(MainWindow)
        self.menuDispHypno.setObjectName(u"menuDispHypno")
        self.menuDispHypno.setCheckable(True)
        self.menuDispHypno.setChecked(True)
        self.menuDispNavbar = QAction(MainWindow)
        self.menuDispNavbar.setObjectName(u"menuDispNavbar")
        self.menuDispNavbar.setCheckable(True)
        self.menuDispNavbar.setChecked(True)
        self.menuDispTimeax = QAction(MainWindow)
        self.menuDispTimeax.setObjectName(u"menuDispTimeax")
        self.menuDispTimeax.setCheckable(True)
        self.menuDispTimeax.setChecked(True)
        self.menuDispTopo = QAction(MainWindow)
        self.menuDispTopo.setObjectName(u"menuDispTopo")
        self.menuDispTopo.setCheckable(True)
        self.menuDispIndic = QAction(MainWindow)
        self.menuDispIndic.setObjectName(u"menuDispIndic")
        self.menuDispIndic.setCheckable(True)
        self.menuDispIndic.setChecked(True)
        self.actionZoom_mode = QAction(MainWindow)
        self.actionZoom_mode.setObjectName(u"actionZoom_mode")
        self.actionZoom_mode.setCheckable(True)
        self.menuDispZoom = QAction(MainWindow)
        self.menuDispZoom.setObjectName(u"menuDispZoom")
        self.menuDispZoom.setCheckable(True)
        self.menuSettingCleanHyp = QAction(MainWindow)
        self.menuSettingCleanHyp.setObjectName(u"menuSettingCleanHyp")
        self.menuSaveAnnotations = QAction(MainWindow)
        self.menuSaveAnnotations.setObjectName(u"menuSaveAnnotations")
        self.menuLoadAnnotations = QAction(MainWindow)
        self.menuLoadAnnotations.setObjectName(u"menuLoadAnnotations")
        self.menuSaveScreenshot = QAction(MainWindow)
        self.menuSaveScreenshot.setObjectName(u"menuSaveScreenshot")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 3, 1, 3)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.q_widget = QWidget(self.splitter)
        self.q_widget.setObjectName(u"q_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.q_widget.sizePolicy().hasHeightForWidth())
        self.q_widget.setSizePolicy(sizePolicy)
        self.q_widget.setMinimumSize(QSize(0, 0))
        self.q_widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.q_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.QuickSettings = QTabWidget(self.q_widget)
        self.QuickSettings.setObjectName(u"QuickSettings")
        self.QuickSettings.setFocusPolicy(Qt.StrongFocus)
        self.QuickSettings.setMaximumSize(QSize(16777215, 16777215))
        self.QuickSettings.setAutoFillBackground(False)
        self.QuickSettings.setTabShape(QTabWidget.Rounded)
        self.QuickSettings.setMovable(True)
        self.q_Panels = QWidget()
        self.q_Panels.setObjectName(u"q_Panels")
        self.verticalLayout = QVBoxLayout(self.q_Panels)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.q_Panels)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.line_14 = QFrame(self.frame)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setMinimumSize(QSize(10, 0))
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_24.addWidget(self.line_14, 0, 1, 1, 1)

        self.label_77 = QLabel(self.frame)
        self.label_77.setObjectName(u"label_77")
        font1 = QFont()
        font1.setItalic(True)
        self.label_77.setFont(font1)

        self.gridLayout_24.addWidget(self.label_77, 0, 0, 1, 1)

        self._pan_pick = QComboBox(self.frame)
        self._pan_pick.addItem("")
        self._pan_pick.addItem("")
        self._pan_pick.addItem("")
        self._pan_pick.addItem("")
        self._pan_pick.setObjectName(u"_pan_pick")

        self.gridLayout_24.addWidget(self._pan_pick, 0, 2, 1, 1)

        self.horizontalSpacer_44 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_44, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self._stacked_panels = QStackedWidget(self.q_Panels)
        self._stacked_panels.setObjectName(u"_stacked_panels")
        self._stacked_panels.setFocusPolicy(Qt.StrongFocus)
        self._stacked_panels.setFrameShape(QFrame.NoFrame)
        self._channels_page = QWidget()
        self._channels_page.setObjectName(u"_channels_page")
        self.verticalLayout_34 = QVBoxLayout(self._channels_page)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.groupBox = QGroupBox(self._channels_page)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, -1, 0, -1)
        self.line_13 = QFrame(self.groupBox)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_13)

        self._PanScrollChan = QScrollArea(self.groupBox)
        self._PanScrollChan.setObjectName(u"_PanScrollChan")
        self._PanScrollChan.setMinimumSize(QSize(0, 0))
        self._PanScrollChan.setFrameShape(QFrame.Box)
        self._PanScrollChan.setFrameShadow(QFrame.Sunken)
        self._PanScrollChan.setWidgetResizable(True)
        self._PanScrollChan.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 341, 657))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget = QWidget(self.scrollAreaWidgetContents_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self._PanChanLay = QGridLayout()
        self._PanChanLay.setObjectName(u"_PanChanLay")
        self._PanChanLay.setSizeConstraint(QLayout.SetMaximumSize)
        self._PanChanLay.setHorizontalSpacing(6)
        self._PanChanLay.setVerticalSpacing(9)

        self.verticalLayout_5.addLayout(self._PanChanLay)


        self.verticalLayout_14.addWidget(self.widget)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self._PanScrollChan.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_13.addWidget(self._PanScrollChan)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, -1, 0, -1)
        self.line_22 = QFrame(self.groupBox_7)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.HLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_28.addWidget(self.line_22)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.widget_6 = QWidget(self.groupBox_7)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self._PanAllAmpMin = QDoubleSpinBox(self.widget_6)
        self._PanAllAmpMin.setObjectName(u"_PanAllAmpMin")
        self._PanAllAmpMin.setDecimals(1)
        self._PanAllAmpMin.setMaximum(100000.000000000000000)
        self._PanAllAmpMin.setValue(0.000000000000000)

        self.horizontalLayout_4.addWidget(self._PanAllAmpMin)

        self._PanAllAmpMax = QDoubleSpinBox(self.widget_6)
        self._PanAllAmpMax.setObjectName(u"_PanAllAmpMax")
        self._PanAllAmpMax.setDecimals(1)
        self._PanAllAmpMax.setMinimum(-100000.000000000000000)
        self._PanAllAmpMax.setMaximum(100000.000000000000000)

        self.horizontalLayout_4.addWidget(self._PanAllAmpMax)


        self.gridLayout_13.addWidget(self.widget_6, 0, 1, 1, 2)

        self.label_35 = QLabel(self.groupBox_7)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_13.addWidget(self.label_35, 0, 0, 1, 1)

        self._PanAmpAuto = QCheckBox(self.groupBox_7)
        self._PanAmpAuto.setObjectName(u"_PanAmpAuto")

        self.gridLayout_13.addWidget(self._PanAmpAuto, 2, 0, 1, 3)

        self._PanAmpSym = QCheckBox(self.groupBox_7)
        self._PanAmpSym.setObjectName(u"_PanAmpSym")
        self._PanAmpSym.setChecked(True)

        self.gridLayout_13.addWidget(self._PanAmpSym, 1, 0, 1, 3)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_9)

        self._PanChanSelectAll = QPushButton(self.groupBox_7)
        self._PanChanSelectAll.setObjectName(u"_PanChanSelectAll")

        self.horizontalLayout_23.addWidget(self._PanChanSelectAll)

        self.horizontalSpacer_14 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_14)

        self._PanChanDeselectAll = QPushButton(self.groupBox_7)
        self._PanChanDeselectAll.setObjectName(u"_PanChanDeselectAll")

        self.horizontalLayout_23.addWidget(self._PanChanDeselectAll)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_12)


        self.gridLayout_13.addLayout(self.horizontalLayout_23, 3, 0, 1, 3)


        self.verticalLayout_28.addLayout(self.gridLayout_13)


        self.verticalLayout_13.addWidget(self.groupBox_7)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.line_38 = QFrame(self.groupBox_4)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.Shape.HLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_38)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(-1, 0, -1, -1)
        self._channels_lw = QDoubleSpinBox(self.groupBox_4)
        self._channels_lw.setObjectName(u"_channels_lw")
        self._channels_lw.setDecimals(1)
        self._channels_lw.setMinimum(1.000000000000000)
        self._channels_lw.setMaximum(10.000000000000000)

        self.gridLayout_15.addWidget(self._channels_lw, 0, 2, 1, 1)

        self.horizontalSpacer_48 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_48, 2, 2, 1, 1)

        self.label_36 = QLabel(self.groupBox_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)

        self.gridLayout_15.addWidget(self.label_36, 0, 0, 1, 1)

        self.line_15 = QFrame(self.groupBox_4)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_15, 0, 1, 1, 1)

        self._channels_alias = QCheckBox(self.groupBox_4)
        self._channels_alias.setObjectName(u"_channels_alias")

        self.gridLayout_15.addWidget(self._channels_alias, 1, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_15)


        self.verticalLayout_13.addWidget(self.groupBox_4)


        self.verticalLayout_34.addWidget(self.groupBox)

        self._stacked_panels.addWidget(self._channels_page)
        self._spec_page = QWidget()
        self._spec_page.setObjectName(u"_spec_page")
        self.verticalLayout_35 = QVBoxLayout(self._spec_page)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self._PanSpecMethod = QComboBox(self._spec_page)
        self._PanSpecMethod.addItem("")
        self._PanSpecMethod.addItem("")
        self._PanSpecMethod.addItem("")
        self._PanSpecMethod.setObjectName(u"_PanSpecMethod")

        self.gridLayout_4.addWidget(self._PanSpecMethod, 1, 2, 1, 1)

        self.label_54 = QLabel(self._spec_page)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font1)

        self.gridLayout_4.addWidget(self.label_54, 0, 0, 1, 1)

        self.line_17 = QFrame(self._spec_page)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setMinimumSize(QSize(10, 0))
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_17, 1, 1, 1, 1)

        self.label_73 = QLabel(self._spec_page)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font1)

        self.gridLayout_4.addWidget(self.label_73, 1, 0, 1, 1)

        self.line_18 = QFrame(self._spec_page)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setMinimumSize(QSize(10, 0))
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_18, 2, 1, 1, 1)

        self.label_55 = QLabel(self._spec_page)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font1)

        self.gridLayout_4.addWidget(self.label_55, 3, 0, 1, 1)

        self.line_29 = QFrame(self._spec_page)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setMinimumSize(QSize(10, 0))
        self.line_29.setFrameShape(QFrame.Shape.VLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_29, 3, 1, 1, 1)

        self._PanSpecChan = QComboBox(self._spec_page)
        self._PanSpecChan.setObjectName(u"_PanSpecChan")

        self.gridLayout_4.addWidget(self._PanSpecChan, 0, 2, 1, 1)

        self.line_8 = QFrame(self._spec_page)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMinimumSize(QSize(10, 0))
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_8, 0, 1, 1, 1)

        self.label_29 = QLabel(self._spec_page)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.gridLayout_4.addWidget(self.label_29, 2, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self._PanSpecCmap = QComboBox(self._spec_page)
        self._PanSpecCmap.setObjectName(u"_PanSpecCmap")

        self.gridLayout_6.addWidget(self._PanSpecCmap, 0, 0, 1, 1)

        self._PanSpecCmapInv = QCheckBox(self._spec_page)
        self._PanSpecCmapInv.setObjectName(u"_PanSpecCmapInv")

        self.gridLayout_6.addWidget(self._PanSpecCmapInv, 0, 1, 1, 1)

        self.label_24 = QLabel(self._spec_page)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_6.addWidget(self.label_24, 1, 0, 1, 1)

        self._PanSpecCon = QDoubleSpinBox(self._spec_page)
        self._PanSpecCon.setObjectName(u"_PanSpecCon")
        self._PanSpecCon.setDecimals(1)
        self._PanSpecCon.setMinimum(0.000000000000000)
        self._PanSpecCon.setMaximum(1.000000000000000)
        self._PanSpecCon.setSingleStep(0.100000000000000)
        self._PanSpecCon.setValue(0.500000000000000)

        self.gridLayout_6.addWidget(self._PanSpecCon, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_6, 2, 2, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer, 5, 2, 1, 1)

        self.line_31 = QFrame(self._spec_page)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setMinimumSize(QSize(10, 0))
        self.line_31.setFrameShape(QFrame.Shape.VLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_12.addWidget(self.line_31, 0, 1, 1, 1)

        self.label_74 = QLabel(self._spec_page)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font1)

        self.gridLayout_12.addWidget(self.label_74, 3, 0, 1, 1)

        self._PanSpecInterp = QComboBox(self._spec_page)
        self._PanSpecInterp.addItem("")
        self._PanSpecInterp.addItem("")
        self._PanSpecInterp.addItem("")
        self._PanSpecInterp.addItem("")
        self._PanSpecInterp.addItem("")
        self._PanSpecInterp.addItem("")
        self._PanSpecInterp.addItem("")
        self._PanSpecInterp.addItem("")
        self._PanSpecInterp.addItem("")
        self._PanSpecInterp.addItem("")
        self._PanSpecInterp.setObjectName(u"_PanSpecInterp")

        self.gridLayout_12.addWidget(self._PanSpecInterp, 3, 2, 1, 1)

        self.label_15 = QLabel(self._spec_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout_12.addWidget(self.label_15, 1, 0, 1, 1)

        self._PanSpecNfft = QDoubleSpinBox(self._spec_page)
        self._PanSpecNfft.setObjectName(u"_PanSpecNfft")
        self._PanSpecNfft.setDecimals(1)
        self._PanSpecNfft.setMinimum(0.100000000000000)
        self._PanSpecNfft.setMaximum(1000.000000000000000)
        self._PanSpecNfft.setValue(30.000000000000000)

        self.gridLayout_12.addWidget(self._PanSpecNfft, 0, 2, 1, 1)

        self.line_34 = QFrame(self._spec_page)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setMinimumSize(QSize(10, 0))
        self.line_34.setFrameShape(QFrame.Shape.VLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_12.addWidget(self.line_34, 3, 1, 1, 1)

        self._PanSpecStep = QDoubleSpinBox(self._spec_page)
        self._PanSpecStep.setObjectName(u"_PanSpecStep")
        self._PanSpecStep.setDecimals(1)
        self._PanSpecStep.setMaximum(0.800000000000000)
        self._PanSpecStep.setSingleStep(0.100000000000000)
        self._PanSpecStep.setValue(0.000000000000000)

        self.gridLayout_12.addWidget(self._PanSpecStep, 1, 2, 1, 1)

        self.line_32 = QFrame(self._spec_page)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setMinimumSize(QSize(10, 0))
        self.line_32.setFrameShape(QFrame.Shape.VLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_12.addWidget(self.line_32, 1, 1, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_16 = QLabel(self._spec_page)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_24.addWidget(self.label_16)

        self._PanSpecFstart = QDoubleSpinBox(self._spec_page)
        self._PanSpecFstart.setObjectName(u"_PanSpecFstart")
        self._PanSpecFstart.setDecimals(1)
        self._PanSpecFstart.setMinimum(0.500000000000000)
        self._PanSpecFstart.setMaximum(190.000000000000000)

        self.horizontalLayout_24.addWidget(self._PanSpecFstart)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_7)

        self.label_17 = QLabel(self._spec_page)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_24.addWidget(self.label_17)

        self._PanSpecFend = QDoubleSpinBox(self._spec_page)
        self._PanSpecFend.setObjectName(u"_PanSpecFend")
        self._PanSpecFend.setDecimals(1)
        self._PanSpecFend.setMinimum(0.100000000000000)
        self._PanSpecFend.setMaximum(200.000000000000000)
        self._PanSpecFend.setValue(20.000000000000000)

        self.horizontalLayout_24.addWidget(self._PanSpecFend)


        self.gridLayout_12.addLayout(self.horizontalLayout_24, 2, 2, 1, 1)

        self.label_14 = QLabel(self._spec_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_12.addWidget(self.label_14, 0, 0, 1, 1)

        self.line_33 = QFrame(self._spec_page)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setMinimumSize(QSize(10, 0))
        self.line_33.setFrameShape(QFrame.Shape.VLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_12.addWidget(self.line_33, 2, 1, 1, 1)

        self.label_32 = QLabel(self._spec_page)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)

        self.gridLayout_12.addWidget(self.label_32, 2, 0, 1, 1)

        self._PanSpecNormW = QWidget(self._spec_page)
        self._PanSpecNormW.setObjectName(u"_PanSpecNormW")
        self._PanSpecNormW.setEnabled(False)
        self._PanSpecNormW.setMinimumSize(QSize(0, 20))
        self.gridLayout_5 = QGridLayout(self._PanSpecNormW)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.line_35 = QFrame(self._PanSpecNormW)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setMinimumSize(QSize(10, 0))
        self.line_35.setFrameShape(QFrame.Shape.VLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_35, 0, 1, 1, 1)

        self._PanSpecNorm = QComboBox(self._PanSpecNormW)
        self._PanSpecNorm.addItem("")
        self._PanSpecNorm.addItem("")
        self._PanSpecNorm.addItem("")
        self._PanSpecNorm.addItem("")
        self._PanSpecNorm.addItem("")
        self._PanSpecNorm.setObjectName(u"_PanSpecNorm")

        self.gridLayout_5.addWidget(self._PanSpecNorm, 0, 2, 1, 1)

        self.label_75 = QLabel(self._PanSpecNormW)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font1)

        self.gridLayout_5.addWidget(self.label_75, 0, 0, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_27, 1, 2, 1, 1)


        self.gridLayout_12.addWidget(self._PanSpecNormW, 4, 0, 1, 3)


        self.gridLayout_4.addLayout(self.gridLayout_12, 3, 2, 1, 1)


        self.verticalLayout_35.addLayout(self.gridLayout_4)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_10)

        self._PanSpecApply = QPushButton(self._spec_page)
        self._PanSpecApply.setObjectName(u"_PanSpecApply")

        self.horizontalLayout_25.addWidget(self._PanSpecApply)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_11)


        self.verticalLayout_35.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_15)

        self._stacked_panels.addWidget(self._spec_page)
        self._hyp_page = QWidget()
        self._hyp_page.setObjectName(u"_hyp_page")
        self.verticalLayout_36 = QVBoxLayout(self._hyp_page)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_81 = QLabel(self._hyp_page)
        self.label_81.setObjectName(u"label_81")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy1)
        self.label_81.setFont(font1)
        self.label_81.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.label_81, 0, 0, 1, 1)

        self.line_40 = QFrame(self._hyp_page)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setMinimumSize(QSize(10, 0))
        self.line_40.setFrameShape(QFrame.Shape.VLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_25.addWidget(self.line_40, 0, 1, 1, 1)

        self._PanHypnoLw = QDoubleSpinBox(self._hyp_page)
        self._PanHypnoLw.setObjectName(u"_PanHypnoLw")
        self._PanHypnoLw.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self._PanHypnoLw.sizePolicy().hasHeightForWidth())
        self._PanHypnoLw.setSizePolicy(sizePolicy2)
        self._PanHypnoLw.setDecimals(0)
        self._PanHypnoLw.setMinimum(1.000000000000000)
        self._PanHypnoLw.setMaximum(9.000000000000000)
        self._PanHypnoLw.setSingleStep(1.000000000000000)
        self._PanHypnoLw.setValue(2.000000000000000)

        self.gridLayout_25.addWidget(self._PanHypnoLw, 0, 2, 1, 1)

        self._PanHypnoColor = QCheckBox(self._hyp_page)
        self._PanHypnoColor.setObjectName(u"_PanHypnoColor")
        self._PanHypnoColor.setChecked(True)

        self.gridLayout_25.addWidget(self._PanHypnoColor, 1, 0, 1, 3)


        self.verticalLayout_36.addLayout(self.gridLayout_25)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_45)

        self._PanHypnoReset = QPushButton(self._hyp_page)
        self._PanHypnoReset.setObjectName(u"_PanHypnoReset")

        self.horizontalLayout_6.addWidget(self._PanHypnoReset)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_46)


        self.verticalLayout_36.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_16)

        self._stacked_panels.addWidget(self._hyp_page)
        self._topo_page = QWidget()
        self._topo_page.setObjectName(u"_topo_page")
        self.verticalLayout_37 = QVBoxLayout(self._topo_page)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setVerticalSpacing(9)
        self.line_27 = QFrame(self._topo_page)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setMinimumSize(QSize(10, 0))
        self.line_27.setFrameShape(QFrame.Shape.VLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_19.addWidget(self.line_27, 1, 1, 1, 1)

        self.line_20 = QFrame(self._topo_page)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setMinimumSize(QSize(10, 0))
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_19.addWidget(self.line_20, 2, 1, 3, 1)

        self._PanTopoAutoClim = QCheckBox(self._topo_page)
        self._PanTopoAutoClim.setObjectName(u"_PanTopoAutoClim")
        self._PanTopoAutoClim.setChecked(True)

        self.gridLayout_19.addWidget(self._PanTopoAutoClim, 2, 2, 1, 6)

        self._PanTopoClimW = QWidget(self._topo_page)
        self._PanTopoClimW.setObjectName(u"_PanTopoClimW")
        self._PanTopoClimW.setMinimumSize(QSize(30, 0))
        self.horizontalLayout_18 = QHBoxLayout(self._PanTopoClimW)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self._PanTopoClimW)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_18.addWidget(self.label_66)

        self._PanTopoCmin = QDoubleSpinBox(self._PanTopoClimW)
        self._PanTopoCmin.setObjectName(u"_PanTopoCmin")
        self._PanTopoCmin.setDecimals(2)
        self._PanTopoCmin.setMinimum(-1000000.000000000000000)
        self._PanTopoCmin.setMaximum(1000000.000000000000000)
        self._PanTopoCmin.setValue(-1.000000000000000)

        self.horizontalLayout_18.addWidget(self._PanTopoCmin)

        self._PanTopoCmax = QDoubleSpinBox(self._PanTopoClimW)
        self._PanTopoCmax.setObjectName(u"_PanTopoCmax")
        self._PanTopoCmax.setDecimals(2)
        self._PanTopoCmax.setMinimum(-1000000.000000000000000)
        self._PanTopoCmax.setMaximum(1000000.000000000000000)
        self._PanTopoCmax.setValue(1.000000000000000)

        self.horizontalLayout_18.addWidget(self._PanTopoCmax)


        self.gridLayout_19.addWidget(self._PanTopoClimW, 3, 2, 1, 6)

        self.label_63 = QLabel(self._topo_page)
        self.label_63.setObjectName(u"label_63")
        font2 = QFont()
        font2.setItalic(True)
        font2.setUnderline(False)
        self.label_63.setFont(font2)

        self.gridLayout_19.addWidget(self.label_63, 2, 0, 3, 1)

        self.widget_9 = QWidget(self._topo_page)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_32 = QVBoxLayout(self.widget_9)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self._PanTopoFW = QWidget(self.widget_9)
        self._PanTopoFW.setObjectName(u"_PanTopoFW")
        self._PanTopoFW.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_16 = QHBoxLayout(self._PanTopoFW)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self._PanTopoFW)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_16.addWidget(self.label_69)

        self._PanTopoFmin = QDoubleSpinBox(self._PanTopoFW)
        self._PanTopoFmin.setObjectName(u"_PanTopoFmin")
        self._PanTopoFmin.setDecimals(1)
        self._PanTopoFmin.setValue(12.000000000000000)

        self.horizontalLayout_16.addWidget(self._PanTopoFmin)

        self.horizontalSpacer_19 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_19)

        self.label_70 = QLabel(self._PanTopoFW)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_16.addWidget(self.label_70)

        self._PanTopoFmax = QDoubleSpinBox(self._PanTopoFW)
        self._PanTopoFmax.setObjectName(u"_PanTopoFmax")
        self._PanTopoFmax.setDecimals(1)
        self._PanTopoFmax.setValue(16.000000000000000)

        self.horizontalLayout_16.addWidget(self._PanTopoFmax)


        self.gridLayout_20.addWidget(self._PanTopoFW, 1, 0, 1, 2)

        self._PanTopoDisp = QComboBox(self.widget_9)
        self._PanTopoDisp.addItem("")
        self._PanTopoDisp.addItem("")
        self._PanTopoDisp.addItem("")
        self._PanTopoDisp.setObjectName(u"_PanTopoDisp")

        self.gridLayout_20.addWidget(self._PanTopoDisp, 0, 0, 1, 2)


        self.verticalLayout_32.addLayout(self.gridLayout_20)


        self.gridLayout_19.addWidget(self.widget_9, 1, 2, 1, 6)

        self.label_65 = QLabel(self._topo_page)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font1)

        self.gridLayout_19.addWidget(self.label_65, 1, 0, 1, 1)

        self.label_67 = QLabel(self._topo_page)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_19.addWidget(self.label_67, 4, 2, 1, 1)

        self._PanTopoRev = QCheckBox(self._topo_page)
        self._PanTopoRev.setObjectName(u"_PanTopoRev")
        self._PanTopoRev.setChecked(True)

        self.gridLayout_19.addWidget(self._PanTopoRev, 4, 7, 1, 1)

        self._PanTopoCmap = QComboBox(self._topo_page)
        self._PanTopoCmap.setObjectName(u"_PanTopoCmap")

        self.gridLayout_19.addWidget(self._PanTopoCmap, 4, 3, 1, 4)


        self.verticalLayout_37.addLayout(self.gridLayout_19)

        self._PanTopoVizW = QWidget(self._topo_page)
        self._PanTopoVizW.setObjectName(u"_PanTopoVizW")
        self._PanTopoVizW.setEnabled(False)
        self._PanTopoVizW.setMinimumSize(QSize(0, 0))
        self.verticalLayout_41 = QVBoxLayout(self._PanTopoVizW)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self._PanTopoVizW)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_24)

        self._PanTopoApply = QPushButton(self.widget_10)
        self._PanTopoApply.setObjectName(u"_PanTopoApply")

        self.horizontalLayout_17.addWidget(self._PanTopoApply)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_31)


        self.verticalLayout_41.addWidget(self.widget_10)


        self.verticalLayout_37.addWidget(self._PanTopoVizW)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_17)

        self._stacked_panels.addWidget(self._topo_page)
        self._PanTopoVizW.raise_()

        self.verticalLayout.addWidget(self._stacked_panels)

        self.QuickSettings.addTab(self.q_Panels, "")
        self.q_Tools = QWidget()
        self.q_Tools.setObjectName(u"q_Tools")
        self.verticalLayout_6 = QVBoxLayout(self.q_Tools)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.q_Tools)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_2)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.line_39 = QFrame(self.frame_2)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setMinimumSize(QSize(10, 0))
        self.line_39.setFrameShape(QFrame.Shape.VLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_26.addWidget(self.line_39, 0, 1, 1, 1)

        self.label_78 = QLabel(self.frame_2)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font1)

        self.gridLayout_26.addWidget(self.label_78, 0, 0, 1, 1)

        self._tool_pick = QComboBox(self.frame_2)
        self._tool_pick.addItem("")
        self._tool_pick.addItem("")
        self._tool_pick.setObjectName(u"_tool_pick")

        self.gridLayout_26.addWidget(self._tool_pick, 0, 2, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_47, 1, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_2)

        self._stacked_tools = QStackedWidget(self.q_Tools)
        self._stacked_tools.setObjectName(u"_stacked_tools")
        self._stacked_tools.setFocusPolicy(Qt.StrongFocus)
        self._sigproc_page = QWidget()
        self._sigproc_page.setObjectName(u"_sigproc_page")
        self.verticalLayout_25 = QVBoxLayout(self._sigproc_page)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.label_76 = QLabel(self._sigproc_page)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font1)

        self.gridLayout_14.addWidget(self.label_76, 0, 0, 1, 1)

        self.line_36 = QFrame(self._sigproc_page)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setMinimumSize(QSize(10, 0))
        self.line_36.setFrameShape(QFrame.Shape.VLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_14.addWidget(self.line_36, 0, 1, 1, 1)

        self._SigFiltChan = QComboBox(self._sigproc_page)
        self._SigFiltChan.addItem("")
        self._SigFiltChan.setObjectName(u"_SigFiltChan")

        self.gridLayout_14.addWidget(self._SigFiltChan, 0, 2, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_43, 1, 2, 1, 1)


        self.verticalLayout_25.addLayout(self.gridLayout_14)

        self.groupBox_5 = QGroupBox(self._sigproc_page)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.line_12 = QFrame(self.groupBox_5)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_12)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self._SigMean = QCheckBox(self.groupBox_5)
        self._SigMean.setObjectName(u"_SigMean")

        self.gridLayout_2.addWidget(self._SigMean, 0, 0, 1, 1)

        self._SigTrend = QCheckBox(self.groupBox_5)
        self._SigTrend.setObjectName(u"_SigTrend")

        self.gridLayout_2.addWidget(self._SigTrend, 0, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_2)


        self.verticalLayout_25.addWidget(self.groupBox_5)

        self._SigFilt = QGroupBox(self._sigproc_page)
        self._SigFilt.setObjectName(u"_SigFilt")
        self._SigFilt.setCheckable(True)
        self._SigFilt.setChecked(False)
        self.verticalLayout_8 = QVBoxLayout(self._SigFilt)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.line_11 = QFrame(self._SigFilt)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_11)

        self._SigFiltW = QWidget(self._SigFilt)
        self._SigFiltW.setObjectName(u"_SigFiltW")
        self._SigFiltW.setEnabled(False)
        self.verticalLayout_9 = QVBoxLayout(self._SigFiltW)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self._SigFiltDisp = QComboBox(self._SigFiltW)
        self._SigFiltDisp.addItem("")
        self._SigFiltDisp.addItem("")
        self._SigFiltDisp.addItem("")
        self._SigFiltDisp.addItem("")
        self._SigFiltDisp.setObjectName(u"_SigFiltDisp")

        self.gridLayout_3.addWidget(self._SigFiltDisp, 0, 2, 1, 1)

        self.label_18 = QLabel(self._SigFiltW)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)

        self.label_7 = QLabel(self._SigFiltW)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.line_24 = QFrame(self._SigFiltW)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setMinimumSize(QSize(10, 0))
        self.line_24.setFrameShape(QFrame.Shape.VLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_24, 2, 1, 1, 1)

        self.line_23 = QFrame(self._SigFiltW)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setMinimumSize(QSize(10, 0))
        self.line_23.setFrameShape(QFrame.Shape.VLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_23, 1, 1, 1, 1)

        self.label_68 = QLabel(self._SigFiltW)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font1)

        self.gridLayout_3.addWidget(self.label_68, 0, 0, 1, 1)

        self.line_26 = QFrame(self._SigFiltW)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setMinimumSize(QSize(10, 0))
        self.line_26.setFrameShape(QFrame.Shape.VLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_26, 0, 1, 1, 1)

        self.label_58 = QLabel(self._SigFiltW)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font1)

        self.gridLayout_3.addWidget(self.label_58, 3, 0, 1, 1)

        self.horizontalSpacer_40 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_40, 4, 2, 1, 1)

        self.widget_5 = QWidget(self._SigFiltW)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 6, -1, -1)
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_22)

        self._SigFiltApply = QPushButton(self.widget_5)
        self._SigFiltApply.setObjectName(u"_SigFiltApply")

        self.horizontalLayout_12.addWidget(self._SigFiltApply)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_23)


        self.gridLayout_3.addWidget(self.widget_5, 5, 0, 1, 3)

        self._SigFiltBand = QComboBox(self._SigFiltW)
        self._SigFiltBand.addItem("")
        self._SigFiltBand.addItem("")
        self._SigFiltBand.addItem("")
        self._SigFiltBand.addItem("")
        self._SigFiltBand.setObjectName(u"_SigFiltBand")

        self.gridLayout_3.addWidget(self._SigFiltBand, 1, 2, 1, 1)

        self.widget_4 = QWidget(self._SigFiltW)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self._SigFiltFrom = QDoubleSpinBox(self.widget_4)
        self._SigFiltFrom.setObjectName(u"_SigFiltFrom")
        self._SigFiltFrom.setDecimals(1)
        self._SigFiltFrom.setMinimum(0.100000000000000)
        self._SigFiltFrom.setMaximum(200.000000000000000)
        self._SigFiltFrom.setValue(12.000000000000000)

        self.horizontalLayout_5.addWidget(self._SigFiltFrom)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)

        self._SigFiltTo = QDoubleSpinBox(self.widget_4)
        self._SigFiltTo.setObjectName(u"_SigFiltTo")
        self._SigFiltTo.setDecimals(1)
        self._SigFiltTo.setMinimum(0.100000000000000)
        self._SigFiltTo.setMaximum(200.000000000000000)
        self._SigFiltTo.setValue(16.000000000000000)

        self.horizontalLayout_5.addWidget(self._SigFiltTo)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)


        self.gridLayout_3.addWidget(self.widget_4, 2, 2, 1, 1)

        self.line_25 = QFrame(self._SigFiltW)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setMinimumSize(QSize(10, 0))
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_25, 3, 1, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.label_10 = QLabel(self._SigFiltW)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_11 = QLabel(self._SigFiltW)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_10.addWidget(self.label_11, 1, 0, 1, 1)

        self._SigFiltOrder = QSpinBox(self._SigFiltW)
        self._SigFiltOrder.setObjectName(u"_SigFiltOrder")
        self._SigFiltOrder.setMinimum(1)
        self._SigFiltOrder.setMaximum(20)
        self._SigFiltOrder.setValue(3)

        self.gridLayout_10.addWidget(self._SigFiltOrder, 1, 1, 1, 1)

        self._SigFiltMeth = QComboBox(self._SigFiltW)
        self._SigFiltMeth.addItem("")
        self._SigFiltMeth.addItem("")
        self._SigFiltMeth.setObjectName(u"_SigFiltMeth")

        self.gridLayout_10.addWidget(self._SigFiltMeth, 0, 1, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_41, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_10, 3, 2, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_3)


        self.verticalLayout_8.addWidget(self._SigFiltW)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.verticalLayout_25.addWidget(self._SigFilt)

        self._stacked_tools.addWidget(self._sigproc_page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_30 = QVBoxLayout(self.page_4)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_6 = QFrame(self.page_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_59 = QLabel(self.frame_6)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font1)
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_59)


        self.verticalLayout_30.addWidget(self.frame_6)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(-1, 0, -1, -1)
        self._ToolsRefIgnore = QCheckBox(self.page_4)
        self._ToolsRefIgnore.setObjectName(u"_ToolsRefIgnore")
        self._ToolsRefIgnore.setChecked(True)

        self.gridLayout_22.addWidget(self._ToolsRefIgnore, 2, 3, 1, 2)

        self._ToolsRefSingleW = QWidget(self.page_4)
        self._ToolsRefSingleW.setObjectName(u"_ToolsRefSingleW")
        self._ToolsRefSingleW.setMinimumSize(QSize(0, 30))
        self.gridLayout_16 = QGridLayout(self._ToolsRefSingleW)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self._ToolsRefSingleW)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_16.addWidget(self.label_56, 0, 0, 1, 1)

        self._ToolsRefLst = QComboBox(self._ToolsRefSingleW)
        self._ToolsRefLst.setObjectName(u"_ToolsRefLst")

        self.gridLayout_16.addWidget(self._ToolsRefLst, 0, 2, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_30, 0, 1, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_25, 0, 3, 1, 1)


        self.gridLayout_22.addWidget(self._ToolsRefSingleW, 1, 3, 1, 2)

        self.line_6 = QFrame(self.page_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(10, 0))
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_22.addWidget(self.line_6, 0, 1, 1, 1)

        self.label_60 = QLabel(self.page_4)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font1)

        self.gridLayout_22.addWidget(self.label_60, 0, 0, 1, 1)

        self.label_61 = QLabel(self.page_4)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font1)

        self.gridLayout_22.addWidget(self.label_61, 1, 0, 3, 1)

        self.line_21 = QFrame(self.page_4)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setMinimumSize(QSize(10, 0))
        self.line_21.setFrameShape(QFrame.Shape.VLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_22.addWidget(self.line_21, 1, 1, 3, 1)

        self._ToolsRefIgn = QCheckBox(self.page_4)
        self._ToolsRefIgn.setObjectName(u"_ToolsRefIgn")

        self.gridLayout_22.addWidget(self._ToolsRefIgn, 3, 3, 1, 2)

        self._ToolsRefMeth = QComboBox(self.page_4)
        self._ToolsRefMeth.addItem("")
        self._ToolsRefMeth.addItem("")
        self._ToolsRefMeth.addItem("")
        self._ToolsRefMeth.setObjectName(u"_ToolsRefMeth")

        self.gridLayout_22.addWidget(self._ToolsRefMeth, 0, 2, 1, 3)


        self.verticalLayout_30.addLayout(self.gridLayout_22)

        self._ToolsRefGrp = QWidget(self.page_4)
        self._ToolsRefGrp.setObjectName(u"_ToolsRefGrp")
        self._ToolsRefGrp.setMinimumSize(QSize(0, 30))
        self.verticalLayout_18 = QVBoxLayout(self._ToolsRefGrp)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self._ToolsRefIgnArea = QScrollArea(self._ToolsRefGrp)
        self._ToolsRefIgnArea.setObjectName(u"_ToolsRefIgnArea")
        self._ToolsRefIgnArea.setMinimumSize(QSize(0, 300))
        self._ToolsRefIgnArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 298))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self._ToolsRefIgnGrd = QGridLayout()
        self._ToolsRefIgnGrd.setObjectName(u"_ToolsRefIgnGrd")

        self.verticalLayout_2.addLayout(self._ToolsRefIgnGrd)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self._ToolsRefIgnArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_18.addWidget(self._ToolsRefIgnArea)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 9, -1, -1)
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_20)

        self._ToolsRefApply = QPushButton(self._ToolsRefGrp)
        self._ToolsRefApply.setObjectName(u"_ToolsRefApply")

        self.horizontalLayout_9.addWidget(self._ToolsRefApply)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_21)


        self.verticalLayout_18.addLayout(self.horizontalLayout_9)


        self.verticalLayout_30.addWidget(self._ToolsRefGrp)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_4)

        self._stacked_tools.addWidget(self.page_4)
        self.frame_6.raise_()
        self._ToolsRefGrp.raise_()

        self.verticalLayout_6.addWidget(self._stacked_tools)

        self.QuickSettings.addTab(self.q_Tools, "")
        self.q_Info = QWidget()
        self.q_Info.setObjectName(u"q_Info")
        self.verticalLayout_3 = QVBoxLayout(self.q_Info)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self._infoTable = QTableWidget(self.q_Info)
        if (self._infoTable.columnCount() < 2):
            self._infoTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self._infoTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self._infoTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self._infoTable.setObjectName(u"_infoTable")
        self._infoTable.horizontalHeader().setStretchLastSection(True)
        self._infoTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self._infoTable)

        self.QuickSettings.addTab(self.q_Info, "")
        self.q_Score = QWidget()
        self.q_Score.setObjectName(u"q_Score")
        self.verticalLayout_29 = QVBoxLayout(self.q_Score)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self._scoreTable = QTableWidget(self.q_Score)
        if (self._scoreTable.columnCount() < 3):
            self._scoreTable.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self._scoreTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self._scoreTable.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self._scoreTable.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self._scoreTable.setObjectName(u"_scoreTable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self._scoreTable.sizePolicy().hasHeightForWidth())
        self._scoreTable.setSizePolicy(sizePolicy3)
        self._scoreTable.setSortingEnabled(True)
        self._scoreTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_29.addWidget(self._scoreTable)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_32)

        self._scoreAdd = QPushButton(self.q_Score)
        self._scoreAdd.setObjectName(u"_scoreAdd")

        self.horizontalLayout_13.addWidget(self._scoreAdd)

        self.horizontalSpacer_35 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_35)

        self._scoreRm = QPushButton(self.q_Score)
        self._scoreRm.setObjectName(u"_scoreRm")

        self.horizontalLayout_13.addWidget(self._scoreRm)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_36)


        self.verticalLayout_29.addLayout(self.horizontalLayout_13)

        self.QuickSettings.addTab(self.q_Score, "")
        self.q_Detection = QWidget()
        self.q_Detection.setObjectName(u"q_Detection")
        self.verticalLayout_22 = QVBoxLayout(self.q_Detection)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self._DetectionTab = QTabWidget(self.q_Detection)
        self._DetectionTab.setObjectName(u"_DetectionTab")
        self.q_DetectSettings = QWidget()
        self.q_DetectSettings.setObjectName(u"q_DetectSettings")
        self.verticalLayout_38 = QVBoxLayout(self.q_DetectSettings)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.groupBox_3 = QGroupBox(self.q_DetectSettings)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_33 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, -1, 0, -1)
        self.line_3 = QFrame(self.groupBox_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_33.addWidget(self.line_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_39 = QLabel(self.groupBox_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.gridLayout.addWidget(self.label_39, 0, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 2, 3, 1, 1)

        self._ToolDetectType = QComboBox(self.groupBox_3)
        self._ToolDetectType.addItem("")
        self._ToolDetectType.addItem("")
        self._ToolDetectType.addItem("")
        self._ToolDetectType.addItem("")
        self._ToolDetectType.addItem("")
        self._ToolDetectType.addItem("")
        self._ToolDetectType.setObjectName(u"_ToolDetectType")

        self.gridLayout.addWidget(self._ToolDetectType, 0, 3, 1, 3)

        self.line_9 = QFrame(self.groupBox_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMinimumSize(QSize(10, 0))
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 1, 2, 3, 1)

        self._ToolRdViz = QRadioButton(self.groupBox_3)
        self._ToolRdViz.setObjectName(u"_ToolRdViz")

        self.gridLayout.addWidget(self._ToolRdViz, 1, 4, 1, 1)

        self.line_10 = QFrame(self.groupBox_3)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMinimumSize(QSize(10, 0))
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_10, 0, 2, 1, 1)

        self.label_49 = QLabel(self.groupBox_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font1)

        self.gridLayout.addWidget(self.label_49, 1, 1, 3, 1)

        self._ToolRdSelected = QRadioButton(self.groupBox_3)
        self._ToolRdSelected.setObjectName(u"_ToolRdSelected")
        self._ToolRdSelected.setChecked(True)

        self.gridLayout.addWidget(self._ToolRdSelected, 1, 3, 1, 1)

        self._ToolRdAll = QRadioButton(self.groupBox_3)
        self._ToolRdAll.setObjectName(u"_ToolRdAll")

        self.gridLayout.addWidget(self._ToolRdAll, 1, 5, 1, 1)

        self._ToolDetectChan = QComboBox(self.groupBox_3)
        self._ToolDetectChan.setObjectName(u"_ToolDetectChan")

        self.gridLayout.addWidget(self._ToolDetectChan, 2, 4, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_28, 2, 5, 1, 1)


        self.verticalLayout_33.addLayout(self.gridLayout)


        self.verticalLayout_38.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.q_DetectSettings)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, -1, 0, -1)
        self.line_4 = QFrame(self.groupBox_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_26.addWidget(self.line_4)

        self._stacked_detections = QStackedWidget(self.groupBox_2)
        self._stacked_detections.setObjectName(u"_stacked_detections")
        self._stacked_detections.setFocusPolicy(Qt.StrongFocus)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self._stacked_detections.sizePolicy().hasHeightForWidth())
        self._stacked_detections.setSizePolicy(sizePolicy4)
        self._spin_page = QWidget()
        self._spin_page.setObjectName(u"_spin_page")
        self.verticalLayout_19 = QVBoxLayout(self._spin_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.label_40 = QLabel(self._spin_page)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_18.addWidget(self.label_40, 2, 2, 1, 1)

        self._ToolSpinTmin = QDoubleSpinBox(self._spin_page)
        self._ToolSpinTmin.setObjectName(u"_ToolSpinTmin")
        self._ToolSpinTmin.setDecimals(1)
        self._ToolSpinTmin.setMaximum(10000.000000000000000)
        self._ToolSpinTmin.setValue(500.000000000000000)

        self.gridLayout_18.addWidget(self._ToolSpinTmin, 1, 3, 1, 1)

        self.label_37 = QLabel(self._spin_page)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_18.addWidget(self.label_37, 1, 6, 1, 1)

        self._ToolSpinRemOnly = QCheckBox(self._spin_page)
        self._ToolSpinRemOnly.setObjectName(u"_ToolSpinRemOnly")

        self.gridLayout_18.addWidget(self._ToolSpinRemOnly, 3, 2, 1, 5)

        self._ToolSpinFmin = QDoubleSpinBox(self._spin_page)
        self._ToolSpinFmin.setObjectName(u"_ToolSpinFmin")
        self._ToolSpinFmin.setDecimals(1)
        self._ToolSpinFmin.setMaximum(200.000000000000000)
        self._ToolSpinFmin.setValue(12.000000000000000)

        self.gridLayout_18.addWidget(self._ToolSpinFmin, 0, 3, 1, 1)

        self.line_5 = QFrame(self._spin_page)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(10, 0))
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_18.addWidget(self.line_5, 0, 1, 4, 1)

        self.label_30 = QLabel(self._spin_page)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_18.addWidget(self.label_30, 1, 4, 1, 1)

        self.label_22 = QLabel(self._spin_page)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_18.addWidget(self.label_22, 1, 2, 1, 1)

        self.label_19 = QLabel(self._spin_page)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_18.addWidget(self.label_19, 0, 2, 1, 1)

        self._ToolSpinFmax = QDoubleSpinBox(self._spin_page)
        self._ToolSpinFmax.setObjectName(u"_ToolSpinFmax")
        self._ToolSpinFmax.setDecimals(1)
        self._ToolSpinFmax.setMaximum(200.000000000000000)
        self._ToolSpinFmax.setValue(14.000000000000000)

        self.gridLayout_18.addWidget(self._ToolSpinFmax, 0, 5, 1, 1)

        self.label_21 = QLabel(self._spin_page)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_18.addWidget(self.label_21, 0, 6, 1, 1)

        self.label_52 = QLabel(self._spin_page)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font1)
        self.label_52.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_18.addWidget(self.label_52, 0, 0, 4, 1)

        self._ToolSpinTmax = QDoubleSpinBox(self._spin_page)
        self._ToolSpinTmax.setObjectName(u"_ToolSpinTmax")
        self._ToolSpinTmax.setDecimals(1)
        self._ToolSpinTmax.setMaximum(10000.000000000000000)
        self._ToolSpinTmax.setValue(2000.000000000000000)

        self.gridLayout_18.addWidget(self._ToolSpinTmax, 1, 5, 1, 1)

        self.label_20 = QLabel(self._spin_page)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_18.addWidget(self.label_20, 0, 4, 1, 1)

        self._ToolSpinTh = QDoubleSpinBox(self._spin_page)
        self._ToolSpinTh.setObjectName(u"_ToolSpinTh")
        self._ToolSpinTh.setDecimals(1)
        self._ToolSpinTh.setValue(2.000000000000000)

        self.gridLayout_18.addWidget(self._ToolSpinTh, 2, 3, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_18)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_10)

        self._stacked_detections.addWidget(self._spin_page)
        self._rem_page = QWidget()
        self._rem_page.setObjectName(u"_rem_page")
        self.verticalLayout_20 = QVBoxLayout(self._rem_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(-1, 0, -1, -1)
        self._ToolRemTh = QDoubleSpinBox(self._rem_page)
        self._ToolRemTh.setObjectName(u"_ToolRemTh")
        self._ToolRemTh.setDecimals(1)
        self._ToolRemTh.setValue(3.000000000000000)

        self.gridLayout_17.addWidget(self._ToolRemTh, 0, 3, 1, 1)

        self.label_38 = QLabel(self._rem_page)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_17.addWidget(self.label_38, 0, 2, 1, 1)

        self._ToolRemOnly = QCheckBox(self._rem_page)
        self._ToolRemOnly.setObjectName(u"_ToolRemOnly")

        self.gridLayout_17.addWidget(self._ToolRemOnly, 1, 2, 1, 4)

        self.line_2 = QFrame(self._rem_page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(10, 0))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_17.addWidget(self.line_2, 0, 1, 2, 1)

        self.label_51 = QLabel(self._rem_page)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font1)

        self.gridLayout_17.addWidget(self.label_51, 0, 0, 2, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_39, 0, 4, 1, 1)


        self.verticalLayout_20.addLayout(self.gridLayout_17)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_9)

        self._stacked_detections.addWidget(self._rem_page)
        self._kcomp_page = QWidget()
        self._kcomp_page.setObjectName(u"_kcomp_page")
        self.verticalLayout_23 = QVBoxLayout(self._kcomp_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(9)
        self.gridLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.widget_8 = QWidget(self._kcomp_page)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.widget_8)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_15.addWidget(self.label_64)

        self._ToolKCMinAmp = QDoubleSpinBox(self.widget_8)
        self._ToolKCMinAmp.setObjectName(u"_ToolKCMinAmp")
        self._ToolKCMinAmp.setDecimals(1)
        self._ToolKCMinAmp.setMinimum(10.000000000000000)
        self._ToolKCMinAmp.setMaximum(500.000000000000000)
        self._ToolKCMinAmp.setSingleStep(10.000000000000000)
        self._ToolKCMinAmp.setValue(80.000000000000000)

        self.horizontalLayout_15.addWidget(self._ToolKCMinAmp)

        self._ToolKCMaxAmp = QDoubleSpinBox(self.widget_8)
        self._ToolKCMaxAmp.setObjectName(u"_ToolKCMaxAmp")
        self._ToolKCMaxAmp.setDecimals(1)
        self._ToolKCMaxAmp.setMinimum(110.000000000000000)
        self._ToolKCMaxAmp.setMaximum(1000.000000000000000)
        self._ToolKCMaxAmp.setSingleStep(10.000000000000000)
        self._ToolKCMaxAmp.setValue(600.000000000000000)

        self.horizontalLayout_15.addWidget(self._ToolKCMaxAmp)


        self.gridLayout_8.addWidget(self.widget_8, 4, 2, 1, 4)

        self.label_57 = QLabel(self._kcomp_page)
        self.label_57.setObjectName(u"label_57")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy5)

        self.gridLayout_8.addWidget(self.label_57, 0, 2, 2, 2)

        self.kc_label = QLabel(self._kcomp_page)
        self.kc_label.setObjectName(u"kc_label")
        self.kc_label.setFont(font1)

        self.gridLayout_8.addWidget(self.kc_label, 0, 0, 6, 1)

        self._ToolKCNremOnly = QCheckBox(self._kcomp_page)
        self._ToolKCNremOnly.setObjectName(u"_ToolKCNremOnly")

        self.gridLayout_8.addWidget(self._ToolKCNremOnly, 5, 2, 1, 4)

        self._ToolKCProbTh = QDoubleSpinBox(self._kcomp_page)
        self._ToolKCProbTh.setObjectName(u"_ToolKCProbTh")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self._ToolKCProbTh.sizePolicy().hasHeightForWidth())
        self._ToolKCProbTh.setSizePolicy(sizePolicy6)
        self._ToolKCProbTh.setMaximum(1.000000000000000)
        self._ToolKCProbTh.setSingleStep(0.100000000000000)
        self._ToolKCProbTh.setValue(0.700000000000000)

        self.gridLayout_8.addWidget(self._ToolKCProbTh, 0, 4, 2, 2)

        self.line_19 = QFrame(self._kcomp_page)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setMinimumSize(QSize(10, 0))
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_8.addWidget(self.line_19, 0, 1, 6, 1)

        self.widget_7 = QWidget(self._kcomp_page)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.widget_7)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_14.addWidget(self.label_62)

        self._ToolKCMinDur = QDoubleSpinBox(self.widget_7)
        self._ToolKCMinDur.setObjectName(u"_ToolKCMinDur")
        self._ToolKCMinDur.setDecimals(1)
        self._ToolKCMinDur.setMaximum(1000.000000000000000)
        self._ToolKCMinDur.setSingleStep(50.000000000000000)
        self._ToolKCMinDur.setValue(400.000000000000000)

        self.horizontalLayout_14.addWidget(self._ToolKCMinDur)

        self._ToolKCMaxDur = QDoubleSpinBox(self.widget_7)
        self._ToolKCMaxDur.setObjectName(u"_ToolKCMaxDur")
        self._ToolKCMaxDur.setDecimals(1)
        self._ToolKCMaxDur.setMinimum(1000.000000000000000)
        self._ToolKCMaxDur.setMaximum(10000.000000000000000)
        self._ToolKCMaxDur.setSingleStep(100.000000000000000)
        self._ToolKCMaxDur.setValue(3000.000000000000000)

        self.horizontalLayout_14.addWidget(self._ToolKCMaxDur)


        self.gridLayout_8.addWidget(self.widget_7, 3, 2, 1, 4)

        self._ToolKCAmpTh = QDoubleSpinBox(self._kcomp_page)
        self._ToolKCAmpTh.setObjectName(u"_ToolKCAmpTh")
        self._ToolKCAmpTh.setMaximum(10.000000000000000)
        self._ToolKCAmpTh.setSingleStep(0.500000000000000)
        self._ToolKCAmpTh.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self._ToolKCAmpTh, 2, 4, 1, 2)

        self.label_71 = QLabel(self._kcomp_page)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_8.addWidget(self.label_71, 2, 2, 1, 2)


        self.verticalLayout_23.addLayout(self.gridLayout_8)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_11)

        self._stacked_detections.addWidget(self._kcomp_page)
        self._sw_page = QWidget()
        self._sw_page.setObjectName(u"_sw_page")
        self.verticalLayout_24 = QVBoxLayout(self._sw_page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_53 = QLabel(self._sw_page)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font1)

        self.gridLayout_9.addWidget(self.label_53, 0, 0, 2, 1)

        self._ToolWaveTh = QDoubleSpinBox(self._sw_page)
        self._ToolWaveTh.setObjectName(u"_ToolWaveTh")
        self._ToolWaveTh.setMaximum(1.000000000000000)
        self._ToolWaveTh.setSingleStep(0.050000000000000)
        self._ToolWaveTh.setValue(0.750000000000000)

        self.gridLayout_9.addWidget(self._ToolWaveTh, 0, 3, 2, 1)

        self.line_7 = QFrame(self._sw_page)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMinimumSize(QSize(10, 0))
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_7, 0, 1, 2, 1)

        self.label_46 = QLabel(self._sw_page)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_9.addWidget(self.label_46, 0, 2, 2, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 0, 4, 2, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_9)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_12)

        self._stacked_detections.addWidget(self._sw_page)
        self._mt_page = QWidget()
        self._mt_page.setObjectName(u"_mt_page")
        self.verticalLayout_27 = QVBoxLayout(self._mt_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(-1, 0, -1, -1)
        self._ToolMTTh = QDoubleSpinBox(self._mt_page)
        self._ToolMTTh.setObjectName(u"_ToolMTTh")
        self._ToolMTTh.setDecimals(1)
        self._ToolMTTh.setMaximum(20.000000000000000)
        self._ToolMTTh.setValue(3.000000000000000)

        self.gridLayout_29.addWidget(self._ToolMTTh, 0, 3, 1, 1)

        self.label_93 = QLabel(self._mt_page)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_29.addWidget(self.label_93, 0, 2, 1, 1)

        self._ToolMTOnly = QCheckBox(self._mt_page)
        self._ToolMTOnly.setObjectName(u"_ToolMTOnly")

        self.gridLayout_29.addWidget(self._ToolMTOnly, 1, 2, 1, 4)

        self.line_37 = QFrame(self._mt_page)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setMinimumSize(QSize(10, 0))
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_29.addWidget(self.line_37, 0, 1, 2, 1)

        self.label_94 = QLabel(self._mt_page)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font1)

        self.gridLayout_29.addWidget(self.label_94, 0, 0, 2, 1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_42, 0, 4, 1, 1)


        self.verticalLayout_27.addLayout(self.gridLayout_29)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_13)

        self._stacked_detections.addWidget(self._mt_page)
        self._peak_page = QWidget()
        self._peak_page.setObjectName(u"_peak_page")
        self.verticalLayout_43 = QVBoxLayout(self._peak_page)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.label_26 = QLabel(self._peak_page)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_11.addWidget(self.label_26, 0, 2, 1, 1)

        self._ToolPeakLook = QDoubleSpinBox(self._peak_page)
        self._ToolPeakLook.setObjectName(u"_ToolPeakLook")
        self._ToolPeakLook.setDecimals(1)
        self._ToolPeakLook.setValue(0.500000000000000)

        self.gridLayout_11.addWidget(self._ToolPeakLook, 0, 3, 1, 1)

        self.label_28 = QLabel(self._peak_page)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_11.addWidget(self.label_28, 1, 2, 1, 1)

        self.label_27 = QLabel(self._peak_page)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_11.addWidget(self.label_27, 0, 4, 1, 1)

        self._ToolPeakMinMax = QComboBox(self._peak_page)
        self._ToolPeakMinMax.addItem("")
        self._ToolPeakMinMax.addItem("")
        self._ToolPeakMinMax.addItem("")
        self._ToolPeakMinMax.setObjectName(u"_ToolPeakMinMax")

        self.gridLayout_11.addWidget(self._ToolPeakMinMax, 1, 3, 1, 2)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_38, 0, 5, 1, 1)

        self.label_50 = QLabel(self._peak_page)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font1)

        self.gridLayout_11.addWidget(self.label_50, 0, 0, 2, 1)

        self.line = QFrame(self._peak_page)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(10, 0))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line, 0, 1, 2, 1)


        self.verticalLayout_43.addLayout(self.gridLayout_11)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_14)

        self._stacked_detections.addWidget(self._peak_page)

        self.verticalLayout_26.addWidget(self._stacked_detections)


        self.verticalLayout_38.addWidget(self.groupBox_2)

        self._ToolDetectTable = QTableWidget(self.q_DetectSettings)
        if (self._ToolDetectTable.columnCount() < 2):
            self._ToolDetectTable.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self._ToolDetectTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self._ToolDetectTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self._ToolDetectTable.setObjectName(u"_ToolDetectTable")
        self._ToolDetectTable.setMaximumSize(QSize(16777215, 100))
        self._ToolDetectTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_38.addWidget(self._ToolDetectTable)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_26)

        self._ToolDetectApply = QPushButton(self.q_DetectSettings)
        self._ToolDetectApply.setObjectName(u"_ToolDetectApply")

        self.horizontalLayout_8.addWidget(self._ToolDetectApply)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_38.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_3)

        self._ToolDetectProgress = QProgressBar(self.q_DetectSettings)
        self._ToolDetectProgress.setObjectName(u"_ToolDetectProgress")
        self._ToolDetectProgress.setValue(0)
        self._ToolDetectProgress.setInvertedAppearance(False)

        self.verticalLayout_38.addWidget(self._ToolDetectProgress)

        self._DetectionTab.addTab(self.q_DetectSettings, "")
        self.q_DetectLoc = QWidget()
        self.q_DetectLoc.setObjectName(u"q_DetectLoc")
        self.verticalLayout_39 = QVBoxLayout(self.q_DetectLoc)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setSpacing(3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(9, 0, -1, 0)
        self.label_72 = QLabel(self.q_DetectLoc)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font1)

        self.gridLayout_23.addWidget(self.label_72, 0, 0, 3, 1)

        self.line_28 = QFrame(self.q_DetectLoc)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setMinimumSize(QSize(10, 0))
        self.line_28.setFrameShape(QFrame.Shape.VLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_23.addWidget(self.line_28, 0, 1, 3, 1)

        self.widget_11 = QWidget(self.q_DetectLoc)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 3, -1, 3)
        self._DetectViz = QCheckBox(self.widget_11)
        self._DetectViz.setObjectName(u"_DetectViz")
        self._DetectViz.setChecked(True)
        self._DetectViz.setTristate(False)

        self.horizontalLayout_19.addWidget(self._DetectViz)

        self._DetectRm = QPushButton(self.widget_11)
        self._DetectRm.setObjectName(u"_DetectRm")

        self.horizontalLayout_19.addWidget(self._DetectRm)


        self.gridLayout_23.addWidget(self.widget_11, 2, 2, 1, 2)

        self.widget_12 = QWidget(self.q_DetectLoc)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)

        self.gridLayout_23.addWidget(self.widget_12, 3, 2, 1, 2)

        self.line_30 = QFrame(self.q_DetectLoc)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setMinimumSize(QSize(10, 0))
        self.line_30.setFrameShape(QFrame.Shape.VLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_23.addWidget(self.line_30, 3, 1, 1, 1)

        self._DetectChanSw = QComboBox(self.q_DetectLoc)
        self._DetectChanSw.setObjectName(u"_DetectChanSw")

        self.gridLayout_23.addWidget(self._DetectChanSw, 1, 2, 1, 2)


        self.verticalLayout_39.addLayout(self.gridLayout_23)

        self._DetectLocations = QTableWidget(self.q_DetectLoc)
        if (self._DetectLocations.columnCount() < 4):
            self._DetectLocations.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self._DetectLocations.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self._DetectLocations.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self._DetectLocations.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self._DetectLocations.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self._DetectLocations.setObjectName(u"_DetectLocations")
        self._DetectLocations.setDragDropMode(QAbstractItemView.InternalMove)
        self._DetectLocations.setAlternatingRowColors(True)
        self._DetectLocations.setSortingEnabled(True)
        self._DetectLocations.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_39.addWidget(self._DetectLocations)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_34)

        self._DetecRmEvent = QPushButton(self.q_DetectLoc)
        self._DetecRmEvent.setObjectName(u"_DetecRmEvent")

        self.horizontalLayout_20.addWidget(self._DetecRmEvent)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_37)


        self.verticalLayout_39.addLayout(self.horizontalLayout_20)

        self._DetectionTab.addTab(self.q_DetectLoc, "")

        self.verticalLayout_22.addWidget(self._DetectionTab)

        self.QuickSettings.addTab(self.q_Detection, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self._AnnotateTable = QTableWidget(self.tab)
        if (self._AnnotateTable.columnCount() < 3):
            self._AnnotateTable.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self._AnnotateTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self._AnnotateTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self._AnnotateTable.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        self._AnnotateTable.setObjectName(u"_AnnotateTable")
        self._AnnotateTable.setDragEnabled(True)
        self._AnnotateTable.setAlternatingRowColors(True)
        self._AnnotateTable.setSortingEnabled(True)
        self._AnnotateTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_11.addWidget(self._AnnotateTable)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self._AnnotateAdd = QPushButton(self.tab)
        self._AnnotateAdd.setObjectName(u"_AnnotateAdd")

        self.horizontalLayout_21.addWidget(self._AnnotateAdd)

        self._AnnotateRm = QPushButton(self.tab)
        self._AnnotateRm.setObjectName(u"_AnnotateRm")

        self.horizontalLayout_21.addWidget(self._AnnotateRm)


        self.verticalLayout_11.addLayout(self.horizontalLayout_21)

        self.QuickSettings.addTab(self.tab, "")

        self.verticalLayout_4.addWidget(self.QuickSettings)

        self.splitter.addWidget(self.q_widget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout_21 = QGridLayout(self.layoutWidget)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self._topoW = QWidget(self.layoutWidget)
        self._topoW.setObjectName(u"_topoW")
        self._topoW.setMinimumSize(QSize(250, 0))
        self._topoW.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_31 = QVBoxLayout(self._topoW)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self._topoLayout = QVBoxLayout()
        self._topoLayout.setObjectName(u"_topoLayout")
        self._topoLayout.setContentsMargins(-1, 0, -1, -1)
        self._topoTitle = QLabel(self._topoW)
        self._topoTitle.setObjectName(u"_topoTitle")
        self._topoTitle.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self._topoTitle.setFont(font3)
        self._topoTitle.setAlignment(Qt.AlignCenter)

        self._topoLayout.addWidget(self._topoTitle)


        self.verticalLayout_31.addLayout(self._topoLayout)


        self.gridLayout_21.addWidget(self._topoW, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_13, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_17)

        self._slFrame = QFrame(self.layoutWidget)
        self._slFrame.setObjectName(u"_slFrame")
        self._slFrame.setMinimumSize(QSize(0, 0))
        self._slFrame.setFrameShape(QFrame.StyledPanel)
        self._slFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self._slFrame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self._sliderPanel = QWidget(self._slFrame)
        self._sliderPanel.setObjectName(u"_sliderPanel")
        self._sliderPanelLayout = QVBoxLayout(self._sliderPanel)
        self._sliderPanelLayout.setSpacing(6)
        self._sliderPanelLayout.setObjectName(u"_sliderPanelLayout")
        self._sliderPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 3, -1, -1)
        self._txtCursor = QLabel(self._sliderPanel)
        self._txtCursor.setObjectName(u"_txtCursor")
        font4 = QFont()
        font4.setBold(True)
        self._txtCursor.setFont(font4)

        self.horizontalLayout_22.addWidget(self._txtCursor)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_18)

        self._SlText = QLabel(self._sliderPanel)
        self._SlText.setObjectName(u"_SlText")
        self._SlText.setAlignment(Qt.AlignCenter)
        self._SlText.setMargin(0)

        self.horizontalLayout_22.addWidget(self._SlText)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_33)

        self._AnnotateRun = QPushButton(self._sliderPanel)
        self._AnnotateRun.setObjectName(u"_AnnotateRun")

        self.horizontalLayout_22.addWidget(self._AnnotateRun)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_29)


        self._sliderPanelLayout.addLayout(self.horizontalLayout_22)

        self._SlVal = QSlider(self._sliderPanel)
        self._SlVal.setObjectName(u"_SlVal")
        self._SlVal.setOrientation(Qt.Horizontal)
        self._SlVal.setTickPosition(QSlider.NoTicks)
        self._SlVal.setTickInterval(10)

        self._sliderPanelLayout.addWidget(self._SlVal)

        self._sliderControls = QWidget(self._sliderPanel)
        self._sliderControls.setObjectName(u"_sliderControls")
        self._sliderControlsLayout = QGridLayout(self._sliderControls)
        self._sliderControlsLayout.setObjectName(u"_sliderControlsLayout")
        self._sliderControlsLayout.setHorizontalSpacing(12)
        self._sliderControlsLayout.setVerticalSpacing(4)
        self._sliderControlsLayout.setContentsMargins(0, 0, 0, 0)
        self._sliderGotoLayout = QHBoxLayout()
        self._sliderGotoLayout.setSpacing(6)
        self._sliderGotoLayout.setObjectName(u"_sliderGotoLayout")
        self._sliderGotoLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self._sliderControls)
        self.label.setObjectName(u"label")

        self._sliderGotoLayout.addWidget(self.label)

        self._SlGoto = QDoubleSpinBox(self._sliderControls)
        self._SlGoto.setObjectName(u"_SlGoto")
        self._SlGoto.setDecimals(1)

        self._sliderGotoLayout.addWidget(self._SlGoto)

        self.label_12 = QLabel(self._sliderControls)
        self.label_12.setObjectName(u"label_12")

        self._sliderGotoLayout.addWidget(self.label_12)


        self._sliderControlsLayout.addLayout(self._sliderGotoLayout, 0, 0, 1, 1)

        self._sliderWindowLayout = QHBoxLayout()
        self._sliderWindowLayout.setSpacing(6)
        self._sliderWindowLayout.setObjectName(u"_sliderWindowLayout")
        self._sliderWindowLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self._sliderControls)
        self.label_3.setObjectName(u"label_3")

        self._sliderWindowLayout.addWidget(self.label_3)

        self._SigWin = QDoubleSpinBox(self._sliderControls)
        self._SigWin.setObjectName(u"_SigWin")
        self._SigWin.setDecimals(1)
        self._SigWin.setMaximum(1000.000000000000000)
        self._SigWin.setValue(30.000000000000000)

        self._sliderWindowLayout.addWidget(self._SigWin)

        self.label_4 = QLabel(self._sliderControls)
        self.label_4.setObjectName(u"label_4")

        self._sliderWindowLayout.addWidget(self.label_4)


        self._sliderControlsLayout.addLayout(self._sliderWindowLayout, 0, 1, 1, 1)

        self._sliderScoringWindowLayout = QHBoxLayout()
        self._sliderScoringWindowLayout.setSpacing(6)
        self._sliderScoringWindowLayout.setObjectName(u"_sliderScoringWindowLayout")
        self._sliderScoringWindowLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3_1 = QLabel(self._sliderControls)
        self.label_3_1.setObjectName(u"label_3_1")

        self._sliderScoringWindowLayout.addWidget(self.label_3_1)

        self._ScorWin = QDoubleSpinBox(self._sliderControls)
        self._ScorWin.setObjectName(u"_ScorWin")
        self._ScorWin.setDecimals(1)
        self._ScorWin.setMinimum(0.100000000000000)
        self._ScorWin.setMaximum(1000.000000000000000)
        self._ScorWin.setValue(30.000000000000000)

        self._sliderScoringWindowLayout.addWidget(self._ScorWin)

        self.label_4_1 = QLabel(self._sliderControls)
        self.label_4_1.setObjectName(u"label_4_1")

        self._sliderScoringWindowLayout.addWidget(self.label_4_1)


        self._sliderControlsLayout.addLayout(self._sliderScoringWindowLayout, 0, 2, 1, 1)

        self._sliderStepLayout = QHBoxLayout()
        self._sliderStepLayout.setSpacing(6)
        self._sliderStepLayout.setObjectName(u"_sliderStepLayout")
        self._sliderStepLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self._sliderControls)
        self.label_5.setObjectName(u"label_5")

        self._sliderStepLayout.addWidget(self.label_5)

        self._SigSlStep = QDoubleSpinBox(self._sliderControls)
        self._SigSlStep.setObjectName(u"_SigSlStep")
        self._SigSlStep.setDecimals(1)
        self._SigSlStep.setMinimum(0.100000000000000)
        self._SigSlStep.setValue(30.000000000000000)

        self._sliderStepLayout.addWidget(self._SigSlStep)

        self.label_6 = QLabel(self._sliderControls)
        self.label_6.setObjectName(u"label_6")

        self._sliderStepLayout.addWidget(self.label_6)


        self._sliderControlsLayout.addLayout(self._sliderStepLayout, 0, 3, 1, 1)

        self._sliderRuleLayout = QHBoxLayout()
        self._sliderRuleLayout.setSpacing(6)
        self._sliderRuleLayout.setObjectName(u"_sliderRuleLayout")
        self._sliderRuleLayout.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self._sliderControls)
        self.label_31.setObjectName(u"label_31")

        self._sliderRuleLayout.addWidget(self.label_31)

        self._slRules = QComboBox(self._sliderControls)
        self._slRules.addItem("")
        self._slRules.addItem("")
        self._slRules.addItem("")
        self._slRules.setObjectName(u"_slRules")

        self._sliderRuleLayout.addWidget(self._slRules)


        self._sliderControlsLayout.addLayout(self._sliderRuleLayout, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._sliderControlsLayout.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)


        self._sliderPanelLayout.addWidget(self._sliderControls)

        self.horizontalLayout_22_1 = QHBoxLayout()
        self.horizontalLayout_22_1.setObjectName(u"horizontalLayout_22_1")
        self.horizontalLayout_22_1.setContentsMargins(-1, -1, -1, 3)
        self._slGrid = QCheckBox(self._sliderPanel)
        self._slGrid.setObjectName(u"_slGrid")
        self._slGrid.setChecked(False)

        self.horizontalLayout_22_1.addWidget(self._slGrid)

        self._slAbsTime = QCheckBox(self._sliderPanel)
        self._slAbsTime.setObjectName(u"_slAbsTime")

        self.horizontalLayout_22_1.addWidget(self._slAbsTime)

        self._slMagnify = QCheckBox(self._sliderPanel)
        self._slMagnify.setObjectName(u"_slMagnify")

        self.horizontalLayout_22_1.addWidget(self._slMagnify)

        self._ScorWinVisible = QCheckBox(self._sliderPanel)
        self._ScorWinVisible.setObjectName(u"_ScorWinVisible")
        self._ScorWinVisible.setChecked(False)

        self.horizontalLayout_22_1.addWidget(self._ScorWinVisible)

        self._LockScorSigWins = QCheckBox(self._sliderPanel)
        self._LockScorSigWins.setObjectName(u"_LockScorSigWins")
        self._LockScorSigWins.setChecked(True)

        self.horizontalLayout_22_1.addWidget(self._LockScorSigWins)


        self._sliderPanelLayout.addLayout(self.horizontalLayout_22_1)


        self.verticalLayout_15.addWidget(self._sliderPanel)


        self.horizontalLayout_3.addWidget(self._slFrame)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_16)


        self.gridLayout_21.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.splitter.addWidget(self.layoutWidget)

        self.horizontalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1359, 21))
        self.menuFiles = QMenu(self.menubar)
        self.menuFiles.setObjectName(u"menuFiles")
        self.menuSave = QMenu(self.menuFiles)
        self.menuSave.setObjectName(u"menuSave")
        self.menuSaveHypnogram = QMenu(self.menuSave)
        self.menuSaveHypnogram.setObjectName(u"menuSaveHypnogram")
        self.menuSaveDetections = QMenu(self.menuSave)
        self.menuSaveDetections.setObjectName(u"menuSaveDetections")
        self.menuSaveDetections.setEnabled(False)
        self.menuLoad = QMenu(self.menuFiles)
        self.menuLoad.setObjectName(u"menuLoad")
        self.menuLoadDetections = QMenu(self.menuLoad)
        self.menuLoadDetections.setObjectName(u"menuLoadDetections")
        self.menuDisplay = QMenu(self.menubar)
        self.menuDisplay.setObjectName(u"menuDisplay")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.QuickSettings, self._stacked_panels)
        QWidget.setTabOrder(self._stacked_panels, self._stacked_tools)
        QWidget.setTabOrder(self._stacked_tools, self._stacked_detections)

        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menuFiles.addAction(self.menuSave.menuAction())
        self.menuFiles.addAction(self.menuLoad.menuAction())
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.menuExit)
        self.menuSave.addAction(self.menuSaveHypnogram.menuAction())
        self.menuSave.addAction(self.menuSaveInfoTable)
        self.menuSave.addAction(self.menuSaveScoringTable)
        self.menuSave.addAction(self.menuSaveDetections.menuAction())
        self.menuSave.addAction(self.menuSaveConfig)
        self.menuSave.addAction(self.menuSaveAnnotations)
        self.menuSave.addAction(self.menuSaveScreenshot)
        self.menuSaveHypnogram.addAction(self.menuSaveHypnogramData)
        self.menuSaveHypnogram.addAction(self.menuSaveHypnogramFigure)
        self.menuSaveDetections.addAction(self.menuSaveDetectAll)
        self.menuSaveDetections.addAction(self.menuSaveDetectSelected)
        self.menuLoad.addAction(self.menuLoadData)
        self.menuLoad.addAction(self.menuLoadHypno)
        self.menuLoad.addAction(self.menuLoadConfig)
        self.menuLoad.addAction(self.menuLoadDetections.menuAction())
        self.menuLoad.addAction(self.menuLoadAnnotations)
        self.menuLoadDetections.addAction(self.menuLoadDetectAll)
        self.menuLoadDetections.addAction(self.menuLoadDetectSelect)
        self.menuDisplay.addAction(self.menuDispSettings)
        self.menuDisplay.addAction(self.menuDispSpec)
        self.menuDisplay.addAction(self.menuDispHypno)
        self.menuDisplay.addAction(self.menuDispTimeax)
        self.menuDisplay.addAction(self.menuDispNavbar)
        self.menuDisplay.addAction(self.menuDispIndic)
        self.menuDisplay.addAction(self.menuDispTopo)
        self.menuDisplay.addAction(self.menuDispZoom)

        self.retranslateUi(MainWindow)

        self.QuickSettings.setCurrentIndex(4)
        self._stacked_panels.setCurrentIndex(0)
        self._PanTopoDisp.setCurrentIndex(0)
        self._stacked_tools.setCurrentIndex(1)
        self._DetectionTab.setCurrentIndex(0)
        self._stacked_detections.setCurrentIndex(2)
        self._slRules.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sleep", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionCortical_repartition.setText(QCoreApplication.translate("MainWindow", u"Cortical repartition", None))
        self.actionCortical.setText(QCoreApplication.translate("MainWindow", u"Cortical", None))
        self.actionSagittal.setText(QCoreApplication.translate("MainWindow", u"Sagittal", None))
        self.actionAxial.setText(QCoreApplication.translate("MainWindow", u"Axial", None))
        self.actionCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.actionLeft.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.actionRight.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.menuDispSettings.setText(QCoreApplication.translate("MainWindow", u"Quick settings", None))
#if QT_CONFIG(shortcut)
        self.menuDispSettings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionProjection.setText(QCoreApplication.translate("MainWindow", u"Projection", None))
#if QT_CONFIG(tooltip)
        self.actionProjection.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Find all vertices under a distance of t_radius with each source and project s_data to the surface</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionProjection.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionRepartition.setText(QCoreApplication.translate("MainWindow", u"Repartition", None))
#if QT_CONFIG(shortcut)
        self.actionRepartition.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionShortcuts.setText(QCoreApplication.translate("MainWindow", u"Shortcuts", None))
#if QT_CONFIG(shortcut)
        self.actionShortcuts.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionUi_settings.setText(QCoreApplication.translate("MainWindow", u"Ui settings", None))
        self.actionNdPlt.setText(QCoreApplication.translate("MainWindow", u"Nd-plot", None))
        self.actionOnedPlt.setText(QCoreApplication.translate("MainWindow", u"1d-plot", None))
        self.actionImage.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.actionColormap.setText(QCoreApplication.translate("MainWindow", u"Colormap", None))
        self.menuShortcut.setText(QCoreApplication.translate("MainWindow", u"Shortcuts", None))
#if QT_CONFIG(shortcut)
        self.menuShortcut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.menuDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
#if QT_CONFIG(shortcut)
        self.menuDocumentation.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionScreenshot.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
#if QT_CONFIG(shortcut)
        self.actionScreenshot.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_hypnogram.setText(QCoreApplication.translate("MainWindow", u"Save hypnogram data", None))
        self.actionSave_infos.setText(QCoreApplication.translate("MainWindow", u"Save infos table", None))
        self.actionSave_scoring.setText(QCoreApplication.translate("MainWindow", u"Save scoring table", None))
        self.actionSave_detection.setText(QCoreApplication.translate("MainWindow", u"Save detection table", None))
        self.actionSave_all.setText(QCoreApplication.translate("MainWindow", u"Save all", None))
        self.menuExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.menuExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionLoad_hypnogram.setText(QCoreApplication.translate("MainWindow", u"Load hypnogram", None))
        self.menuSaveInfoTable.setText(QCoreApplication.translate("MainWindow", u"Stats info table", None))
        self.menuSaveScoringTable.setText(QCoreApplication.translate("MainWindow", u"Scoring table", None))
        self.actionAll.setText(QCoreApplication.translate("MainWindow", u"All", None))
#if QT_CONFIG(shortcut)
        self.actionAll.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.menuLoadHypno.setText(QCoreApplication.translate("MainWindow", u"Hypnogram", None))
        self.menuLoadData.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.actionHypnogram_figure.setText(QCoreApplication.translate("MainWindow", u"Hypnogram figure", None))
        self.menuLoadConfig.setText(QCoreApplication.translate("MainWindow", u"GUI config", None))
        self.menuSaveConfig.setText(QCoreApplication.translate("MainWindow", u"GUI config", None))
        self.menuDownload_pdf_doc.setText(QCoreApplication.translate("MainWindow", u"Download pdf doc", None))
        self.menuSaveHypnogramFigure.setText(QCoreApplication.translate("MainWindow", u"Figure", None))
        self.menuSaveHypnogramData.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.menuSaveDetectAll.setText(QCoreApplication.translate("MainWindow", u"All detections", None))
        self.menuSaveDetectSelected.setText(QCoreApplication.translate("MainWindow", u"Selected detection", None))
        self.menuSaveScreenshotEntire.setText(QCoreApplication.translate("MainWindow", u"Entire window", None))
        self.menuSaveScreenshotSelected.setText(QCoreApplication.translate("MainWindow", u"Selected canvas", None))
        self.menuLoadDetectAll.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.menuLoadDetectSelect.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.menuDispSpec.setText(QCoreApplication.translate("MainWindow", u"Spectrogram", None))
#if QT_CONFIG(shortcut)
        self.menuDispSpec.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispHypno.setText(QCoreApplication.translate("MainWindow", u"Hypnogram", None))
#if QT_CONFIG(shortcut)
        self.menuDispHypno.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispNavbar.setText(QCoreApplication.translate("MainWindow", u"Navigation bar", None))
#if QT_CONFIG(shortcut)
        self.menuDispNavbar.setShortcut(QCoreApplication.translate("MainWindow", u"P", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispTimeax.setText(QCoreApplication.translate("MainWindow", u"Time axis", None))
#if QT_CONFIG(shortcut)
        self.menuDispTimeax.setShortcut(QCoreApplication.translate("MainWindow", u"X", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispTopo.setText(QCoreApplication.translate("MainWindow", u"Topoplot", None))
#if QT_CONFIG(shortcut)
        self.menuDispTopo.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispIndic.setText(QCoreApplication.translate("MainWindow", u"Time indicators", None))
#if QT_CONFIG(shortcut)
        self.menuDispIndic.setShortcut(QCoreApplication.translate("MainWindow", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.actionZoom_mode.setText(QCoreApplication.translate("MainWindow", u"Zoom mode", None))
#if QT_CONFIG(shortcut)
        self.actionZoom_mode.setShortcut(QCoreApplication.translate("MainWindow", u"Z", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispZoom.setText(QCoreApplication.translate("MainWindow", u"Zoom mode", None))
#if QT_CONFIG(shortcut)
        self.menuDispZoom.setShortcut(QCoreApplication.translate("MainWindow", u"Z", None))
#endif // QT_CONFIG(shortcut)
        self.menuSettingCleanHyp.setText(QCoreApplication.translate("MainWindow", u"Clean hypnogram", None))
        self.menuSaveAnnotations.setText(QCoreApplication.translate("MainWindow", u"Annotation", None))
        self.menuLoadAnnotations.setText(QCoreApplication.translate("MainWindow", u"Annotations", None))
        self.menuSaveScreenshot.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
#if QT_CONFIG(shortcut)
        self.menuSaveScreenshot.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.QuickSettings.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Panel\n"
"type", None))
        self._pan_pick.setItemText(0, QCoreApplication.translate("MainWindow", u"Channels", None))
        self._pan_pick.setItemText(1, QCoreApplication.translate("MainWindow", u"Time-frequency", None))
        self._pan_pick.setItemText(2, QCoreApplication.translate("MainWindow", u"Hypnogram", None))
        self._pan_pick.setItemText(3, QCoreApplication.translate("MainWindow", u"Topoplot", None))

#if QT_CONFIG(tooltip)
        self._pan_pick.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select the panel type to control</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select the channels to be displayed and control the amplitudes of each one of them.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Select channels to display", None))
#if QT_CONFIG(tooltip)
        self._PanScrollChan.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Amplitude control", None))
#if QT_CONFIG(tooltip)
        self._PanAllAmpMin.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Change minimum amplitude for all channels</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._PanAllAmpMax.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Change maximum amplitude for all channels</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Set all amplitudes to: ", None))
        self._PanAmpAuto.setText(QCoreApplication.translate("MainWindow", u"Use auto-ajusted amplitudes", None))
        self._PanAmpSym.setText(QCoreApplication.translate("MainWindow", u"Use symetric amplitudes", None))
#if QT_CONFIG(tooltip)
        self._PanChanSelectAll.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Display all channels</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._PanChanSelectAll.setText(QCoreApplication.translate("MainWindow", u"Display all channels", None))
#if QT_CONFIG(tooltip)
        self._PanChanDeselectAll.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Hide all channels</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._PanChanDeselectAll.setText(QCoreApplication.translate("MainWindow", u"Hide all channels", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Line", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Line width", None))
        self._channels_alias.setText(QCoreApplication.translate("MainWindow", u"Antialias", None))
        self._PanSpecMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"Fourier transform", None))
        self._PanSpecMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"Wavelet", None))
        self._PanSpecMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"Multitaper", None))

#if QT_CONFIG(tooltip)
        self._PanSpecMethod.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Computation method for the spectrogram</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Apply on\n"
"channel", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self._PanSpecChan.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select the channel on which to compute the spectrogram</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Colormap", None))
#if QT_CONFIG(tooltip)
        self._PanSpecCmap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Colormap for the spectrogram</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._PanSpecCmapInv.setText(QCoreApplication.translate("MainWindow", u"Reversed", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
#if QT_CONFIG(tooltip)
        self._PanSpecCon.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Change the contrast of the spectrogram</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Interpolation", None))
        self._PanSpecInterp.setItemText(0, QCoreApplication.translate("MainWindow", u"nearest", None))
        self._PanSpecInterp.setItemText(1, QCoreApplication.translate("MainWindow", u"bilinear", None))
        self._PanSpecInterp.setItemText(2, QCoreApplication.translate("MainWindow", u"gaussian", None))
        self._PanSpecInterp.setItemText(3, QCoreApplication.translate("MainWindow", u"hanning", None))
        self._PanSpecInterp.setItemText(4, QCoreApplication.translate("MainWindow", u"hamming", None))
        self._PanSpecInterp.setItemText(5, QCoreApplication.translate("MainWindow", u"kaiser", None))
        self._PanSpecInterp.setItemText(6, QCoreApplication.translate("MainWindow", u"quadric", None))
        self._PanSpecInterp.setItemText(7, QCoreApplication.translate("MainWindow", u"bicubic", None))
        self._PanSpecInterp.setItemText(8, QCoreApplication.translate("MainWindow", u"bessel", None))
        self._PanSpecInterp.setItemText(9, QCoreApplication.translate("MainWindow", u"blackman", None))

#if QT_CONFIG(tooltip)
        self._PanSpecInterp.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select to channel used for the spectrogram</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Overlap", None))
#if QT_CONFIG(tooltip)
        self._PanSpecNfft.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Length of each time window for computing the spectrogram</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._PanSpecStep.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Overlap between each consecutive windows (e.g 0 mean no overlap and 0,50 mean 50% overlap)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(tooltip)
        self._PanSpecFstart.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Starting frequency for the spectrogram</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"End", None))
#if QT_CONFIG(tooltip)
        self._PanSpecFend.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ending frequency for the spectrogram</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Frequencies", None))
        self._PanSpecNorm.setItemText(0, QCoreApplication.translate("MainWindow", u"No normalization", None))
        self._PanSpecNorm.setItemText(1, QCoreApplication.translate("MainWindow", u"Subtract the mean", None))
        self._PanSpecNorm.setItemText(2, QCoreApplication.translate("MainWindow", u"Divide by the mean", None))
        self._PanSpecNorm.setItemText(3, QCoreApplication.translate("MainWindow", u"Subtract then divide by the mean", None))
        self._PanSpecNorm.setItemText(4, QCoreApplication.translate("MainWindow", u"Z-score", None))

#if QT_CONFIG(tooltip)
        self._PanSpecNorm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select to channel used for the spectrogram</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Normalization", None))
#if QT_CONFIG(tooltip)
        self._PanSpecApply.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Compute the spectrogram on the selected channel and using the time length, overlap, [fstart, fend], colormap and contrast.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._PanSpecApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Linewidth", None))
#if QT_CONFIG(tooltip)
        self._PanHypnoLw.setToolTip(QCoreApplication.translate("MainWindow", u"Change the line width of the hypnogram [ 1 - 10 ]", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._PanHypnoColor.setToolTip(QCoreApplication.translate("MainWindow", u"Select whether the hypnogram is displayed in color or in black", None))
#endif // QT_CONFIG(tooltip)
        self._PanHypnoColor.setText(QCoreApplication.translate("MainWindow", u"Color", None))
#if QT_CONFIG(tooltip)
        self._PanHypnoReset.setToolTip(QCoreApplication.translate("MainWindow", u"Reset the hypnogram to an empty one", None))
#endif // QT_CONFIG(tooltip)
        self._PanHypnoReset.setText(QCoreApplication.translate("MainWindow", u"Reset hypnogram", None))
        self._PanTopoAutoClim.setText(QCoreApplication.translate("MainWindow", u"Use automatic limits", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Clim", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Properties", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Fmin", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Fmax", None))
        self._PanTopoDisp.setItemText(0, QCoreApplication.translate("MainWindow", u"power", None))
        self._PanTopoDisp.setItemText(1, QCoreApplication.translate("MainWindow", u"amplitude", None))
        self._PanTopoDisp.setItemText(2, QCoreApplication.translate("MainWindow", u"filter", None))

        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Colormap", None))
        self._PanTopoRev.setText(QCoreApplication.translate("MainWindow", u"Inverse", None))
        self._PanTopoApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.q_Panels), QCoreApplication.translate("MainWindow", u"Panels", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Tool\n"
"type", None))
        self._tool_pick.setItemText(0, QCoreApplication.translate("MainWindow", u"Signal processing", None))
        self._tool_pick.setItemText(1, QCoreApplication.translate("MainWindow", u"Re-referencing", None))

#if QT_CONFIG(tooltip)
        self._tool_pick.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select the panel type to control</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Apply preprocessing\n"
"to", None))
        self._SigFiltChan.setItemText(0, QCoreApplication.translate("MainWindow", u"all channels", None))

#if QT_CONFIG(tooltip)
        self._SigFiltChan.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Display the signal, in a specific frequency band as :</p><p>- &quot;filter&quot; : simply, the filtered signal</p><p>- &quot;amplitude&quot; : the amplitude of the signal</p><p>- &quot;power&quot; : the power of the signal</p><p>- &quot;phase&quot; : the phase of the signal</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Mean and trend", None))
        self._SigMean.setText(QCoreApplication.translate("MainWindow", u"Remove mean", None))
        self._SigTrend.setText(QCoreApplication.translate("MainWindow", u"Remove linear trend", None))
        self._SigFilt.setTitle(QCoreApplication.translate("MainWindow", u"Filtering", None))
        self._SigFiltDisp.setItemText(0, QCoreApplication.translate("MainWindow", u"filter", None))
        self._SigFiltDisp.setItemText(1, QCoreApplication.translate("MainWindow", u"amplitude", None))
        self._SigFiltDisp.setItemText(2, QCoreApplication.translate("MainWindow", u"power", None))
        self._SigFiltDisp.setItemText(3, QCoreApplication.translate("MainWindow", u"phase", None))

#if QT_CONFIG(tooltip)
        self._SigFiltDisp.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Display the signal, in a specific frequency band as :</p><p>- &quot;filter&quot; : simply, the filtered signal</p><p>- &quot;amplitude&quot; : the amplitude of the signal</p><p>- &quot;power&quot; : the power of the signal</p><p>- &quot;phase&quot; : the phase of the signal</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Filter type", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self._SigFiltApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self._SigFiltBand.setItemText(0, QCoreApplication.translate("MainWindow", u"bandpass", None))
        self._SigFiltBand.setItemText(1, QCoreApplication.translate("MainWindow", u"bandstop", None))
        self._SigFiltBand.setItemText(2, QCoreApplication.translate("MainWindow", u"lowpass", None))
        self._SigFiltBand.setItemText(3, QCoreApplication.translate("MainWindow", u"highpass", None))

#if QT_CONFIG(tooltip)
        self._SigFiltBand.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>- bandpass: keep only frequencies between [fmin, fmax]</p><p>- bandstop: remove frequencies between [fmin, fmax]</p><p>- lowpass: keep only frequencies under fmax</p><p>- highpass: keep only frequencies over fmin</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Fmin", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fmax", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"order", None))
#if QT_CONFIG(tooltip)
        self._SigFiltOrder.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Choose filter order and control narrow band. It is not recommended to use filter order over 3 (can provoc distorsion).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._SigFiltMeth.setItemText(0, QCoreApplication.translate("MainWindow", u"butterworth", None))
        self._SigFiltMeth.setItemText(1, QCoreApplication.translate("MainWindow", u"bessel", None))

        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Warning : re-referencing can only be achieved once", None))
#if QT_CONFIG(tooltip)
        self._ToolsRefIgnore.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>When this option is checked, channels that are not re-referenced are going to be ignored in the interface  (Ex : if channels is [ O1, O2, O3, Cz, Pz ]  the bipolarized channels will be [ O1, O2-O1, O3-O2, Cz, Pz ] but if this checkbox is activated you will only see the clean version [ O2-O1, 03-O2 ] )</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ToolsRefIgnore.setText(QCoreApplication.translate("MainWindow", u"Remove non-referenced channels", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Use as  reference", None))
#if QT_CONFIG(tooltip)
        self._ToolsRefLst.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Channel to use as the reference</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self._ToolsRefIgn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>If some channels doesn't need to be re-referenced, and if you want to visualize them, be sure to deactivate &quot;Ignore non-referenced channels&quot;</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ToolsRefIgn.setText(QCoreApplication.translate("MainWindow", u"Add channels that don't need to be\n"
"re-referenced", None))
        self._ToolsRefMeth.setItemText(0, QCoreApplication.translate("MainWindow", u"Use one channel as reference", None))
        self._ToolsRefMeth.setItemText(1, QCoreApplication.translate("MainWindow", u"Common average", None))
        self._ToolsRefMeth.setItemText(2, QCoreApplication.translate("MainWindow", u"Bipolarization", None))

        self._ToolsRefApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.q_Tools), QCoreApplication.translate("MainWindow", u"Tools", None))
        ___qtablewidgetitem = self._infoTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Infos", None));
        ___qtablewidgetitem1 = self._infoTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.q_Info), QCoreApplication.translate("MainWindow", u"Infos", None))
        ___qtablewidgetitem2 = self._scoreTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"From (minutes)", None));
        ___qtablewidgetitem3 = self._scoreTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"To (minutes)", None));
        ___qtablewidgetitem4 = self._scoreTable.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Stage", None));
        self._scoreAdd.setText(QCoreApplication.translate("MainWindow", u"Add line", None))
        self._scoreRm.setText(QCoreApplication.translate("MainWindow", u"Remove line", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.q_Score), QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Detection type", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"On channel", None))
        self._ToolDetectType.setItemText(0, QCoreApplication.translate("MainWindow", u"Spindles", None))
        self._ToolDetectType.setItemText(1, QCoreApplication.translate("MainWindow", u"REM", None))
        self._ToolDetectType.setItemText(2, QCoreApplication.translate("MainWindow", u"K-complexes", None))
        self._ToolDetectType.setItemText(3, QCoreApplication.translate("MainWindow", u"Slow waves", None))
        self._ToolDetectType.setItemText(4, QCoreApplication.translate("MainWindow", u"Muscle twitches", None))
        self._ToolDetectType.setItemText(5, QCoreApplication.translate("MainWindow", u"Peaks", None))

#if QT_CONFIG(tooltip)
        self._ToolDetectType.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Choose the detection type</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ToolRdViz.setText(QCoreApplication.translate("MainWindow", u"Visible", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Apply\n"
"on", None))
        self._ToolRdSelected.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self._ToolRdAll.setText(QCoreApplication.translate("MainWindow", u"All", None))
#if QT_CONFIG(tooltip)
        self._ToolDetectChan.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pick up a channel to run the detection (only avaible with &quot;Selected&quot; option)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
#if QT_CONFIG(tooltip)
        self._ToolSpinTmin.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimum spindle's duration</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self._ToolSpinRemOnly.setText(QCoreApplication.translate("MainWindow", u"Perform detection only for NREM sleep", None))
#if QT_CONFIG(tooltip)
        self._ToolSpinFmin.setToolTip(QCoreApplication.translate("MainWindow", u"High-pass cutoff frequency", None))
#endif // QT_CONFIG(tooltip)
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Tmax", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Tmin", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Fmin", None))
#if QT_CONFIG(tooltip)
        self._ToolSpinFmax.setToolTip(QCoreApplication.translate("MainWindow", u"Low-pass cutoff frequency", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Spindles", None))
#if QT_CONFIG(tooltip)
        self._ToolSpinTmax.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximum spindle's duration</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Fmax", None))
#if QT_CONFIG(tooltip)
        self._ToolSpinTh.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Look for signals having an amplitude 'Threshold' times superior to the deviation of the filtered signal amplitude</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._ToolRemTh.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Number of standard deviation of the derivative signal</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self._ToolRemOnly.setText(QCoreApplication.translate("MainWindow", u"Perform detection only for REM sleep", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"REM", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Min / Max", None))
#if QT_CONFIG(tooltip)
        self._ToolKCMinAmp.setToolTip(QCoreApplication.translate("MainWindow", u"Min amplitude of KC", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._ToolKCMaxAmp.setToolTip(QCoreApplication.translate("MainWindow", u"Max amplitude of KC", None))
#endif // QT_CONFIG(tooltip)
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Proba threshold", None))
        self.kc_label.setText(QCoreApplication.translate("MainWindow", u"K-complexes", None))
        self._ToolKCNremOnly.setText(QCoreApplication.translate("MainWindow", u"Use hypnogram to improve detection", None))
#if QT_CONFIG(tooltip)
        self._ToolKCProbTh.setToolTip(QCoreApplication.translate("MainWindow", u"Number of standard deviations of the wavelet envelope", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_62.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Tmin / Tmax", None))
#if QT_CONFIG(tooltip)
        self._ToolKCMinDur.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimum duration of KC (ms)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._ToolKCMaxDur.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximum duration of KC (ms)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Amp threshold", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Slow waves", None))
#if QT_CONFIG(tooltip)
        self._ToolWaveTh.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Normalized Delta power threshold (between 0 and 1) </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Delta power (norm.)", None))
#if QT_CONFIG(tooltip)
        self._ToolMTTh.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Number of standard deviation of the derivative signal</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self._ToolMTOnly.setText(QCoreApplication.translate("MainWindow", u"Perform detection only for REM sleep", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Muscle\n"
"Twitches", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Lookahead", None))
#if QT_CONFIG(tooltip)
        self._ToolPeakLook.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimum distance between two peaks</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"seconds", None))
        self._ToolPeakMinMax.setItemText(0, QCoreApplication.translate("MainWindow", u"Max only", None))
        self._ToolPeakMinMax.setItemText(1, QCoreApplication.translate("MainWindow", u"Min only", None))
        self._ToolPeakMinMax.setItemText(2, QCoreApplication.translate("MainWindow", u"Min and Max", None))

#if QT_CONFIG(tooltip)
        self._ToolPeakMinMax.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Search either for maximum / minimum / both</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Peak", None))
        ___qtablewidgetitem5 = self._ToolDetectTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem6 = self._ToolDetectTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Density ( / min )", None));
#if QT_CONFIG(tooltip)
        self._ToolDetectApply.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Apply detection either on :</p><p>- Selected channels via the channel selection box above</p><p>- Visible channels</p><p>- All channels</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ToolDetectApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self._DetectionTab.setTabText(self._DetectionTab.indexOf(self.q_DetectSettings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Select which\n"
"detection to\n"
"display", None))
        self._DetectViz.setText(QCoreApplication.translate("MainWindow", u"Visible", None))
        self._DetectRm.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        ___qtablewidgetitem7 = self._DetectLocations.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Start (sec)", None));
        ___qtablewidgetitem8 = self._DetectLocations.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"End (sec)", None));
        ___qtablewidgetitem9 = self._DetectLocations.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Duration (ms)", None));
        ___qtablewidgetitem10 = self._DetectLocations.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Stage", None));
        self._DetecRmEvent.setText(QCoreApplication.translate("MainWindow", u"Remove selected event", None))
        self._DetectionTab.setTabText(self._DetectionTab.indexOf(self.q_DetectLoc), QCoreApplication.translate("MainWindow", u"Locations", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.q_Detection), QCoreApplication.translate("MainWindow", u"Detection", None))
        ___qtablewidgetitem11 = self._AnnotateTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Start (seconds)", None));
        ___qtablewidgetitem12 = self._AnnotateTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"End (seconds)", None));
        ___qtablewidgetitem13 = self._AnnotateTable.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        self._AnnotateAdd.setText(QCoreApplication.translate("MainWindow", u"Annotate", None))
        self._AnnotateRm.setText(QCoreApplication.translate("MainWindow", u"Remove selected line", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Annotations", None))
        self._topoTitle.setText(QCoreApplication.translate("MainWindow", u"topotitle", None))
        self._txtCursor.setText(QCoreApplication.translate("MainWindow", u"[...]", None))
        self._SlText.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self._AnnotateRun.setText(QCoreApplication.translate("MainWindow", u"Annotate", None))
        self._sliderControlsLayout.setColumnStretch(QCoreApplication.translate("MainWindow", u"0,0,0,0,0,1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Go to", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"sec", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"sec", None))
        self.label_3_1.setText(QCoreApplication.translate("MainWindow", u"Scoring Window", None))
        self.label_4_1.setText(QCoreApplication.translate("MainWindow", u"sec", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Slider step", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"sec", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Rule", None))
        self._slRules.setItemText(0, QCoreApplication.translate("MainWindow", u"seconds", None))
        self._slRules.setItemText(1, QCoreApplication.translate("MainWindow", u"minutes", None))
        self._slRules.setItemText(2, QCoreApplication.translate("MainWindow", u"hours", None))

        self._slGrid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self._slAbsTime.setText(QCoreApplication.translate("MainWindow", u"Absolute time", None))
        self._slMagnify.setText(QCoreApplication.translate("MainWindow", u"Magnify", None))
        self._ScorWinVisible.setText(QCoreApplication.translate("MainWindow", u"Display scoring window", None))
        self._LockScorSigWins.setText(QCoreApplication.translate("MainWindow", u"Lock scoring to display", None))
        self.menuFiles.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuSaveHypnogram.setTitle(QCoreApplication.translate("MainWindow", u"Hypnogram", None))
        self.menuSaveDetections.setTitle(QCoreApplication.translate("MainWindow", u"Detection", None))
        self.menuLoad.setTitle(QCoreApplication.translate("MainWindow", u"Load", None))
        self.menuLoadDetections.setTitle(QCoreApplication.translate("MainWindow", u"Detections", None))
        self.menuDisplay.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

