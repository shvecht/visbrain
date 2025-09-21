# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brain_gui.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QSplitter,
    QStackedWidget, QStatusBar, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1513, 920)
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
        self.menuDispQuickSettings = QAction(MainWindow)
        self.menuDispQuickSettings.setObjectName(u"menuDispQuickSettings")
        self.menuDispQuickSettings.setCheckable(True)
        self.menuDispQuickSettings.setChecked(True)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.menuCortProj = QAction(MainWindow)
        self.menuCortProj.setObjectName(u"menuCortProj")
        self.menuCortRep = QAction(MainWindow)
        self.menuCortRep.setObjectName(u"menuCortRep")
        self.actionShortcuts = QAction(MainWindow)
        self.actionShortcuts.setObjectName(u"actionShortcuts")
        self.actionShortcuts.setCheckable(True)
        self.actionUi_settings = QAction(MainWindow)
        self.actionUi_settings.setObjectName(u"actionUi_settings")
        self.actionUi_settings.setCheckable(True)
        self.actionUi_settings.setChecked(False)
        self.actionMNI = QAction(MainWindow)
        self.actionMNI.setObjectName(u"actionMNI")
        self.actionMNI.setCheckable(True)
        self.actionSources = QAction(MainWindow)
        self.actionSources.setObjectName(u"actionSources")
        self.actionSources.setCheckable(True)
        self.actionConnectivity = QAction(MainWindow)
        self.actionConnectivity.setObjectName(u"actionConnectivity")
        self.actionConnectivity.setCheckable(True)
        self.actionColormap = QAction(MainWindow)
        self.actionColormap.setObjectName(u"actionColormap")
        self.actionColormap.setCheckable(True)
        self.actionShortcut = QAction(MainWindow)
        self.actionShortcut.setObjectName(u"actionShortcut")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionScreenshot = QAction(MainWindow)
        self.actionScreenshot.setObjectName(u"actionScreenshot")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.menuDispCbar = QAction(MainWindow)
        self.menuDispCbar.setObjectName(u"menuDispCbar")
        self.menuDispCbar.setCheckable(True)
        self.menuRotTop = QAction(MainWindow)
        self.menuRotTop.setObjectName(u"menuRotTop")
        self.menuRotBottom = QAction(MainWindow)
        self.menuRotBottom.setObjectName(u"menuRotBottom")
        self.menuRotLeft = QAction(MainWindow)
        self.menuRotLeft.setObjectName(u"menuRotLeft")
        self.menuRotRight = QAction(MainWindow)
        self.menuRotRight.setObjectName(u"menuRotRight")
        self.menuRotFront = QAction(MainWindow)
        self.menuRotFront.setObjectName(u"menuRotFront")
        self.menuRotBack = QAction(MainWindow)
        self.menuRotBack.setObjectName(u"menuRotBack")
        self.menuCamTurn = QAction(MainWindow)
        self.menuCamTurn.setObjectName(u"menuCamTurn")
        self.menuCamFly = QAction(MainWindow)
        self.menuCamFly.setObjectName(u"menuCamFly")
        self.menuCamFly.setCheckable(True)
        self.menuDispBrain = QAction(MainWindow)
        self.menuDispBrain.setObjectName(u"menuDispBrain")
        self.menuDispBrain.setCheckable(True)
        self.menuDispSources = QAction(MainWindow)
        self.menuDispSources.setObjectName(u"menuDispSources")
        self.menuDispSources.setCheckable(True)
        self.menuDispSources.setChecked(True)
        self.menuDispConnect = QAction(MainWindow)
        self.menuDispConnect.setObjectName(u"menuDispConnect")
        self.menuDispConnect.setCheckable(True)
        self.menuDispConnect.setChecked(True)
        self.menuDispROI = QAction(MainWindow)
        self.menuDispROI.setObjectName(u"menuDispROI")
        self.menuDispROI.setCheckable(True)
        self.menuDispROI.setEnabled(True)
        self.menuSaveScreenCan = QAction(MainWindow)
        self.menuSaveScreenCan.setObjectName(u"menuSaveScreenCan")
        self.menuSaveScreenWin = QAction(MainWindow)
        self.menuSaveScreenWin.setObjectName(u"menuSaveScreenWin")
        self.actionConfig = QAction(MainWindow)
        self.actionConfig.setObjectName(u"actionConfig")
        self.menuSaveGuiConfig = QAction(MainWindow)
        self.menuSaveGuiConfig.setObjectName(u"menuSaveGuiConfig")
        self.menuSaveCbarConfig = QAction(MainWindow)
        self.menuSaveCbarConfig.setObjectName(u"menuSaveCbarConfig")
        self.menuLoadGuiConfig = QAction(MainWindow)
        self.menuLoadGuiConfig.setObjectName(u"menuLoadGuiConfig")
        self.menuLoadCbarConfig = QAction(MainWindow)
        self.menuLoadCbarConfig.setObjectName(u"menuLoadCbarConfig")
        self.actionClean_projection = QAction(MainWindow)
        self.actionClean_projection.setObjectName(u"actionClean_projection")
        self.menuResetCam = QAction(MainWindow)
        self.menuResetCam.setObjectName(u"menuResetCam")
        self.actionObjects = QAction(MainWindow)
        self.actionObjects.setObjectName(u"actionObjects")
        self.actionObjects.setEnabled(False)
        self.actionCamera_2 = QAction(MainWindow)
        self.actionCamera_2.setObjectName(u"actionCamera_2")
        self.actionCamera_2.setEnabled(False)
        self.menuDispCrossec = QAction(MainWindow)
        self.menuDispCrossec.setObjectName(u"menuDispCrossec")
        self.menuDispCrossec.setCheckable(True)
        self.menuDispVol = QAction(MainWindow)
        self.menuDispVol.setObjectName(u"menuDispVol")
        self.menuDispVol.setCheckable(True)
        self.menuScreenshot = QAction(MainWindow)
        self.menuScreenshot.setObjectName(u"menuScreenshot")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setHandleWidth(12)
        self.q_widget = QWidget(self.splitter)
        self.q_widget.setObjectName(u"q_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.q_widget.sizePolicy().hasHeightForWidth())
        self.q_widget.setSizePolicy(sizePolicy)
        self.q_widget.setMinimumSize(QSize(360, 0))
        self.q_widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.q_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.QuickSettings = QTabWidget(self.q_widget)
        self.QuickSettings.setObjectName(u"QuickSettings")
        self.QuickSettings.setFocusPolicy(Qt.StrongFocus)
        self.QuickSettings.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setBold(False)
        self.QuickSettings.setFont(font)
        self.QuickSettings.setAutoFillBackground(True)
        self.QuickSettings.setDocumentMode(True)
        self.QuickSettings.setMovable(True)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_8 = QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.tab_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_4)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(6, 6, 6, 0)
        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_16.addWidget(self.line, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        self.label_5.setFont(font1)

        self.gridLayout_16.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_15, 2, 2, 1, 1)

        self._obj_type_lst = QComboBox(self.frame_4)
        self._obj_type_lst.addItem("")
        self._obj_type_lst.addItem("")
        self._obj_type_lst.addItem("")
        self._obj_type_lst.addItem("")
        self._obj_type_lst.addItem("")
        self._obj_type_lst.addItem("")
        self._obj_type_lst.addItem("")
        self._obj_type_lst.addItem("")
        self._obj_type_lst.addItem("")
        self._obj_type_lst.setObjectName(u"_obj_type_lst")

        self.gridLayout_16.addWidget(self._obj_type_lst, 0, 2, 1, 1)

        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.gridLayout_16.addWidget(self.label_16, 1, 0, 1, 1)

        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_16.addWidget(self.line_2, 1, 1, 1, 1)

        self._obj_name_lst = QComboBox(self.frame_4)
        self._obj_name_lst.setObjectName(u"_obj_name_lst")

        self.gridLayout_16.addWidget(self._obj_name_lst, 1, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_4)

        self._obj_stack = QStackedWidget(self.tab_4)
        self._obj_stack.setObjectName(u"_obj_stack")
        self._obj_stack.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self._obj_stack.sizePolicy().hasHeightForWidth())
        self._obj_stack.setSizePolicy(sizePolicy1)
        self._brain_page = QWidget()
        self._brain_page.setObjectName(u"_brain_page")
        self.verticalLayout_3 = QVBoxLayout(self._brain_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self._brain_grp = QGroupBox(self._brain_page)
        self._brain_grp.setObjectName(u"_brain_grp")
        self._brain_grp.setCheckable(True)
        self.verticalLayout_49 = QVBoxLayout(self._brain_grp)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, -1, 0, -1)
        self.line_43 = QFrame(self._brain_grp)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setMinimumSize(QSize(200, 0))
        self.line_43.setFrameShape(QFrame.Shape.HLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_49.addWidget(self.line_43)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_59 = QLabel(self._brain_grp)
        self.label_59.setObjectName(u"label_59")
        font2 = QFont()
        font2.setItalic(True)
        self.label_59.setFont(font2)

        self.gridLayout_2.addWidget(self.label_59, 5, 0, 1, 1)

        self._brain_ymin = QSlider(self._brain_grp)
        self._brain_ymin.setObjectName(u"_brain_ymin")
        self._brain_ymin.setMaximum(10)
        self._brain_ymin.setSliderPosition(10)
        self._brain_ymin.setOrientation(Qt.Horizontal)
        self._brain_ymin.setInvertedAppearance(False)

        self.gridLayout_2.addWidget(self._brain_ymin, 2, 1, 1, 1)

        self.label_36 = QLabel(self._brain_grp)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)

        self.gridLayout_2.addWidget(self.label_36, 2, 0, 1, 1)

        self.label_35 = QLabel(self._brain_grp)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.gridLayout_2.addWidget(self.label_35, 1, 0, 1, 1)

        self.label_56 = QLabel(self._brain_grp)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font2)

        self.gridLayout_2.addWidget(self.label_56, 4, 0, 1, 1)

        self._brain_xmax = QSlider(self._brain_grp)
        self._brain_xmax.setObjectName(u"_brain_xmax")
        self._brain_xmax.setMaximum(10)
        self._brain_xmax.setSliderPosition(10)
        self._brain_xmax.setOrientation(Qt.Horizontal)
        self._brain_xmax.setInvertedAppearance(False)
        self._brain_xmax.setInvertedControls(True)

        self.gridLayout_2.addWidget(self._brain_xmax, 1, 1, 1, 1)

        self._brain_xmin = QSlider(self._brain_grp)
        self._brain_xmin.setObjectName(u"_brain_xmin")
        self._brain_xmin.setMaximum(10)
        self._brain_xmin.setSliderPosition(10)
        self._brain_xmin.setOrientation(Qt.Horizontal)
        self._brain_xmin.setInvertedAppearance(False)
        self._brain_xmin.setInvertedControls(True)

        self.gridLayout_2.addWidget(self._brain_xmin, 0, 1, 1, 1)

        self.label_34 = QLabel(self._brain_grp)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)

        self.gridLayout_2.addWidget(self.label_34, 0, 0, 1, 1)

        self.label_40 = QLabel(self._brain_grp)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)

        self.gridLayout_2.addWidget(self.label_40, 3, 0, 1, 1)

        self._brain_ymax = QSlider(self._brain_grp)
        self._brain_ymax.setObjectName(u"_brain_ymax")
        self._brain_ymax.setMaximum(10)
        self._brain_ymax.setSliderPosition(10)
        self._brain_ymax.setOrientation(Qt.Horizontal)
        self._brain_ymax.setInvertedControls(True)

        self.gridLayout_2.addWidget(self._brain_ymax, 3, 1, 1, 1)

        self._brain_zmin = QSlider(self._brain_grp)
        self._brain_zmin.setObjectName(u"_brain_zmin")
        self._brain_zmin.setMaximum(10)
        self._brain_zmin.setSliderPosition(10)
        self._brain_zmin.setOrientation(Qt.Horizontal)
        self._brain_zmin.setInvertedAppearance(False)

        self.gridLayout_2.addWidget(self._brain_zmin, 4, 1, 1, 1)

        self._brain_zmax = QSlider(self._brain_grp)
        self._brain_zmax.setObjectName(u"_brain_zmax")
        self._brain_zmax.setMaximum(10)
        self._brain_zmax.setSliderPosition(10)
        self._brain_zmax.setOrientation(Qt.Horizontal)
        self._brain_zmax.setInvertedAppearance(False)
        self._brain_zmax.setInvertedControls(True)

        self.gridLayout_2.addWidget(self._brain_zmax, 5, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 3, 2, 1, 1)

        self.label_19 = QLabel(self._brain_grp)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.gridLayout_5.addWidget(self.label_19, 1, 0, 1, 1)

        self.line_27 = QFrame(self._brain_grp)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setMinimumSize(QSize(20, 0))
        self.line_27.setFrameShape(QFrame.Shape.VLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_27, 1, 1, 1, 1)

        self.label_26 = QLabel(self._brain_grp)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.gridLayout_5.addWidget(self.label_26, 2, 0, 1, 1)

        self._brain_template = QComboBox(self._brain_grp)
        self._brain_template.setObjectName(u"_brain_template")

        self.gridLayout_5.addWidget(self._brain_template, 2, 2, 1, 1)

        self.line_29 = QFrame(self._brain_grp)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setMinimumSize(QSize(20, 0))
        self.line_29.setFrameShape(QFrame.Shape.VLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_29, 2, 1, 1, 1)

        self._brain_hemi = QComboBox(self._brain_grp)
        self._brain_hemi.addItem("")
        self._brain_hemi.addItem("")
        self._brain_hemi.addItem("")
        self._brain_hemi.setObjectName(u"_brain_hemi")

        self.gridLayout_5.addWidget(self._brain_hemi, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 5, 2, 1, 1)

        self.line_55 = QFrame(self._brain_grp)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setMinimumSize(QSize(20, 0))
        self.line_55.setFrameShape(QFrame.Shape.VLine)
        self.line_55.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_55, 0, 1, 1, 1)

        self._brain_translucent = QCheckBox(self._brain_grp)
        self._brain_translucent.setObjectName(u"_brain_translucent")
        self._brain_translucent.setFont(font2)
        self._brain_translucent.setChecked(True)

        self.gridLayout_5.addWidget(self._brain_translucent, 0, 0, 1, 1)

        self._brain_alpha = QSlider(self._brain_grp)
        self._brain_alpha.setObjectName(u"_brain_alpha")
        self._brain_alpha.setMaximum(10)
        self._brain_alpha.setSliderPosition(10)
        self._brain_alpha.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self._brain_alpha, 0, 2, 1, 1)

        self.line_30 = QFrame(self._brain_grp)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setMinimumSize(QSize(20, 0))
        self.line_30.setFrameShape(QFrame.Shape.VLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_30, 3, 1, 1, 1)

        self.label_33 = QLabel(self._brain_grp)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)

        self.gridLayout_5.addWidget(self.label_33, 3, 0, 1, 1)

        self.label_62 = QLabel(self._brain_grp)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font2)

        self.gridLayout_5.addWidget(self.label_62, 4, 0, 1, 1)

        self.line_31 = QFrame(self._brain_grp)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setMinimumSize(QSize(20, 0))
        self.line_31.setFrameShape(QFrame.Shape.VLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_31, 4, 1, 1, 1)

        self._brain_inlight = QCheckBox(self._brain_grp)
        self._brain_inlight.setObjectName(u"_brain_inlight")

        self.gridLayout_5.addWidget(self._brain_inlight, 4, 2, 1, 1)


        self.verticalLayout_49.addLayout(self.gridLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_3)


        self.verticalLayout_3.addWidget(self._brain_grp)

        self._obj_stack.addWidget(self._brain_page)
        self._roi_page = QWidget()
        self._roi_page.setObjectName(u"_roi_page")
        self.verticalLayout_11 = QVBoxLayout(self._roi_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self._roi_grp = QGroupBox(self._roi_page)
        self._roi_grp.setObjectName(u"_roi_grp")
        self._roi_grp.setEnabled(True)
        self._roi_grp.setCheckable(True)
        self._roi_grp.setChecked(False)
        self.verticalLayout_23 = QVBoxLayout(self._roi_grp)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, -1, 0, -1)
        self.line_86 = QFrame(self._roi_grp)
        self.line_86.setObjectName(u"line_86")
        self.line_86.setMinimumSize(QSize(200, 0))
        self.line_86.setFrameShape(QFrame.Shape.HLine)
        self.line_86.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_23.addWidget(self.line_86)

        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(-1, 0, -1, -1)
        self.label_114 = QLabel(self._roi_grp)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setFont(font2)

        self.gridLayout_39.addWidget(self.label_114, 2, 0, 1, 1)

        self._roiSmooth = QSpinBox(self._roi_grp)
        self._roiSmooth.setObjectName(u"_roiSmooth")
        self._roiSmooth.setMinimum(3)
        self._roiSmooth.setSingleStep(2)
        self._roiSmooth.setValue(3)

        self.gridLayout_39.addWidget(self._roiSmooth, 3, 2, 1, 1)

        self.label_113 = QLabel(self._roi_grp)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setFont(font2)

        self.gridLayout_39.addWidget(self.label_113, 1, 0, 1, 1)

        self.line_3 = QFrame(self._roi_grp)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(10, 0))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_39.addWidget(self.line_3, 1, 1, 1, 1)

        self.line_4 = QFrame(self._roi_grp)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(10, 0))
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_39.addWidget(self.line_4, 3, 1, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_29, 5, 2, 1, 1)

        self._roiTransp = QCheckBox(self._roi_grp)
        self._roiTransp.setObjectName(u"_roiTransp")
        self._roiTransp.setEnabled(False)

        self.gridLayout_39.addWidget(self._roiTransp, 0, 0, 1, 3)

        self._roiDiv = QComboBox(self._roi_grp)
        self._roiDiv.setObjectName(u"_roiDiv")

        self.gridLayout_39.addWidget(self._roiDiv, 1, 2, 1, 1)

        self.line_7 = QFrame(self._roi_grp)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMinimumSize(QSize(10, 0))
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_39.addWidget(self.line_7, 2, 1, 1, 1)

        self._roiLevel = QComboBox(self._roi_grp)
        self._roiLevel.addItem("")
        self._roiLevel.addItem("")
        self._roiLevel.addItem("")
        self._roiLevel.addItem("")
        self._roiLevel.addItem("")
        self._roiLevel.addItem("")
        self._roiLevel.addItem("")
        self._roiLevel.setObjectName(u"_roiLevel")
        self._roiLevel.setEnabled(False)

        self.gridLayout_39.addWidget(self._roiLevel, 2, 2, 1, 1)

        self._roiIsSmooth = QCheckBox(self._roi_grp)
        self._roiIsSmooth.setObjectName(u"_roiIsSmooth")

        self.gridLayout_39.addWidget(self._roiIsSmooth, 3, 0, 1, 1)

        self._roiUniColor = QCheckBox(self._roi_grp)
        self._roiUniColor.setObjectName(u"_roiUniColor")

        self.gridLayout_39.addWidget(self._roiUniColor, 4, 0, 1, 3)


        self.verticalLayout_23.addLayout(self.gridLayout_39)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_55)

        self._roiButApply = QPushButton(self._roi_grp)
        self._roiButApply.setObjectName(u"_roiButApply")

        self.horizontalLayout_13.addWidget(self._roiButApply)

        self.horizontalSpacer_56 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_56)

        self._roiButRst = QPushButton(self._roi_grp)
        self._roiButRst.setObjectName(u"_roiButRst")

        self.horizontalLayout_13.addWidget(self._roiButRst)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)


        self.gridLayout_20.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_12, 0, 1, 1, 1)

        self._roiFilter = QLineEdit(self._roi_grp)
        self._roiFilter.setObjectName(u"_roiFilter")

        self.gridLayout_20.addWidget(self._roiFilter, 1, 0, 1, 1)

        self._roiToAdd = QTableView(self._roi_grp)
        self._roiToAdd.setObjectName(u"_roiToAdd")

        self.gridLayout_20.addWidget(self._roiToAdd, 0, 0, 1, 1)


        self.verticalLayout_23.addLayout(self.gridLayout_20)


        self.verticalLayout_11.addWidget(self._roi_grp)

        self._obj_stack.addWidget(self._roi_page)
        self._volume_page = QWidget()
        self._volume_page.setObjectName(u"_volume_page")
        self.verticalLayout_14 = QVBoxLayout(self._volume_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self._vol_grp = QGroupBox(self._volume_page)
        self._vol_grp.setObjectName(u"_vol_grp")
        self._vol_grp.setCheckable(True)
        self._vol_grp.setChecked(False)
        self.verticalLayout_22 = QVBoxLayout(self._vol_grp)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, -1, 0, -1)
        self.line_83 = QFrame(self._vol_grp)
        self.line_83.setObjectName(u"line_83")
        self.line_83.setMinimumSize(QSize(200, 0))
        self.line_83.setFrameShape(QFrame.Shape.HLine)
        self.line_83.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_22.addWidget(self.line_83)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self._volRendering = QComboBox(self._vol_grp)
        self._volRendering.addItem("")
        self._volRendering.addItem("")
        self._volRendering.addItem("")
        self._volRendering.addItem("")
        self._volRendering.setObjectName(u"_volRendering")

        self.gridLayout_18.addWidget(self._volRendering, 1, 2, 1, 1)

        self._volIsoTh = QDoubleSpinBox(self._vol_grp)
        self._volIsoTh.setObjectName(u"_volIsoTh")
        self._volIsoTh.setDecimals(4)
        self._volIsoTh.setMinimum(0.010000000000000)
        self._volIsoTh.setMaximum(0.999900000000000)
        self._volIsoTh.setSingleStep(0.025000000000000)

        self.gridLayout_18.addWidget(self._volIsoTh, 3, 2, 1, 1)

        self.line_84 = QFrame(self._vol_grp)
        self.line_84.setObjectName(u"line_84")
        self.line_84.setMinimumSize(QSize(20, 0))
        self.line_84.setFrameShape(QFrame.Shape.VLine)
        self.line_84.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_18.addWidget(self.line_84, 0, 1, 1, 1)

        self.label_60 = QLabel(self._vol_grp)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font2)

        self.gridLayout_18.addWidget(self.label_60, 2, 0, 1, 1)

        self.line_88 = QFrame(self._vol_grp)
        self.line_88.setObjectName(u"line_88")
        self.line_88.setMinimumSize(QSize(20, 0))
        self.line_88.setFrameShape(QFrame.Shape.VLine)
        self.line_88.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_18.addWidget(self.line_88, 2, 1, 1, 1)

        self.label_61 = QLabel(self._vol_grp)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font2)

        self.gridLayout_18.addWidget(self.label_61, 3, 0, 1, 1)

        self.line_85 = QFrame(self._vol_grp)
        self.line_85.setObjectName(u"line_85")
        self.line_85.setMinimumSize(QSize(20, 0))
        self.line_85.setFrameShape(QFrame.Shape.VLine)
        self.line_85.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_18.addWidget(self.line_85, 1, 1, 1, 1)

        self._volDiv = QComboBox(self._vol_grp)
        self._volDiv.setObjectName(u"_volDiv")

        self.gridLayout_18.addWidget(self._volDiv, 0, 2, 1, 1)

        self.label_58 = QLabel(self._vol_grp)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font2)

        self.gridLayout_18.addWidget(self.label_58, 1, 0, 1, 1)

        self._volCmap = QComboBox(self._vol_grp)
        self._volCmap.setObjectName(u"_volCmap")

        self.gridLayout_18.addWidget(self._volCmap, 2, 2, 1, 1)

        self.label_57 = QLabel(self._vol_grp)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font2)

        self.gridLayout_18.addWidget(self.label_57, 0, 0, 1, 1)

        self.line_89 = QFrame(self._vol_grp)
        self.line_89.setObjectName(u"line_89")
        self.line_89.setMinimumSize(QSize(20, 0))
        self.line_89.setFrameShape(QFrame.Shape.VLine)
        self.line_89.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_18.addWidget(self.line_89, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_3, 4, 2, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_18)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_5)


        self.verticalLayout_14.addWidget(self._vol_grp)

        self._obj_stack.addWidget(self._volume_page)
        self._crossec_page = QWidget()
        self._crossec_page.setObjectName(u"_crossec_page")
        self.verticalLayout_15 = QVBoxLayout(self._crossec_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self._sec_grp = QGroupBox(self._crossec_page)
        self._sec_grp.setObjectName(u"_sec_grp")
        self._sec_grp.setCheckable(True)
        self._sec_grp.setChecked(False)
        self.verticalLayout_19 = QVBoxLayout(self._sec_grp)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 9, 0, 9)
        self.line_47 = QFrame(self._sec_grp)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setMinimumSize(QSize(200, 0))
        self.line_47.setFrameShape(QFrame.Shape.HLine)
        self.line_47.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_47)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.line_75 = QFrame(self._sec_grp)
        self.line_75.setObjectName(u"line_75")
        self.line_75.setMinimumSize(QSize(20, 0))
        self.line_75.setFrameShape(QFrame.Shape.VLine)
        self.line_75.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_75, 1, 1, 1, 1)

        self._csAxial = QSlider(self._sec_grp)
        self._csAxial.setObjectName(u"_csAxial")
        self._csAxial.setMinimum(-5)
        self._csAxial.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self._csAxial, 5, 2, 1, 1)

        self.label_46 = QLabel(self._sec_grp)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font2)

        self.gridLayout_10.addWidget(self.label_46, 4, 0, 1, 1)

        self.line_71 = QFrame(self._sec_grp)
        self.line_71.setObjectName(u"line_71")
        self.line_71.setMinimumSize(QSize(20, 0))
        self.line_71.setFrameShape(QFrame.Shape.VLine)
        self.line_71.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_71, 5, 1, 1, 1)

        self.label_50 = QLabel(self._sec_grp)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font2)

        self.gridLayout_10.addWidget(self.label_50, 1, 0, 1, 1)

        self.line_73 = QFrame(self._sec_grp)
        self.line_73.setObjectName(u"line_73")
        self.line_73.setMinimumSize(QSize(20, 0))
        self.line_73.setFrameShape(QFrame.Shape.VLine)
        self.line_73.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_73, 0, 1, 1, 1)

        self._csCoron = QSlider(self._sec_grp)
        self._csCoron.setObjectName(u"_csCoron")
        self._csCoron.setMinimum(-5)
        self._csCoron.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self._csCoron, 4, 2, 1, 1)

        self.label_47 = QLabel(self._sec_grp)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font2)

        self.gridLayout_10.addWidget(self.label_47, 5, 0, 1, 1)

        self._csDiv = QComboBox(self._sec_grp)
        self._csDiv.setObjectName(u"_csDiv")

        self.gridLayout_10.addWidget(self._csDiv, 0, 2, 1, 1)

        self.line_69 = QFrame(self._sec_grp)
        self.line_69.setObjectName(u"line_69")
        self.line_69.setMinimumSize(QSize(20, 0))
        self.line_69.setFrameShape(QFrame.Shape.VLine)
        self.line_69.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_69, 4, 1, 1, 1)

        self.line_48 = QFrame(self._sec_grp)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setMinimumSize(QSize(20, 0))
        self.line_48.setFrameShape(QFrame.Shape.VLine)
        self.line_48.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_48, 3, 1, 1, 1)

        self._csSagit = QSlider(self._sec_grp)
        self._csSagit.setObjectName(u"_csSagit")
        self._csSagit.setMinimum(-5)
        self._csSagit.setOrientation(Qt.Horizontal)
        self._csSagit.setInvertedAppearance(False)
        self._csSagit.setInvertedControls(False)

        self.gridLayout_10.addWidget(self._csSagit, 3, 2, 1, 1)

        self.label_44 = QLabel(self._sec_grp)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font2)

        self.gridLayout_10.addWidget(self.label_44, 3, 0, 1, 1)

        self.label_49 = QLabel(self._sec_grp)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font2)

        self.gridLayout_10.addWidget(self.label_49, 0, 0, 1, 1)

        self.widget_5 = QWidget(self._sec_grp)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")

        self.gridLayout_10.addWidget(self.widget_5, 6, 0, 1, 3)

        self.line_80 = QFrame(self._sec_grp)
        self.line_80.setObjectName(u"line_80")
        self.line_80.setMinimumSize(QSize(20, 0))
        self.line_80.setFrameShape(QFrame.Shape.VLine)
        self.line_80.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_80, 2, 1, 1, 1)

        self.label_55 = QLabel(self._sec_grp)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font2)

        self.gridLayout_10.addWidget(self.label_55, 2, 0, 1, 1)

        self._csLevel = QComboBox(self._sec_grp)
        self._csLevel.addItem("")
        self._csLevel.addItem("")
        self._csLevel.addItem("")
        self._csLevel.addItem("")
        self._csLevel.addItem("")
        self._csLevel.addItem("")
        self._csLevel.addItem("")
        self._csLevel.setObjectName(u"_csLevel")
        self._csLevel.setEnabled(False)

        self.gridLayout_10.addWidget(self._csLevel, 1, 2, 1, 1)

        self._csInterp = QComboBox(self._sec_grp)
        self._csInterp.addItem("")
        self._csInterp.addItem("")
        self._csInterp.addItem("")
        self._csInterp.addItem("")
        self._csInterp.addItem("")
        self._csInterp.addItem("")
        self._csInterp.addItem("")
        self._csInterp.addItem("")
        self._csInterp.setObjectName(u"_csInterp")

        self.gridLayout_10.addWidget(self._csInterp, 2, 2, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_10)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_7)


        self.verticalLayout_15.addWidget(self._sec_grp)

        self._obj_stack.addWidget(self._crossec_page)
        self._sources_page = QWidget()
        self._sources_page.setObjectName(u"_sources_page")
        self.verticalLayout_9 = QVBoxLayout(self._sources_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self._source_tab = QTabWidget(self._sources_page)
        self._source_tab.setObjectName(u"_source_tab")
        self._source_tab.setFocusPolicy(Qt.StrongFocus)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_24 = QVBoxLayout(self.tab_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.scrollArea_2 = QScrollArea(self.tab_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 312, 392))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self._s_grp = QGroupBox(self.scrollAreaWidgetContents_2)
        self._s_grp.setObjectName(u"_s_grp")
        self._s_grp.setCheckable(True)
        self.verticalLayout_35 = QVBoxLayout(self._s_grp)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, -1, 0, -1)
        self.line_20 = QFrame(self._s_grp)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setMinimumSize(QSize(200, 0))
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_35.addWidget(self.line_20)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.line_23 = QFrame(self._s_grp)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setMinimumSize(QSize(20, 0))
        self.line_23.setFrameShape(QFrame.Shape.VLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_23, 3, 1, 1, 1)

        self._s_select = QComboBox(self._s_grp)
        self._s_select.addItem("")
        self._s_select.addItem("")
        self._s_select.addItem("")
        self._s_select.addItem("")
        self._s_select.addItem("")
        self._s_select.addItem("")
        self._s_select.setObjectName(u"_s_select")

        self.gridLayout_15.addWidget(self._s_select, 0, 2, 1, 1)

        self._s_symbol = QComboBox(self._s_grp)
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.addItem("")
        self._s_symbol.setObjectName(u"_s_symbol")

        self.gridLayout_15.addWidget(self._s_symbol, 1, 2, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self._s_radiusmin = QDoubleSpinBox(self._s_grp)
        self._s_radiusmin.setObjectName(u"_s_radiusmin")
        self._s_radiusmin.setDecimals(1)

        self.horizontalLayout_14.addWidget(self._s_radiusmin)

        self._s_radiusmax = QDoubleSpinBox(self._s_grp)
        self._s_radiusmax.setObjectName(u"_s_radiusmax")
        self._s_radiusmax.setDecimals(1)

        self.horizontalLayout_14.addWidget(self._s_radiusmax)


        self.gridLayout_15.addLayout(self.horizontalLayout_14, 2, 2, 1, 1)

        self.line_25 = QFrame(self._s_grp)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setMinimumSize(QSize(20, 0))
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_25, 1, 1, 1, 1)

        self.line_24 = QFrame(self._s_grp)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setMinimumSize(QSize(20, 0))
        self.line_24.setFrameShape(QFrame.Shape.VLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_24, 2, 1, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_17 = QLabel(self._s_grp)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_17.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_20 = QLabel(self._s_grp)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_17.addWidget(self.label_20, 1, 0, 1, 1)

        self._s_edge_width = QDoubleSpinBox(self._s_grp)
        self._s_edge_width.setObjectName(u"_s_edge_width")
        self._s_edge_width.setDecimals(1)

        self.gridLayout_17.addWidget(self._s_edge_width, 1, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self._s_edge_color = QLineEdit(self._s_grp)
        self._s_edge_color.setObjectName(u"_s_edge_color")

        self.horizontalLayout_16.addWidget(self._s_edge_color)

        self._s_edge_color_p = QToolButton(self._s_grp)
        self._s_edge_color_p.setObjectName(u"_s_edge_color_p")

        self.horizontalLayout_16.addWidget(self._s_edge_color_p)


        self.gridLayout_17.addLayout(self.horizontalLayout_16, 0, 1, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_17, 3, 2, 1, 1)

        self.label_28 = QLabel(self._s_grp)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.gridLayout_15.addWidget(self.label_28, 1, 0, 1, 1)

        self.label_32 = QLabel(self._s_grp)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)

        self.gridLayout_15.addWidget(self.label_32, 2, 0, 1, 1)

        self.line_28 = QFrame(self._s_grp)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setMinimumSize(QSize(20, 0))
        self.line_28.setFrameShape(QFrame.Shape.VLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_28, 0, 1, 1, 1)

        self.label_27 = QLabel(self._s_grp)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.gridLayout_15.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_31 = QLabel(self._s_grp)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.gridLayout_15.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_39 = QLabel(self._s_grp)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.gridLayout_15.addWidget(self.label_39, 4, 0, 1, 1)

        self.line_49 = QFrame(self._s_grp)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setMinimumSize(QSize(20, 0))
        self.line_49.setFrameShape(QFrame.Shape.VLine)
        self.line_49.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_49, 4, 1, 1, 1)

        self._s_alpha = QSlider(self._s_grp)
        self._s_alpha.setObjectName(u"_s_alpha")
        self._s_alpha.setMaximum(99)
        self._s_alpha.setSliderPosition(99)
        self._s_alpha.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self._s_alpha, 4, 2, 1, 1)


        self.verticalLayout_35.addLayout(self.gridLayout_15)


        self.verticalLayout_12.addWidget(self._s_grp)

        self._st_grp = QGroupBox(self.scrollAreaWidgetContents_2)
        self._st_grp.setObjectName(u"_st_grp")
        self._st_grp.setEnabled(True)
        self._st_grp.setCheckable(False)
        self.verticalLayout_6 = QVBoxLayout(self._st_grp)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.line_39 = QFrame(self._st_grp)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setMinimumSize(QSize(200, 0))
        self.line_39.setFrameShape(QFrame.Shape.HLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_39)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_30 = QLabel(self._st_grp)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.gridLayout_7.addWidget(self.label_30, 2, 0, 1, 1)

        self.line_38 = QFrame(self._st_grp)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setMinimumSize(QSize(20, 0))
        self.line_38.setFrameShape(QFrame.Shape.VLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_38, 2, 1, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self._st_color = QLineEdit(self._st_grp)
        self._st_color.setObjectName(u"_st_color")

        self.horizontalLayout_18.addWidget(self._st_color)

        self._st_color_p = QToolButton(self._st_grp)
        self._st_color_p.setObjectName(u"_st_color_p")

        self.horizontalLayout_18.addWidget(self._st_color_p)


        self.gridLayout_7.addLayout(self.horizontalLayout_18, 1, 2, 1, 1)

        self.line_37 = QFrame(self._st_grp)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setMinimumSize(QSize(20, 0))
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_37, 0, 1, 1, 1)

        self.label_14 = QLabel(self._st_grp)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.gridLayout_7.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_12 = QLabel(self._st_grp)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)

        self._st_font_size = QDoubleSpinBox(self._st_grp)
        self._st_font_size.setObjectName(u"_st_font_size")
        self._st_font_size.setDecimals(1)

        self.gridLayout_7.addWidget(self._st_font_size, 0, 2, 1, 1)

        self.line_51 = QFrame(self._st_grp)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setMinimumSize(QSize(20, 0))
        self.line_51.setFrameShape(QFrame.Shape.VLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_51, 1, 1, 1, 1)

        self.widget_2 = QWidget(self._st_grp)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self._st_dx = QDoubleSpinBox(self.widget_2)
        self._st_dx.setObjectName(u"_st_dx")
        self._st_dx.setDecimals(1)
        self._st_dx.setMinimum(-100.000000000000000)
        self._st_dx.setMaximum(100.000000000000000)

        self.horizontalLayout_3.addWidget(self._st_dx)

        self._st_dy = QDoubleSpinBox(self.widget_2)
        self._st_dy.setObjectName(u"_st_dy")
        self._st_dy.setDecimals(1)
        self._st_dy.setMinimum(-100.000000000000000)
        self._st_dy.setMaximum(100.000000000000000)

        self.horizontalLayout_3.addWidget(self._st_dy)

        self._st_dz = QDoubleSpinBox(self.widget_2)
        self._st_dz.setObjectName(u"_st_dz")
        self._st_dz.setDecimals(1)
        self._st_dz.setMinimum(-100.000000000000000)
        self._st_dz.setMaximum(100.000000000000000)

        self.horizontalLayout_3.addWidget(self._st_dz)


        self.gridLayout_7.addWidget(self.widget_2, 2, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_7)


        self.verticalLayout_12.addWidget(self._st_grp)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_24.addWidget(self.scrollArea_2)

        self._source_tab.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_29 = QVBoxLayout(self.tab_5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.groupBox_6 = QGroupBox(self.tab_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.line_40 = QFrame(self.groupBox_6)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setMinimumSize(QSize(200, 0))
        self.line_40.setFrameShape(QFrame.Shape.HLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_40)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.gridLayout_8.addWidget(self.label_15, 0, 0, 1, 1)

        self._s_proj_radius = QDoubleSpinBox(self.groupBox_6)
        self._s_proj_radius.setObjectName(u"_s_proj_radius")
        self._s_proj_radius.setDecimals(1)
        self._s_proj_radius.setValue(10.000000000000000)

        self.gridLayout_8.addWidget(self._s_proj_radius, 0, 2, 1, 1)

        self.line_52 = QFrame(self.groupBox_6)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setMinimumSize(QSize(20, 0))
        self.line_52.setFrameShape(QFrame.Shape.VLine)
        self.line_52.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_8.addWidget(self.line_52, 0, 1, 1, 1)

        self.line_53 = QFrame(self.groupBox_6)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setMinimumSize(QSize(20, 0))
        self.line_53.setFrameShape(QFrame.Shape.VLine)
        self.line_53.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_8.addWidget(self.line_53, 1, 1, 1, 1)

        self.label_115 = QLabel(self.groupBox_6)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setFont(font2)

        self.gridLayout_8.addWidget(self.label_115, 1, 0, 1, 1)

        self.line_54 = QFrame(self.groupBox_6)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setMinimumSize(QSize(20, 0))
        self.line_54.setFrameShape(QFrame.Shape.VLine)
        self.line_54.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_8.addWidget(self.line_54, 2, 1, 1, 1)

        self.label_116 = QLabel(self.groupBox_6)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setFont(font2)

        self.gridLayout_8.addWidget(self.label_116, 2, 0, 1, 1)

        self._s_proj_on = QComboBox(self.groupBox_6)
        self._s_proj_on.addItem("")
        self._s_proj_on.addItem("")
        self._s_proj_on.setObjectName(u"_s_proj_on")

        self.gridLayout_8.addWidget(self._s_proj_on, 2, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_11, 5, 2, 1, 1)

        self._s_proj_contribute = QCheckBox(self.groupBox_6)
        self._s_proj_contribute.setObjectName(u"_s_proj_contribute")
        self._s_proj_contribute.setFont(font2)

        self.gridLayout_8.addWidget(self._s_proj_contribute, 4, 0, 1, 3)

        self._s_proj_type = QComboBox(self.groupBox_6)
        self._s_proj_type.addItem("")
        self._s_proj_type.addItem("")
        self._s_proj_type.setObjectName(u"_s_proj_type")

        self.gridLayout_8.addWidget(self._s_proj_type, 1, 2, 1, 1)

        self.label_117 = QLabel(self.groupBox_6)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setFont(font2)

        self.gridLayout_8.addWidget(self.label_117, 3, 0, 1, 1)

        self.line_56 = QFrame(self.groupBox_6)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setMinimumSize(QSize(20, 0))
        self.line_56.setFrameShape(QFrame.Shape.VLine)
        self.line_56.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_8.addWidget(self.line_56, 3, 1, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self._s_proj_mask_color = QLineEdit(self.groupBox_6)
        self._s_proj_mask_color.setObjectName(u"_s_proj_mask_color")

        self.horizontalLayout_19.addWidget(self._s_proj_mask_color)

        self._s_proj_mask_color_p = QToolButton(self.groupBox_6)
        self._s_proj_mask_color_p.setObjectName(u"_s_proj_mask_color_p")

        self.horizontalLayout_19.addWidget(self._s_proj_mask_color_p)


        self.gridLayout_8.addLayout(self.horizontalLayout_19, 3, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_8)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_24)

        self._s_proj_apply = QPushButton(self.groupBox_6)
        self._s_proj_apply.setObjectName(u"_s_proj_apply")
        self._s_proj_apply.setEnabled(True)

        self.horizontalLayout_8.addWidget(self._s_proj_apply)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)


        self.verticalLayout_29.addWidget(self.groupBox_6)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_6)

        self._source_tab.addTab(self.tab_5, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_25 = QVBoxLayout(self.tab_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self._s_table = QTableWidget(self.tab_3)
        self._s_table.setObjectName(u"_s_table")
        self._s_table.setEnabled(False)
        self._s_table.setAlternatingRowColors(True)
        self._s_table.setSortingEnabled(False)
        self._s_table.setCornerButtonEnabled(False)

        self.verticalLayout_25.addWidget(self._s_table)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, -1, -1)
        self._s_analyse_run = QPushButton(self.tab_3)
        self._s_analyse_run.setObjectName(u"_s_analyse_run")

        self.gridLayout_6.addWidget(self._s_analyse_run, 1, 3, 1, 1)

        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)

        self.gridLayout_6.addWidget(self.label_24, 0, 0, 2, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 3, 2, 1, 1)

        self._s_analyse_roi = QComboBox(self.tab_3)
        self._s_analyse_roi.addItem("")
        self._s_analyse_roi.addItem("")
        self._s_analyse_roi.addItem("")
        self._s_analyse_roi.setObjectName(u"_s_analyse_roi")

        self.gridLayout_6.addWidget(self._s_analyse_roi, 1, 2, 1, 1)

        self.line_5 = QFrame(self.tab_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_5, 0, 1, 2, 2)

        self.line_6 = QFrame(self.tab_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_6, 2, 1, 1, 1)

        self.label_29 = QLabel(self.tab_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.gridLayout_6.addWidget(self.label_29, 2, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)

        self._s_show_cs = QPushButton(self.tab_3)
        self._s_show_cs.setObjectName(u"_s_show_cs")

        self.horizontalLayout_20.addWidget(self._s_show_cs)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_5)


        self.gridLayout_6.addLayout(self.horizontalLayout_20, 2, 2, 1, 2)


        self.verticalLayout_25.addLayout(self.gridLayout_6)

        self._source_tab.addTab(self.tab_3, "")

        self.verticalLayout_9.addWidget(self._source_tab)

        self._obj_stack.addWidget(self._sources_page)
        self._connect_page = QWidget()
        self._connect_page.setObjectName(u"_connect_page")
        self.verticalLayout_20 = QVBoxLayout(self._connect_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self._c_grp = QGroupBox(self._connect_page)
        self._c_grp.setObjectName(u"_c_grp")
        self._c_grp.setFont(font)
        self._c_grp.setCheckable(True)
        self.verticalLayout_39 = QVBoxLayout(self._c_grp)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, -1, 0, -1)
        self.line_42 = QFrame(self._c_grp)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setMinimumSize(QSize(200, 0))
        self.line_42.setFrameShape(QFrame.Shape.HLine)
        self.line_42.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_39.addWidget(self.line_42)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self._c_dyn_meth = QComboBox(self._c_grp)
        self._c_dyn_meth.addItem("")
        self._c_dyn_meth.addItem("")
        self._c_dyn_meth.setObjectName(u"_c_dyn_meth")

        self.gridLayout_14.addWidget(self._c_dyn_meth, 1, 1, 1, 1)

        self.label_110 = QLabel(self._c_grp)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setFont(font2)

        self.gridLayout_14.addWidget(self.label_110, 0, 0, 1, 1)

        self._c_alpha_stack = QStackedWidget(self._c_grp)
        self._c_alpha_stack.setObjectName(u"_c_alpha_stack")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self._c_alpha_stack.sizePolicy().hasHeightForWidth())
        self._c_alpha_stack.setSizePolicy(sizePolicy2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout = QHBoxLayout(self.page_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_38 = QLabel(self.page_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)

        self.horizontalLayout.addWidget(self.label_38)

        self._c_alpha = QSlider(self.page_4)
        self._c_alpha.setObjectName(u"_c_alpha")
        self._c_alpha.setMaximum(99)
        self._c_alpha.setSliderPosition(99)
        self._c_alpha.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self._c_alpha)

        self._c_alpha_stack.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout = QGridLayout(self.page_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_23 = QLabel(self.page_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.gridLayout.addWidget(self.label_23, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self._c_dyn_min = QDoubleSpinBox(self.page_5)
        self._c_dyn_min.setObjectName(u"_c_dyn_min")
        self._c_dyn_min.setDecimals(1)
        self._c_dyn_min.setMinimum(0.100000000000000)
        self._c_dyn_min.setMaximum(1.000000000000000)
        self._c_dyn_min.setSingleStep(0.100000000000000)

        self.horizontalLayout_5.addWidget(self._c_dyn_min)

        self._c_dyn_max = QDoubleSpinBox(self.page_5)
        self._c_dyn_max.setObjectName(u"_c_dyn_max")
        self._c_dyn_max.setDecimals(1)
        self._c_dyn_max.setMaximum(1.000000000000000)
        self._c_dyn_max.setSingleStep(0.100000000000000)
        self._c_dyn_max.setValue(1.000000000000000)

        self.horizontalLayout_5.addWidget(self._c_dyn_max)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 1, 1, 1)

        self._c_alpha_stack.addWidget(self.page_5)

        self.gridLayout_14.addWidget(self._c_alpha_stack, 3, 0, 1, 2)

        self._c_colorby = QComboBox(self._c_grp)
        self._c_colorby.addItem("")
        self._c_colorby.addItem("")
        self._c_colorby.addItem("")
        self._c_colorby.setObjectName(u"_c_colorby")

        self.gridLayout_14.addWidget(self._c_colorby, 0, 1, 1, 1)

        self.label_37 = QLabel(self._c_grp)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)

        self.gridLayout_14.addWidget(self.label_37, 1, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_14, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_14, 0, 2, 1, 1)

        self.line_26 = QFrame(self._c_grp)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setMinimumSize(QSize(20, 0))
        self.line_26.setFrameShape(QFrame.Shape.VLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_26, 1, 1, 1, 1)

        self.label_109 = QLabel(self._c_grp)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font2)

        self.gridLayout_3.addWidget(self.label_109, 0, 0, 1, 1)

        self.label_22 = QLabel(self._c_grp)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.gridLayout_3.addWidget(self.label_22, 1, 0, 1, 1)

        self._c_line_width = QDoubleSpinBox(self._c_grp)
        self._c_line_width.setObjectName(u"_c_line_width")
        self._c_line_width.setDecimals(1)
        self._c_line_width.setMinimum(0.100000000000000)
        self._c_line_width.setMaximum(20.000000000000000)
        self._c_line_width.setSingleStep(1.000000000000000)
        self._c_line_width.setValue(4.000000000000000)

        self.gridLayout_3.addWidget(self._c_line_width, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.line_22 = QFrame(self._c_grp)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setMinimumSize(QSize(20, 0))
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_22, 0, 1, 1, 1)


        self.verticalLayout_39.addLayout(self.gridLayout_3)


        self.verticalLayout_20.addWidget(self._c_grp)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_9)

        self._obj_stack.addWidget(self._connect_page)
        self._ts_page = QWidget()
        self._ts_page.setObjectName(u"_ts_page")
        self.verticalLayout_21 = QVBoxLayout(self._ts_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self._ts_grp = QGroupBox(self._ts_page)
        self._ts_grp.setObjectName(u"_ts_grp")
        self._ts_grp.setMinimumSize(QSize(0, 0))
        self._ts_grp.setFlat(False)
        self._ts_grp.setCheckable(True)
        self.verticalLayout_16 = QVBoxLayout(self._ts_grp)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, 0, -1)
        self.line_41 = QFrame(self._ts_grp)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setMinimumSize(QSize(200, 0))
        self.line_41.setFrameShape(QFrame.Shape.HLine)
        self.line_41.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.line_41)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self._ts_color = QLineEdit(self._ts_grp)
        self._ts_color.setObjectName(u"_ts_color")

        self.horizontalLayout_12.addWidget(self._ts_color)

        self._ts_color_p = QToolButton(self._ts_grp)
        self._ts_color_p.setObjectName(u"_ts_color_p")

        self.horizontalLayout_12.addWidget(self._ts_color_p)


        self.gridLayout_4.addLayout(self.horizontalLayout_12, 3, 2, 1, 1)

        self._ts_width = QDoubleSpinBox(self._ts_grp)
        self._ts_width.setObjectName(u"_ts_width")
        self._ts_width.setDecimals(1)

        self.gridLayout_4.addWidget(self._ts_width, 0, 2, 1, 1)

        self.label_41 = QLabel(self._ts_grp)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font2)

        self.gridLayout_4.addWidget(self.label_41, 5, 0, 1, 1)

        self.label_10 = QLabel(self._ts_grp)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.line_65 = QFrame(self._ts_grp)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setMinimumSize(QSize(20, 0))
        self.line_65.setFrameShape(QFrame.Shape.VLine)
        self.line_65.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_65, 5, 1, 1, 1)

        self.label_18 = QLabel(self._ts_grp)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)

        self.line_63 = QFrame(self._ts_grp)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setMinimumSize(QSize(20, 0))
        self.line_63.setFrameShape(QFrame.Shape.VLine)
        self.line_63.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_63, 1, 1, 1, 1)

        self.label_11 = QLabel(self._ts_grp)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.line_64 = QFrame(self._ts_grp)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setMinimumSize(QSize(20, 0))
        self.line_64.setFrameShape(QFrame.Shape.VLine)
        self.line_64.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_64, 3, 1, 1, 1)

        self.line_62 = QFrame(self._ts_grp)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setMinimumSize(QSize(20, 0))
        self.line_62.setFrameShape(QFrame.Shape.VLine)
        self.line_62.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_62, 0, 1, 1, 1)

        self._ts_amp = QDoubleSpinBox(self._ts_grp)
        self._ts_amp.setObjectName(u"_ts_amp")
        self._ts_amp.setDecimals(1)

        self.gridLayout_4.addWidget(self._ts_amp, 1, 2, 1, 1)

        self.label_25 = QLabel(self._ts_grp)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.gridLayout_4.addWidget(self.label_25, 2, 0, 1, 1)

        self.line_66 = QFrame(self._ts_grp)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setMinimumSize(QSize(20, 0))
        self.line_66.setFrameShape(QFrame.Shape.VLine)
        self.line_66.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_66, 2, 1, 1, 1)

        self._ts_line_width = QDoubleSpinBox(self._ts_grp)
        self._ts_line_width.setObjectName(u"_ts_line_width")
        self._ts_line_width.setDecimals(1)

        self.gridLayout_4.addWidget(self._ts_line_width, 2, 2, 1, 1)

        self.widget = QWidget(self._ts_grp)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
#ifndef Q_OS_MAC
        self.horizontalLayout_4.setSpacing(6)
#endif
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self._ts_dx = QDoubleSpinBox(self.widget)
        self._ts_dx.setObjectName(u"_ts_dx")
        self._ts_dx.setDecimals(1)
        self._ts_dx.setMinimum(-100.000000000000000)
        self._ts_dx.setMaximum(100.000000000000000)

        self.horizontalLayout_4.addWidget(self._ts_dx)

        self._ts_dy = QDoubleSpinBox(self.widget)
        self._ts_dy.setObjectName(u"_ts_dy")
        self._ts_dy.setDecimals(1)
        self._ts_dy.setMinimum(-100.000000000000000)
        self._ts_dy.setMaximum(100.000000000000000)

        self.horizontalLayout_4.addWidget(self._ts_dy)

        self._ts_dz = QDoubleSpinBox(self.widget)
        self._ts_dz.setObjectName(u"_ts_dz")
        self._ts_dz.setDecimals(1)
        self._ts_dz.setMinimum(-100.000000000000000)
        self._ts_dz.setMaximum(100.000000000000000)

        self.horizontalLayout_4.addWidget(self._ts_dz)


        self.gridLayout_4.addWidget(self.widget, 5, 2, 1, 1)

        self.label_21 = QLabel(self._ts_grp)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.gridLayout_4.addWidget(self.label_21, 4, 0, 1, 1)

        self.line_72 = QFrame(self._ts_grp)
        self.line_72.setObjectName(u"line_72")
        self.line_72.setMinimumSize(QSize(20, 0))
        self.line_72.setFrameShape(QFrame.Shape.VLine)
        self.line_72.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_72, 4, 1, 1, 1)

        self._ts_alpha = QSlider(self._ts_grp)
        self._ts_alpha.setObjectName(u"_ts_alpha")
        self._ts_alpha.setMaximum(99)
        self._ts_alpha.setSliderPosition(99)
        self._ts_alpha.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self._ts_alpha, 4, 2, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_4)


        self.verticalLayout_21.addWidget(self._ts_grp)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_8)

        self._obj_stack.addWidget(self._ts_page)
        self._pic_page = QWidget()
        self._pic_page.setObjectName(u"_pic_page")
        self.verticalLayout_28 = QVBoxLayout(self._pic_page)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self._pic_grp = QGroupBox(self._pic_page)
        self._pic_grp.setObjectName(u"_pic_grp")
        self._pic_grp.setMinimumSize(QSize(0, 0))
        self._pic_grp.setFlat(False)
        self._pic_grp.setCheckable(True)
        self.verticalLayout_17 = QVBoxLayout(self._pic_grp)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, -1)
        self.line_46 = QFrame(self._pic_grp)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setMinimumSize(QSize(200, 0))
        self.line_46.setFrameShape(QFrame.Shape.HLine)
        self.line_46.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_46)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self._pic_width = QDoubleSpinBox(self._pic_grp)
        self._pic_width.setObjectName(u"_pic_width")
        self._pic_width.setDecimals(1)

        self.gridLayout_9.addWidget(self._pic_width, 0, 2, 1, 1)

        self.label_42 = QLabel(self._pic_grp)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font2)

        self.gridLayout_9.addWidget(self.label_42, 3, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_7, 4, 2, 1, 1)

        self.label_43 = QLabel(self._pic_grp)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font2)

        self.gridLayout_9.addWidget(self.label_43, 0, 0, 1, 1)

        self.line_67 = QFrame(self._pic_grp)
        self.line_67.setObjectName(u"line_67")
        self.line_67.setMinimumSize(QSize(20, 0))
        self.line_67.setFrameShape(QFrame.Shape.VLine)
        self.line_67.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_67, 3, 1, 1, 1)

        self.line_68 = QFrame(self._pic_grp)
        self.line_68.setObjectName(u"line_68")
        self.line_68.setMinimumSize(QSize(20, 0))
        self.line_68.setFrameShape(QFrame.Shape.VLine)
        self.line_68.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_68, 1, 1, 1, 1)

        self.label_45 = QLabel(self._pic_grp)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font2)

        self.gridLayout_9.addWidget(self.label_45, 1, 0, 1, 1)

        self.line_70 = QFrame(self._pic_grp)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setMinimumSize(QSize(20, 0))
        self.line_70.setFrameShape(QFrame.Shape.VLine)
        self.line_70.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_70, 0, 1, 1, 1)

        self._pic_height = QDoubleSpinBox(self._pic_grp)
        self._pic_height.setObjectName(u"_pic_height")
        self._pic_height.setDecimals(1)

        self.gridLayout_9.addWidget(self._pic_height, 1, 2, 1, 1)

        self.widget_3 = QWidget(self._pic_grp)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
#ifndef Q_OS_MAC
        self.horizontalLayout_6.setSpacing(6)
#endif
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self._pic_dx = QDoubleSpinBox(self.widget_3)
        self._pic_dx.setObjectName(u"_pic_dx")
        self._pic_dx.setDecimals(1)
        self._pic_dx.setMinimum(-100.000000000000000)
        self._pic_dx.setMaximum(100.000000000000000)

        self.horizontalLayout_17.addWidget(self._pic_dx)

        self._pic_dy = QDoubleSpinBox(self.widget_3)
        self._pic_dy.setObjectName(u"_pic_dy")
        self._pic_dy.setDecimals(1)
        self._pic_dy.setMinimum(-100.000000000000000)
        self._pic_dy.setMaximum(100.000000000000000)

        self.horizontalLayout_17.addWidget(self._pic_dy)

        self._pic_dz = QDoubleSpinBox(self.widget_3)
        self._pic_dz.setObjectName(u"_pic_dz")
        self._pic_dz.setDecimals(1)
        self._pic_dz.setMinimum(-100.000000000000000)
        self._pic_dz.setMaximum(100.000000000000000)

        self.horizontalLayout_17.addWidget(self._pic_dz)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_17)


        self.gridLayout_9.addWidget(self.widget_3, 3, 2, 1, 1)

        self.label_48 = QLabel(self._pic_grp)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font2)

        self.gridLayout_9.addWidget(self.label_48, 2, 0, 1, 1)

        self.line_74 = QFrame(self._pic_grp)
        self.line_74.setObjectName(u"line_74")
        self.line_74.setMinimumSize(QSize(20, 0))
        self.line_74.setFrameShape(QFrame.Shape.VLine)
        self.line_74.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_74, 2, 1, 1, 1)

        self._pic_alpha = QSlider(self._pic_grp)
        self._pic_alpha.setObjectName(u"_pic_alpha")
        self._pic_alpha.setMaximum(99)
        self._pic_alpha.setSliderPosition(99)
        self._pic_alpha.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self._pic_alpha, 2, 2, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout_9)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_10)


        self.verticalLayout_28.addWidget(self._pic_grp)

        self._obj_stack.addWidget(self._pic_page)
        self._vec_page = QWidget()
        self._vec_page.setObjectName(u"_vec_page")
        self.verticalLayout = QVBoxLayout(self._vec_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self._vec_grp = QGroupBox(self._vec_page)
        self._vec_grp.setObjectName(u"_vec_grp")
        self._vec_grp.setMinimumSize(QSize(0, 0))
        self._vec_grp.setFlat(False)
        self._vec_grp.setCheckable(True)
        self.verticalLayout_18 = QVBoxLayout(self._vec_grp)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, -1, 0, -1)
        self.line_50 = QFrame(self._vec_grp)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setMinimumSize(QSize(200, 0))
        self.line_50.setFrameShape(QFrame.Shape.HLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_18.addWidget(self.line_50)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.line_79 = QFrame(self._vec_grp)
        self.line_79.setObjectName(u"line_79")
        self.line_79.setMinimumSize(QSize(20, 0))
        self.line_79.setFrameShape(QFrame.Shape.VLine)
        self.line_79.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line_79, 2, 1, 1, 1)

        self._vec_line_width = QDoubleSpinBox(self._vec_grp)
        self._vec_line_width.setObjectName(u"_vec_line_width")
        self._vec_line_width.setDecimals(1)
        self._vec_line_width.setMinimum(1.000000000000000)

        self.gridLayout_11.addWidget(self._vec_line_width, 0, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_10, 4, 2, 1, 1)

        self.label_51 = QLabel(self._vec_grp)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font2)

        self.gridLayout_11.addWidget(self.label_51, 0, 0, 1, 1)

        self.line_76 = QFrame(self._vec_grp)
        self.line_76.setObjectName(u"line_76")
        self.line_76.setMinimumSize(QSize(20, 0))
        self.line_76.setFrameShape(QFrame.Shape.VLine)
        self.line_76.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line_76, 1, 1, 1, 1)

        self.label_52 = QLabel(self._vec_grp)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font2)

        self.gridLayout_11.addWidget(self.label_52, 1, 0, 1, 1)

        self.line_77 = QFrame(self._vec_grp)
        self.line_77.setObjectName(u"line_77")
        self.line_77.setMinimumSize(QSize(20, 0))
        self.line_77.setFrameShape(QFrame.Shape.VLine)
        self.line_77.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line_77, 0, 1, 1, 1)

        self._vec_arrow_size = QDoubleSpinBox(self._vec_grp)
        self._vec_arrow_size.setObjectName(u"_vec_arrow_size")
        self._vec_arrow_size.setDecimals(1)
        self._vec_arrow_size.setMinimum(1.000000000000000)

        self.gridLayout_11.addWidget(self._vec_arrow_size, 1, 2, 1, 1)

        self.label_53 = QLabel(self._vec_grp)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font2)

        self.gridLayout_11.addWidget(self.label_53, 3, 0, 1, 1)

        self.line_78 = QFrame(self._vec_grp)
        self.line_78.setObjectName(u"line_78")
        self.line_78.setMinimumSize(QSize(20, 0))
        self.line_78.setFrameShape(QFrame.Shape.VLine)
        self.line_78.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line_78, 3, 1, 1, 1)

        self._vec_alpha = QSlider(self._vec_grp)
        self._vec_alpha.setObjectName(u"_vec_alpha")
        self._vec_alpha.setMaximum(99)
        self._vec_alpha.setSliderPosition(99)
        self._vec_alpha.setOrientation(Qt.Horizontal)

        self.gridLayout_11.addWidget(self._vec_alpha, 3, 2, 1, 1)

        self._vec_arrow_type = QComboBox(self._vec_grp)
        self._vec_arrow_type.addItem("")
        self._vec_arrow_type.addItem("")
        self._vec_arrow_type.addItem("")
        self._vec_arrow_type.addItem("")
        self._vec_arrow_type.addItem("")
        self._vec_arrow_type.addItem("")
        self._vec_arrow_type.addItem("")
        self._vec_arrow_type.addItem("")
        self._vec_arrow_type.addItem("")
        self._vec_arrow_type.setObjectName(u"_vec_arrow_type")

        self.gridLayout_11.addWidget(self._vec_arrow_type, 2, 2, 1, 1)

        self.label_54 = QLabel(self._vec_grp)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font2)

        self.gridLayout_11.addWidget(self.label_54, 2, 0, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_11)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_13)


        self.verticalLayout.addWidget(self._vec_grp)

        self._obj_stack.addWidget(self._vec_page)

        self.verticalLayout_8.addWidget(self._obj_stack)

        self.QuickSettings.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self._cbarWidget = QWidget(self.tab)
        self._cbarWidget.setObjectName(u"_cbarWidget")

        self.verticalLayout_2.addWidget(self._cbarWidget)

        self.UserMsgBox = QWidget(self.tab)
        self.UserMsgBox.setObjectName(u"UserMsgBox")
        self.UserMsgBox.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_52 = QHBoxLayout(self.UserMsgBox)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")

        self.verticalLayout_2.addWidget(self.UserMsgBox)

        self.QuickSettings.addTab(self.tab, "")

        self.verticalLayout_4.addWidget(self.QuickSettings)

        self.userRotationPanel = QFrame(self.q_widget)
        self.userRotationPanel.setObjectName(u"userRotationPanel")
        self.userRotationPanel.setFrameShape(QFrame.StyledPanel)
        self.userRotationPanel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.userRotationPanel)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_21)

        self.userRotation = QLabel(self.userRotationPanel)
        self.userRotation.setObjectName(u"userRotation")

        self.horizontalLayout_10.addWidget(self.userRotation)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_20)


        self.verticalLayout_4.addWidget(self.userRotationPanel)

        self.progressBar = QProgressBar(self.q_widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFocusPolicy(Qt.TabFocus)
        self.progressBar.setValue(0)

        self.verticalLayout_4.addWidget(self.progressBar)

        self.splitter.addWidget(self.q_widget)
        self._objsPage = QStackedWidget(self.splitter)
        self._objsPage.setObjectName(u"_objsPage")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self._objsPage.sizePolicy().hasHeightForWidth())
        self._objsPage.setSizePolicy(sizePolicy3)
        self._objsPage.setFocusPolicy(Qt.StrongFocus)
        self._BrainPage = QWidget()
        self._BrainPage.setObjectName(u"_BrainPage")
        self.horizontalLayout_7 = QHBoxLayout(self._BrainPage)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.cbpanelW = QWidget(self._BrainPage)
        self.cbpanelW.setObjectName(u"cbpanelW")
        self.cbpanelW.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.cbpanelW)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cbpanel = QVBoxLayout()
        self.cbpanel.setSpacing(0)
        self.cbpanel.setObjectName(u"cbpanel")
        self.cbpanel.setContentsMargins(-1, 0, -1, 0)

        self.verticalLayout_10.addLayout(self.cbpanel)


        self.horizontalLayout_11.addWidget(self.cbpanelW)

        self.vBrain = QHBoxLayout()
        self.vBrain.setObjectName(u"vBrain")

        self.horizontalLayout_11.addLayout(self.vBrain)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_11)

        self._objsPage.addWidget(self._BrainPage)
        self._crossecPage = QWidget()
        self._crossecPage.setObjectName(u"_crossecPage")
        self.verticalLayout_26 = QVBoxLayout(self._crossecPage)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self._axialLayout = QHBoxLayout()
        self._axialLayout.setObjectName(u"_axialLayout")

        self.verticalLayout_26.addLayout(self._axialLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self._coronLayout = QHBoxLayout()
        self._coronLayout.setObjectName(u"_coronLayout")

        self.horizontalLayout_9.addLayout(self._coronLayout)

        self._sagitLayout = QHBoxLayout()
        self._sagitLayout.setObjectName(u"_sagitLayout")

        self.horizontalLayout_9.addLayout(self._sagitLayout)


        self.verticalLayout_26.addLayout(self.horizontalLayout_9)

        self._objsPage.addWidget(self._crossecPage)
        self.splitter.addWidget(self._objsPage)

        self.horizontalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1513, 25))
        self.menuFiles = QMenu(self.menubar)
        self.menuFiles.setObjectName(u"menuFiles")
        self.menuSave = QMenu(self.menuFiles)
        self.menuSave.setObjectName(u"menuSave")
        self.menuConfig = QMenu(self.menuSave)
        self.menuConfig.setObjectName(u"menuConfig")
        self.menuLoad = QMenu(self.menuFiles)
        self.menuLoad.setObjectName(u"menuLoad")
        self.menuConfig_2 = QMenu(self.menuLoad)
        self.menuConfig_2.setObjectName(u"menuConfig_2")
        self.menuTransform = QMenu(self.menubar)
        self.menuTransform.setObjectName(u"menuTransform")
        self.menuRun_projection = QMenu(self.menuTransform)
        self.menuRun_projection.setObjectName(u"menuRun_projection")
        self.menuDisplay = QMenu(self.menubar)
        self.menuDisplay.setObjectName(u"menuDisplay")
        self.menuRotate = QMenu(self.menuDisplay)
        self.menuRotate.setObjectName(u"menuRotate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.QuickSettings, self._obj_type_lst)
        QWidget.setTabOrder(self._obj_type_lst, self._source_tab)
        QWidget.setTabOrder(self._source_tab, self.progressBar)

        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menubar.addAction(self.menuTransform.menuAction())
        self.menuFiles.addAction(self.menuSave.menuAction())
        self.menuFiles.addAction(self.menuLoad.menuAction())
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionExit)
        self.menuSave.addAction(self.menuScreenshot)
        self.menuSave.addAction(self.menuConfig.menuAction())
        self.menuConfig.addAction(self.menuSaveGuiConfig)
        self.menuConfig.addAction(self.menuSaveCbarConfig)
        self.menuLoad.addAction(self.menuConfig_2.menuAction())
        self.menuConfig_2.addAction(self.menuLoadGuiConfig)
        self.menuConfig_2.addAction(self.menuLoadCbarConfig)
        self.menuTransform.addAction(self.menuRun_projection.menuAction())
        self.menuTransform.addAction(self.actionClean_projection)
        self.menuRun_projection.addAction(self.menuCortProj)
        self.menuRun_projection.addAction(self.menuCortRep)
        self.menuDisplay.addAction(self.actionObjects)
        self.menuDisplay.addAction(self.menuDispQuickSettings)
        self.menuDisplay.addAction(self.menuDispBrain)
        self.menuDisplay.addAction(self.menuDispCrossec)
        self.menuDisplay.addAction(self.menuDispVol)
        self.menuDisplay.addAction(self.menuDispSources)
        self.menuDisplay.addAction(self.menuDispConnect)
        self.menuDisplay.addAction(self.menuDispROI)
        self.menuDisplay.addAction(self.menuDispCbar)
        self.menuDisplay.addSeparator()
        self.menuDisplay.addAction(self.actionCamera_2)
        self.menuDisplay.addAction(self.menuRotate.menuAction())
        self.menuDisplay.addAction(self.menuCamFly)
        self.menuDisplay.addAction(self.menuResetCam)
        self.menuRotate.addAction(self.menuRotTop)
        self.menuRotate.addAction(self.menuRotBottom)
        self.menuRotate.addAction(self.menuRotLeft)
        self.menuRotate.addAction(self.menuRotRight)
        self.menuRotate.addAction(self.menuRotFront)
        self.menuRotate.addAction(self.menuRotBack)

        self.retranslateUi(MainWindow)

        self.QuickSettings.setCurrentIndex(0)
        self._obj_stack.setCurrentIndex(0)
        self._brain_hemi.setCurrentIndex(0)
        self._source_tab.setCurrentIndex(2)
        self._c_alpha_stack.setCurrentIndex(0)
        self._objsPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Brain", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"QMainWindow { font-size: 10pt; }\n"
"QGroupBox { font-size: 11pt; }\n"
"QLabel { font-size: 10pt; }", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionCortical_repartition.setText(QCoreApplication.translate("MainWindow", u"Cortical repartition", None))
        self.actionCortical.setText(QCoreApplication.translate("MainWindow", u"Cortical", None))
        self.actionSagittal.setText(QCoreApplication.translate("MainWindow", u"Sagittal", None))
        self.actionAxial.setText(QCoreApplication.translate("MainWindow", u"Axial", None))
        self.actionCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.actionLeft.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.actionRight.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.menuDispQuickSettings.setText(QCoreApplication.translate("MainWindow", u"Quick settings", None))
#if QT_CONFIG(shortcut)
        self.menuDispQuickSettings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.menuCortProj.setText(QCoreApplication.translate("MainWindow", u"Cortical projection", None))
#if QT_CONFIG(tooltip)
        self.menuCortProj.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Find all vertices under a distance of t_radius with each source and project s_data to the surface</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.menuCortProj.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.menuCortRep.setText(QCoreApplication.translate("MainWindow", u"Cortical repartition", None))
#if QT_CONFIG(shortcut)
        self.menuCortRep.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionShortcuts.setText(QCoreApplication.translate("MainWindow", u"Shortcuts", None))
#if QT_CONFIG(shortcut)
        self.actionShortcuts.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionUi_settings.setText(QCoreApplication.translate("MainWindow", u"Ui settings", None))
        self.actionMNI.setText(QCoreApplication.translate("MainWindow", u"MNI", None))
        self.actionSources.setText(QCoreApplication.translate("MainWindow", u"Sources", None))
        self.actionConnectivity.setText(QCoreApplication.translate("MainWindow", u"Connectivity", None))
        self.actionColormap.setText(QCoreApplication.translate("MainWindow", u"Colormap", None))
        self.actionShortcut.setText(QCoreApplication.translate("MainWindow", u"Shortcuts", None))
#if QT_CONFIG(shortcut)
        self.actionShortcut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
#if QT_CONFIG(shortcut)
        self.actionDocumentation.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionScreenshot.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispCbar.setText(QCoreApplication.translate("MainWindow", u"Colorbar", None))
#if QT_CONFIG(shortcut)
        self.menuDispCbar.setShortcut(QCoreApplication.translate("MainWindow", u"C", None))
#endif // QT_CONFIG(shortcut)
        self.menuRotTop.setText(QCoreApplication.translate("MainWindow", u"Top", None))
#if QT_CONFIG(shortcut)
        self.menuRotTop.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.menuRotBottom.setText(QCoreApplication.translate("MainWindow", u"Bottom", None))
#if QT_CONFIG(shortcut)
        self.menuRotBottom.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.menuRotLeft.setText(QCoreApplication.translate("MainWindow", u"Left", None))
#if QT_CONFIG(shortcut)
        self.menuRotLeft.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.menuRotRight.setText(QCoreApplication.translate("MainWindow", u"Right", None))
#if QT_CONFIG(shortcut)
        self.menuRotRight.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.menuRotFront.setText(QCoreApplication.translate("MainWindow", u"Front", None))
#if QT_CONFIG(shortcut)
        self.menuRotFront.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.menuRotBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
#if QT_CONFIG(shortcut)
        self.menuRotBack.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.menuCamTurn.setText(QCoreApplication.translate("MainWindow", u"Turntable", None))
        self.menuCamFly.setText(QCoreApplication.translate("MainWindow", u"Fly camera", None))
        self.menuDispBrain.setText(QCoreApplication.translate("MainWindow", u"Brain", None))
#if QT_CONFIG(shortcut)
        self.menuDispBrain.setShortcut(QCoreApplication.translate("MainWindow", u"B", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispSources.setText(QCoreApplication.translate("MainWindow", u"Sources", None))
#if QT_CONFIG(shortcut)
        self.menuDispSources.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispConnect.setText(QCoreApplication.translate("MainWindow", u"Connectivity", None))
#if QT_CONFIG(shortcut)
        self.menuDispConnect.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispROI.setText(QCoreApplication.translate("MainWindow", u"ROI", None))
#if QT_CONFIG(shortcut)
        self.menuDispROI.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.menuSaveScreenCan.setText(QCoreApplication.translate("MainWindow", u"Main canvas", None))
#if QT_CONFIG(shortcut)
        self.menuSaveScreenCan.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.menuSaveScreenWin.setText(QCoreApplication.translate("MainWindow", u"Window", None))
#if QT_CONFIG(shortcut)
        self.menuSaveScreenWin.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionConfig.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.menuSaveGuiConfig.setText(QCoreApplication.translate("MainWindow", u"GUI config", None))
        self.menuSaveCbarConfig.setText(QCoreApplication.translate("MainWindow", u"Cbar config", None))
        self.menuLoadGuiConfig.setText(QCoreApplication.translate("MainWindow", u"GUI config", None))
        self.menuLoadCbarConfig.setText(QCoreApplication.translate("MainWindow", u"Cbar config", None))
        self.actionClean_projection.setText(QCoreApplication.translate("MainWindow", u"Clean projection", None))
        self.menuResetCam.setText(QCoreApplication.translate("MainWindow", u"Reset camera", None))
#if QT_CONFIG(shortcut)
        self.menuResetCam.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.actionObjects.setText(QCoreApplication.translate("MainWindow", u"Objects", None))
        self.actionCamera_2.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.menuDispCrossec.setText(QCoreApplication.translate("MainWindow", u"Cross-sections", None))
#if QT_CONFIG(shortcut)
        self.menuDispCrossec.setShortcut(QCoreApplication.translate("MainWindow", u"X", None))
#endif // QT_CONFIG(shortcut)
        self.menuDispVol.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
#if QT_CONFIG(shortcut)
        self.menuDispVol.setShortcut(QCoreApplication.translate("MainWindow", u"V", None))
#endif // QT_CONFIG(shortcut)
        self.menuScreenshot.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
#if QT_CONFIG(shortcut)
        self.menuScreenshot.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.QuickSettings.setStyleSheet(QCoreApplication.translate("MainWindow", u"QTabWidget::pane { border: 0; }\n"
"QTabBar::tab { padding: 6px 12px; font-size: 10pt; }\n"
"QTabBar::tab:selected { font-weight: 600; }", None))
#if QT_CONFIG(tooltip)
        self.QuickSettings.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Object\n"
"type", None))
        self._obj_type_lst.setItemText(0, QCoreApplication.translate("MainWindow", u"Brain", None))
        self._obj_type_lst.setItemText(1, QCoreApplication.translate("MainWindow", u"Region Of Interest (ROI)", None))
        self._obj_type_lst.setItemText(2, QCoreApplication.translate("MainWindow", u"Volume", None))
        self._obj_type_lst.setItemText(3, QCoreApplication.translate("MainWindow", u"Cross-sections", None))
        self._obj_type_lst.setItemText(4, QCoreApplication.translate("MainWindow", u"Sources", None))
        self._obj_type_lst.setItemText(5, QCoreApplication.translate("MainWindow", u"Connectivity", None))
        self._obj_type_lst.setItemText(6, QCoreApplication.translate("MainWindow", u"Time-series", None))
        self._obj_type_lst.setItemText(7, QCoreApplication.translate("MainWindow", u"Pictures", None))
        self._obj_type_lst.setItemText(8, QCoreApplication.translate("MainWindow", u"Vectors", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Object\n"
"name", None))
#if QT_CONFIG(tooltip)
        self._obj_name_lst.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Color connectivity line according to :</p><p>- Their connectivity strength</p><p>- The number of connections per node</p><p>- The line density (use the radius to control the density)</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">c_colorby</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._brain_grp.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"z-max", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"y-min", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"x-max", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"z-min", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"x-min", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"y-max", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Hemisphere", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Template", None))
#if QT_CONFIG(tooltip)
        self._brain_template.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Switch brain template.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">a_template</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._brain_hemi.setItemText(0, QCoreApplication.translate("MainWindow", u"both", None))
        self._brain_hemi.setItemText(1, QCoreApplication.translate("MainWindow", u"left", None))
        self._brain_hemi.setItemText(2, QCoreApplication.translate("MainWindow", u"right", None))

#if QT_CONFIG(tooltip)
        self._brain_translucent.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Use transparent or opaque brain.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">a_proj</span> and <span style=\" font-style:italic;\">a_opacity</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._brain_translucent.setText(QCoreApplication.translate("MainWindow", u"Translucent", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Slice", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self._brain_inlight.setText(QCoreApplication.translate("MainWindow", u"Inside", None))
        self._roi_grp.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"ROI", None))
        self._roiTransp.setText(QCoreApplication.translate("MainWindow", u"Translucent", None))
        self._roiLevel.setItemText(0, QCoreApplication.translate("MainWindow", u"7", None))
        self._roiLevel.setItemText(1, QCoreApplication.translate("MainWindow", u"12", None))
        self._roiLevel.setItemText(2, QCoreApplication.translate("MainWindow", u"20", None))
        self._roiLevel.setItemText(3, QCoreApplication.translate("MainWindow", u"36", None))
        self._roiLevel.setItemText(4, QCoreApplication.translate("MainWindow", u"64", None))
        self._roiLevel.setItemText(5, QCoreApplication.translate("MainWindow", u"122", None))
        self._roiLevel.setItemText(6, QCoreApplication.translate("MainWindow", u"ROI", None))

        self._roiIsSmooth.setText(QCoreApplication.translate("MainWindow", u"Smooth", None))
        self._roiUniColor.setText(QCoreApplication.translate("MainWindow", u"Unique color", None))
        self._roiButApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self._roiButRst.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self._roiFilter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter (regular expression)", None))
        self._vol_grp.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self._volRendering.setItemText(0, QCoreApplication.translate("MainWindow", u"mip", None))
        self._volRendering.setItemText(1, QCoreApplication.translate("MainWindow", u"translucent", None))
        self._volRendering.setItemText(2, QCoreApplication.translate("MainWindow", u"additive", None))
        self._volRendering.setItemText(3, QCoreApplication.translate("MainWindow", u"iso", None))

        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Cmap", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Rendering", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self._sec_grp.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Coronal", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Axial", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Sagittal", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Interpolation", None))
        self._csLevel.setItemText(0, QCoreApplication.translate("MainWindow", u"7", None))
        self._csLevel.setItemText(1, QCoreApplication.translate("MainWindow", u"12", None))
        self._csLevel.setItemText(2, QCoreApplication.translate("MainWindow", u"20", None))
        self._csLevel.setItemText(3, QCoreApplication.translate("MainWindow", u"36", None))
        self._csLevel.setItemText(4, QCoreApplication.translate("MainWindow", u"64", None))
        self._csLevel.setItemText(5, QCoreApplication.translate("MainWindow", u"122", None))
        self._csLevel.setItemText(6, QCoreApplication.translate("MainWindow", u"ROI", None))

        self._csInterp.setItemText(0, QCoreApplication.translate("MainWindow", u"nearest", None))
        self._csInterp.setItemText(1, QCoreApplication.translate("MainWindow", u"bilinear", None))
        self._csInterp.setItemText(2, QCoreApplication.translate("MainWindow", u"hanning", None))
        self._csInterp.setItemText(3, QCoreApplication.translate("MainWindow", u"hamming", None))
        self._csInterp.setItemText(4, QCoreApplication.translate("MainWindow", u"hermite", None))
        self._csInterp.setItemText(5, QCoreApplication.translate("MainWindow", u"kaiser", None))
        self._csInterp.setItemText(6, QCoreApplication.translate("MainWindow", u"quadric", None))
        self._csInterp.setItemText(7, QCoreApplication.translate("MainWindow", u"bicubic", None))

        self._s_grp.setTitle(QCoreApplication.translate("MainWindow", u"Display sources", None))
        self._s_select.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self._s_select.setItemText(1, QCoreApplication.translate("MainWindow", u"None", None))
        self._s_select.setItemText(2, QCoreApplication.translate("MainWindow", u"Left hemisphere", None))
        self._s_select.setItemText(3, QCoreApplication.translate("MainWindow", u"Right hemisphere", None))
        self._s_select.setItemText(4, QCoreApplication.translate("MainWindow", u"Inside the brain", None))
        self._s_select.setItemText(5, QCoreApplication.translate("MainWindow", u"Outside the brain", None))

#if QT_CONFIG(tooltip)
        self._s_select.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Hide or display sources. Specify if you want to keep only sources in the left or right hemisphere or sources that are either inside or outside the brain volume.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._s_symbol.setItemText(0, QCoreApplication.translate("MainWindow", u"disc", None))
        self._s_symbol.setItemText(1, QCoreApplication.translate("MainWindow", u"arrow", None))
        self._s_symbol.setItemText(2, QCoreApplication.translate("MainWindow", u"ring", None))
        self._s_symbol.setItemText(3, QCoreApplication.translate("MainWindow", u"clobber", None))
        self._s_symbol.setItemText(4, QCoreApplication.translate("MainWindow", u"square", None))
        self._s_symbol.setItemText(5, QCoreApplication.translate("MainWindow", u"diamond", None))
        self._s_symbol.setItemText(6, QCoreApplication.translate("MainWindow", u"vbar", None))
        self._s_symbol.setItemText(7, QCoreApplication.translate("MainWindow", u"hbar", None))
        self._s_symbol.setItemText(8, QCoreApplication.translate("MainWindow", u"cross", None))
        self._s_symbol.setItemText(9, QCoreApplication.translate("MainWindow", u"tailed_arrow", None))
        self._s_symbol.setItemText(10, QCoreApplication.translate("MainWindow", u"x", None))
        self._s_symbol.setItemText(11, QCoreApplication.translate("MainWindow", u"triangle_up", None))
        self._s_symbol.setItemText(12, QCoreApplication.translate("MainWindow", u"triangle_down", None))

#if QT_CONFIG(tooltip)
        self._s_symbol.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Change sources symbol</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">s_symbol</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._s_radiusmin.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximum radius for the sources.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">s_radiusmax</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._s_radiusmax.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimum radius for the sources.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">s_radiusmin</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Width", None))
#if QT_CONFIG(tooltip)
        self._s_edge_width.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Edge width.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">s_edgewidth</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._s_edge_color.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Edge color (<span style=\" font-style:italic;\">if edge width is not 0.</span>)</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">s_edgecolor</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._s_edge_color_p.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Symbol", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Radius", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Edge", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self._st_grp.setTitle(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Translate\n"
"(x, y, z)", None))
#if QT_CONFIG(tooltip)
        self._st_color.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Edge color (<span style=\" font-style:italic;\">if edge width is not 0.</span>)</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">s_edgecolor</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._st_color_p.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Fontsize", None))
#if QT_CONFIG(tooltip)
        self._st_font_size.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Font size of source's text.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">s_textsize</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Offset along the x-axis (dx), y-axis (dy) and z-axis (dz)</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">s_textshift</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._source_tab.setTabText(self._source_tab.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Properties", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Projection", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Radius", None))
#if QT_CONFIG(tooltip)
        self._s_proj_radius.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Radius for the cortical projection / repartition. Every vertices arround each sources comprised in a sphere of radius &quot;Radius&quot; will be considered in the projection. </p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">t_radius</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Projection\n"
"type", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Project on", None))
        self._s_proj_on.setItemText(0, QCoreApplication.translate("MainWindow", u"brain", None))
        self._s_proj_on.setItemText(1, QCoreApplication.translate("MainWindow", u"roi", None))

#if QT_CONFIG(tooltip)
        self._s_proj_on.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Project source's activity / repartition either on the surface of :</p><p>- The brain</p><p>- ROI (if a ROI is displayed)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._s_proj_contribute.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>If contribute is checked, the projection of a source can contribute to both hemisphere. If it's not checked, the projection is only performed on the hemisphere it belong to. If the source is perfectly centered (like Cz), the projection is forced to be on both hemisphere.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">t_contribute</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._s_proj_contribute.setText(QCoreApplication.translate("MainWindow", u"Contribute", None))
        self._s_proj_type.setItemText(0, QCoreApplication.translate("MainWindow", u"modulation", None))
        self._s_proj_type.setItemText(1, QCoreApplication.translate("MainWindow", u"repartition", None))

#if QT_CONFIG(tooltip)
        self._s_proj_type.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Choose the projection type :</p><p>- <span style=\" font-weight:600;\">Source's activity :</span> project the s_data input parameter on the surface.</p><p>- <span style=\" font-weight:600;\">Source's repartition :</span> project the number of contributing sources per vertex.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self._s_proj_type.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Choose the projection type :</p><p>- <span style=\" font-weight:600;\">Source's activity :</span> project the s_data input parameter on the surface.</p><p>- <span style=\" font-weight:600;\">Source's repartition :</span> project the number of contributing sources per vertex.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Mask\n"
"color", None))
        self._s_proj_mask_color.setText(QCoreApplication.translate("MainWindow", u"gray", None))
        self._s_proj_mask_color_p.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self._s_proj_apply.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Run the source's projection using above parameters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._s_proj_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self._source_tab.setTabText(self._source_tab.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Projection", None))
        self._s_analyse_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Analyse using\n"
"ROI", None))
        self._s_analyse_roi.setItemText(0, QCoreApplication.translate("MainWindow", u"Brodmann", None))
        self._s_analyse_roi.setItemText(1, QCoreApplication.translate("MainWindow", u"AAL", None))
        self._s_analyse_roi.setItemText(2, QCoreApplication.translate("MainWindow", u"Talairach", None))

        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Cross-section", None))
        self._s_show_cs.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self._source_tab.setTabText(self._source_tab.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Analyse", None))
        self._c_grp.setTitle(QCoreApplication.translate("MainWindow", u"Display connectivity", None))
        self._c_dyn_meth.setItemText(0, QCoreApplication.translate("MainWindow", u"Static", None))
        self._c_dyn_meth.setItemText(1, QCoreApplication.translate("MainWindow", u"Dynamic", None))

#if QT_CONFIG(tooltip)
        self._c_dyn_meth.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Control the dynamic opacity so that stronger connections are more opaque to weaker connections.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">c_dynamic</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"(Min, Max)", None))
#if QT_CONFIG(tooltip)
        self._c_dyn_min.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimum opacity for the weaker connexions.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">c_dynamic</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._c_dyn_max.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximum opacity for the stronger connexions.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">c_dynamic</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._c_colorby.setItemText(0, QCoreApplication.translate("MainWindow", u"strength", None))
        self._c_colorby.setItemText(1, QCoreApplication.translate("MainWindow", u"count", None))
        self._c_colorby.setItemText(2, QCoreApplication.translate("MainWindow", u"causal", None))

#if QT_CONFIG(tooltip)
        self._c_colorby.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Color connectivity line according to :</p><p>- Their connectivity strength</p><p>- The number of connections per node</p><p>- The line density (use the radius to control the density)</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">c_colorby</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Transparency", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Line\n"
"width", None))
#if QT_CONFIG(tooltip)
        self._c_line_width.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Connectivity line width.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">c_linewidth</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ts_grp.setTitle(QCoreApplication.translate("MainWindow", u"Display time-series", None))
#if QT_CONFIG(tooltip)
        self._ts_color.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Time-serie's color.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">ts_color</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ts_color_p.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self._ts_width.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Width of the time-series</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">ts_width</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Translate\n"
"(x, y, z)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
#if QT_CONFIG(tooltip)
        self._ts_amp.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Amplitude of the time-series.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">ts_amp</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Line width", None))
#if QT_CONFIG(tooltip)
        self._ts_line_width.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Line-width of each time-series.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">ts_lw</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Offset along the x-axis (dx), y-axis (dy) and z-axis (dz)</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">ts_dxyz</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self._pic_grp.setTitle(QCoreApplication.translate("MainWindow", u"Display pictures", None))
#if QT_CONFIG(tooltip)
        self._pic_width.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Width of the pictures</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">pic_width</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Translate\n"
"(x, y, z)", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Height", None))
#if QT_CONFIG(tooltip)
        self._pic_height.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Height of the pictures.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">pic_height</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Offset along the x-axis (dx), y-axis (dy) and z-axis (dz)</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">pic_dxyz</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self._vec_grp.setTitle(QCoreApplication.translate("MainWindow", u"Display vectors", None))
#if QT_CONFIG(tooltip)
        self._vec_line_width.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Width of the pictures</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">pic_width</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Line\n"
"width", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Arrow\n"
"size", None))
#if QT_CONFIG(tooltip)
        self._vec_arrow_size.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Height of the pictures.</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">pic_height</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self._vec_arrow_type.setItemText(0, QCoreApplication.translate("MainWindow", u"stealth", None))
        self._vec_arrow_type.setItemText(1, QCoreApplication.translate("MainWindow", u"curved", None))
        self._vec_arrow_type.setItemText(2, QCoreApplication.translate("MainWindow", u"angle_30", None))
        self._vec_arrow_type.setItemText(3, QCoreApplication.translate("MainWindow", u"angle_60", None))
        self._vec_arrow_type.setItemText(4, QCoreApplication.translate("MainWindow", u"angle_90", None))
        self._vec_arrow_type.setItemText(5, QCoreApplication.translate("MainWindow", u"triangle_30", None))
        self._vec_arrow_type.setItemText(6, QCoreApplication.translate("MainWindow", u"triangle_60", None))
        self._vec_arrow_type.setItemText(7, QCoreApplication.translate("MainWindow", u"triangle_90", None))
        self._vec_arrow_type.setItemText(8, QCoreApplication.translate("MainWindow", u"inhibitor_round", None))

#if QT_CONFIG(tooltip)
        self._vec_arrow_type.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Color connectivity line according to :</p><p>- Their connectivity strength</p><p>- The number of connections per node</p><p>- The line density (use the radius to control the density)</p><p><span style=\" font-weight:600;\">Input parameter : </span><span style=\" font-style:italic;\">c_colorby</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Arrow\n"
"type", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Objects", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cbar", None))
        self.userRotation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuFiles.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuConfig.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.menuLoad.setTitle(QCoreApplication.translate("MainWindow", u"Load", None))
        self.menuConfig_2.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.menuTransform.setTitle(QCoreApplication.translate("MainWindow", u"Project", None))
        self.menuRun_projection.setTitle(QCoreApplication.translate("MainWindow", u"Run projection", None))
        self.menuDisplay.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.menuRotate.setTitle(QCoreApplication.translate("MainWindow", u"Rotate", None))
    # retranslateUi

