# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signal_gui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QStackedWidget, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1197, 941)
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
        self.menuScreenshot = QAction(MainWindow)
        self.menuScreenshot.setObjectName(u"menuScreenshot")
        self.actionGrid = QAction(MainWindow)
        self.actionGrid.setObjectName(u"actionGrid")
        self.actionGrid.setCheckable(True)
        self.actionGrid.setChecked(True)
        self.actionSignal = QAction(MainWindow)
        self.actionSignal.setObjectName(u"actionSignal")
        self.actionSignal.setCheckable(True)
        self.actionSignal.setChecked(True)
        self.actionQSP = QAction(MainWindow)
        self.actionQSP.setObjectName(u"actionQSP")
        self.actionQSP.setCheckable(True)
        self.actionQSP.setChecked(True)
        self.saveAnnotations = QAction(MainWindow)
        self.saveAnnotations.setObjectName(u"saveAnnotations")
        self.loadAnnotations = QAction(MainWindow)
        self.loadAnnotations.setObjectName(u"loadAnnotations")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setLineWidth(1)
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
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 414, 935))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setItalic(True)
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.line_10 = QFrame(self.groupBox_3)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_10, 3, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_29 = QLabel(self.groupBox_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.gridLayout.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self._axis_color = QLineEdit(self.groupBox_3)
        self._axis_color.setObjectName(u"_axis_color")

        self.gridLayout.addWidget(self._axis_color, 3, 2, 1, 1)

        self.line_4 = QFrame(self.groupBox_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 0, 1, 1, 1)

        self.line_21 = QFrame(self.groupBox_3)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.VLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_21, 2, 1, 1, 1)

        self.line_3 = QFrame(self.groupBox_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.line_9 = QFrame(self.groupBox_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 4, 1, 1, 1)

        self._sig_color = QLineEdit(self.groupBox_3)
        self._sig_color.setObjectName(u"_sig_color")

        self.gridLayout.addWidget(self._sig_color, 4, 2, 1, 1)

        self._sig_ax_picker = QToolButton(self.groupBox_3)
        self._sig_ax_picker.setObjectName(u"_sig_ax_picker")

        self.gridLayout.addWidget(self._sig_ax_picker, 3, 3, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.gridLayout_2.addWidget(self.label_22, 1, 0, 1, 1)

        self._sig_title = QLineEdit(self.groupBox_3)
        self._sig_title.setObjectName(u"_sig_title")

        self.gridLayout_2.addWidget(self._sig_title, 0, 1, 1, 1)

        self._sig_title_fz = QDoubleSpinBox(self.groupBox_3)
        self._sig_title_fz.setObjectName(u"_sig_title_fz")
        self._sig_title_fz.setDecimals(1)
        self._sig_title_fz.setMinimum(0.100000000000000)

        self.gridLayout_2.addWidget(self._sig_title_fz, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 2)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.gridLayout_15.addWidget(self.label_23, 0, 0, 1, 1)

        self._sig_lab_fz = QDoubleSpinBox(self.groupBox_3)
        self._sig_lab_fz.setObjectName(u"_sig_lab_fz")
        self._sig_lab_fz.setDecimals(1)
        self._sig_lab_fz.setMinimum(0.100000000000000)

        self.gridLayout_15.addWidget(self._sig_lab_fz, 2, 1, 1, 1)

        self._sig_xlab = QLineEdit(self.groupBox_3)
        self._sig_xlab.setObjectName(u"_sig_xlab")

        self.gridLayout_15.addWidget(self._sig_xlab, 0, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.gridLayout_15.addWidget(self.label_24, 2, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.gridLayout_15.addWidget(self.label_25, 1, 0, 1, 1)

        self._sig_ylab = QLineEdit(self.groupBox_3)
        self._sig_ylab.setObjectName(u"_sig_ylab")

        self.gridLayout_15.addWidget(self._sig_ylab, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_15, 1, 2, 1, 2)

        self._sig_ticks_fz = QDoubleSpinBox(self.groupBox_3)
        self._sig_ticks_fz.setObjectName(u"_sig_ticks_fz")
        self._sig_ticks_fz.setDecimals(1)
        self._sig_ticks_fz.setMinimum(0.100000000000000)

        self.gridLayout.addWidget(self._sig_ticks_fz, 2, 2, 1, 2)

        self._sig_sig_picker = QToolButton(self.groupBox_3)
        self._sig_sig_picker.setObjectName(u"_sig_sig_picker")

        self.gridLayout.addWidget(self._sig_sig_picker, 4, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_12.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, -1, 0, -1)
        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 1)

        self._sig_form = QComboBox(self.groupBox_5)
        self._sig_form.addItem("")
        self._sig_form.addItem("")
        self._sig_form.addItem("")
        self._sig_form.addItem("")
        self._sig_form.addItem("")
        self._sig_form.addItem("")
        self._sig_form.setObjectName(u"_sig_form")

        self.gridLayout_6.addWidget(self._sig_form, 0, 2, 1, 1)

        self.line_12 = QFrame(self.groupBox_5)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_12, 0, 1, 1, 1)

        self._sig_amp = QGroupBox(self.groupBox_5)
        self._sig_amp.setObjectName(u"_sig_amp")
        font2 = QFont()
        font2.setItalic(False)
        font2.setKerning(True)
        self._sig_amp.setFont(font2)
        self._sig_amp.setCheckable(True)
        self._sig_amp.setChecked(False)
        self.horizontalLayout_3 = QHBoxLayout(self._sig_amp)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.line_6 = QFrame(self._sig_amp)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_6, 0, 1, 1, 1)

        self.label_2 = QLabel(self._sig_amp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_15, 3, 2, 1, 1)

        self._sig_amp_min = QDoubleSpinBox(self._sig_amp)
        self._sig_amp_min.setObjectName(u"_sig_amp_min")

        self.gridLayout_5.addWidget(self._sig_amp_min, 1, 2, 1, 1)

        self.label = QLabel(self._sig_amp)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.line_2 = QFrame(self._sig_amp)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 1, 1, 1, 1)

        self._sig_amp_max = QDoubleSpinBox(self._sig_amp)
        self._sig_amp_max.setObjectName(u"_sig_amp_max")

        self.gridLayout_5.addWidget(self._sig_amp_max, 0, 2, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_5)


        self.gridLayout_6.addWidget(self._sig_amp, 3, 0, 1, 3)

        self.horizontalSpacer_5 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self._PlottingForm = QStackedWidget(self.groupBox_5)
        self._PlottingForm.setObjectName(u"_PlottingForm")
        self._PlottingForm.setFrameShape(QFrame.NoFrame)
        self.line = QWidget()
        self.line.setObjectName(u"line")
        self.gridLayout_9 = QGridLayout(self.line)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self._sig_th = QGroupBox(self.line)
        self._sig_th.setObjectName(u"_sig_th")
        self._sig_th.setCheckable(True)
        self._sig_th.setChecked(False)
        self.verticalLayout_10 = QVBoxLayout(self._sig_th)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_30 = QLabel(self._sig_th)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.gridLayout_7.addWidget(self.label_30, 1, 0, 1, 1)

        self.line_22 = QFrame(self._sig_th)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_22, 1, 1, 1, 1)

        self._sig_th_min = QDoubleSpinBox(self._sig_th)
        self._sig_th_min.setObjectName(u"_sig_th_min")
        self._sig_th_min.setDecimals(1)
        self._sig_th_min.setMinimum(1.000000000000000)
        self._sig_th_min.setSingleStep(0.100000000000000)

        self.gridLayout_7.addWidget(self._sig_th_min, 1, 2, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_16, 3, 2, 1, 1)

        self.label_31 = QLabel(self._sig_th)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.gridLayout_7.addWidget(self.label_31, 0, 0, 1, 1)

        self.line_23 = QFrame(self._sig_th)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.Shape.VLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_23, 0, 1, 1, 1)

        self._sig_th_max = QDoubleSpinBox(self._sig_th)
        self._sig_th_max.setObjectName(u"_sig_th_max")
        self._sig_th_max.setDecimals(1)
        self._sig_th_max.setMinimum(1.000000000000000)
        self._sig_th_max.setSingleStep(0.100000000000000)

        self.gridLayout_7.addWidget(self._sig_th_max, 0, 2, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_7)


        self.gridLayout_9.addWidget(self._sig_th, 2, 0, 1, 3)

        self.label_15 = QLabel(self.line)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout_9.addWidget(self.label_15, 1, 0, 1, 1)

        self.line_15 = QFrame(self.line)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_15, 1, 1, 1, 1)

        self._sig_lw = QDoubleSpinBox(self.line)
        self._sig_lw.setObjectName(u"_sig_lw")
        self._sig_lw.setDecimals(1)
        self._sig_lw.setMinimum(1.000000000000000)
        self._sig_lw.setSingleStep(0.100000000000000)

        self.gridLayout_9.addWidget(self._sig_lw, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_7, 4, 2, 1, 1)

        self._PlottingForm.addWidget(self.line)
        self.markers = QWidget()
        self.markers.setObjectName(u"markers")
        self.gridLayout_13 = QGridLayout(self.markers)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_9, 2, 2, 1, 1)

        self.line_17 = QFrame(self.markers)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_13.addWidget(self.line_17, 0, 1, 1, 1)

        self.label_19 = QLabel(self.markers)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_13.addWidget(self.label_19, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self._sig_size = QDoubleSpinBox(self.markers)
        self._sig_size.setObjectName(u"_sig_size")

        self.gridLayout_13.addWidget(self._sig_size, 0, 2, 1, 1)

        self.label_27 = QLabel(self.markers)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.gridLayout_13.addWidget(self.label_27, 1, 0, 1, 1)

        self.line_19 = QFrame(self.markers)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_13.addWidget(self.line_19, 1, 1, 1, 1)

        self._sig_symbol = QComboBox(self.markers)
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.addItem("")
        self._sig_symbol.setObjectName(u"_sig_symbol")

        self.gridLayout_13.addWidget(self._sig_symbol, 1, 2, 1, 1)

        self._PlottingForm.addWidget(self.markers)
        self.histogram = QWidget()
        self.histogram.setObjectName(u"histogram")
        self.gridLayout_12 = QGridLayout(self.histogram)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_18 = QLabel(self.histogram)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.gridLayout_12.addWidget(self.label_18, 0, 0, 1, 1)

        self._sig_nbins = QSpinBox(self.histogram)
        self._sig_nbins.setObjectName(u"_sig_nbins")
        self._sig_nbins.setMinimum(1)
        self._sig_nbins.setMaximum(10000)

        self.gridLayout_12.addWidget(self._sig_nbins, 0, 2, 1, 1)

        self.line_16 = QFrame(self.histogram)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_12.addWidget(self.line_16, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self._PlottingForm.addWidget(self.histogram)
        self.TF = QWidget()
        self.TF.setObjectName(u"TF")
        self.gridLayout_3 = QGridLayout(self.TF)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_20)

        self._sig_tf_apply = QPushButton(self.TF)
        self._sig_tf_apply.setObjectName(u"_sig_tf_apply")

        self.horizontalLayout_6.addWidget(self._sig_tf_apply)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_21)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 8, 0, 1, 3)

        self.line_14 = QFrame(self.TF)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_14, 0, 1, 1, 1)

        self._sig_tf_interp = QComboBox(self.TF)
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.addItem("")
        self._sig_tf_interp.setObjectName(u"_sig_tf_interp")

        self.gridLayout_3.addWidget(self._sig_tf_interp, 1, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 4, 2, 1, 1)

        self.label_26 = QLabel(self.TF)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.gridLayout_3.addWidget(self.label_26, 1, 0, 1, 1)

        self.label_6 = QLabel(self.TF)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self._sig_baseline = QGroupBox(self.TF)
        self._sig_baseline.setObjectName(u"_sig_baseline")
        self._sig_baseline.setCheckable(True)
        self._sig_baseline.setChecked(False)
        self.horizontalLayout_5 = QHBoxLayout(self._sig_baseline)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.label_13 = QLabel(self._sig_baseline)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.line_8 = QFrame(self._sig_baseline)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_8)

        self._sig_base_start = QSpinBox(self._sig_baseline)
        self._sig_base_start.setObjectName(u"_sig_base_start")

        self.horizontalLayout_5.addWidget(self._sig_base_start)

        self.horizontalSpacer_17 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_17)

        self.label_14 = QLabel(self._sig_baseline)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_14)

        self.line_18 = QFrame(self._sig_baseline)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_18)

        self._sig_base_end = QSpinBox(self._sig_baseline)
        self._sig_base_end.setObjectName(u"_sig_base_end")

        self.horizontalLayout_5.addWidget(self._sig_base_end)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_18)


        self.gridLayout_3.addWidget(self._sig_baseline, 5, 0, 1, 3)

        self._sig_averaging = QGroupBox(self.TF)
        self._sig_averaging.setObjectName(u"_sig_averaging")
        self._sig_averaging.setCheckable(True)
        self._sig_averaging.setChecked(False)
        self.gridLayout_11 = QGridLayout(self._sig_averaging)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, -1, 0, -1)
        self._sig_av_overlap = QDoubleSpinBox(self._sig_averaging)
        self._sig_av_overlap.setObjectName(u"_sig_av_overlap")
        self._sig_av_overlap.setMaximum(0.800000000000000)
        self._sig_av_overlap.setSingleStep(0.100000000000000)

        self.gridLayout_11.addWidget(self._sig_av_overlap, 1, 2, 1, 2)

        self.label_17 = QLabel(self._sig_averaging)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.gridLayout_11.addWidget(self.label_17, 1, 0, 1, 1)

        self._sig_av_win = QSpinBox(self._sig_averaging)
        self._sig_av_win.setObjectName(u"_sig_av_win")

        self.gridLayout_11.addWidget(self._sig_av_win, 0, 2, 1, 2)

        self.label_16 = QLabel(self._sig_averaging)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.gridLayout_11.addWidget(self.label_16, 0, 0, 1, 1)

        self.line_25 = QFrame(self._sig_averaging)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line_25, 1, 1, 1, 1)

        self.line_24 = QFrame(self._sig_averaging)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.VLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line_24, 0, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_19, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self._sig_averaging, 6, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 9, 0, 1, 1)

        self._sig_norm = QComboBox(self.TF)
        self._sig_norm.addItem("")
        self._sig_norm.addItem("")
        self._sig_norm.addItem("")
        self._sig_norm.addItem("")
        self._sig_norm.addItem("")
        self._sig_norm.setObjectName(u"_sig_norm")

        self.gridLayout_3.addWidget(self._sig_norm, 0, 2, 1, 1)

        self.line_26 = QFrame(self.TF)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.Shape.VLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_26, 1, 1, 1, 1)

        self._sig_tf_clim = QGroupBox(self.TF)
        self._sig_tf_clim.setObjectName(u"_sig_tf_clim")
        self._sig_tf_clim.setCheckable(True)
        self._sig_tf_clim.setChecked(False)
        self.horizontalLayout_8 = QHBoxLayout(self._sig_tf_clim)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.label_32 = QLabel(self._sig_tf_clim)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_32)

        self.line_27 = QFrame(self._sig_tf_clim)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.Shape.VLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_27)

        self._sig_climin = QDoubleSpinBox(self._sig_tf_clim)
        self._sig_climin.setObjectName(u"_sig_climin")
        self._sig_climin.setMinimum(-1000000000.000000000000000)
        self._sig_climin.setMaximum(1000000000.000000000000000)

        self.horizontalLayout_8.addWidget(self._sig_climin)

        self.horizontalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_23)

        self.label_33 = QLabel(self._sig_tf_clim)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_33)

        self.line_28 = QFrame(self._sig_tf_clim)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.Shape.VLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_28)

        self._sig_climax = QDoubleSpinBox(self._sig_tf_clim)
        self._sig_climax.setObjectName(u"_sig_climax")
        self._sig_climax.setMinimum(-1000000000.000000000000000)
        self._sig_climax.setMaximum(1000000000.000000000000000)

        self.horizontalLayout_8.addWidget(self._sig_climax)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_24)


        self.gridLayout_3.addWidget(self._sig_tf_clim, 7, 0, 1, 3)

        self.label_34 = QLabel(self.TF)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)

        self.gridLayout_3.addWidget(self.label_34, 2, 0, 1, 1)

        self.line_29 = QFrame(self.TF)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.Shape.VLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_29, 2, 1, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self._sig_tf_rev = QCheckBox(self.TF)
        self._sig_tf_rev.setObjectName(u"_sig_tf_rev")

        self.gridLayout_14.addWidget(self._sig_tf_rev, 0, 1, 1, 1)

        self._sig_tf_cmap = QComboBox(self.TF)
        self._sig_tf_cmap.setObjectName(u"_sig_tf_cmap")

        self.gridLayout_14.addWidget(self._sig_tf_cmap, 0, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_25, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_14, 2, 2, 1, 1)

        self._PlottingForm.addWidget(self.TF)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_16 = QGridLayout(self.page)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.line_31 = QFrame(self.page)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.Shape.VLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_16.addWidget(self.line_31, 1, 1, 1, 1)

        self._sig_noverlap = QSpinBox(self.page)
        self._sig_noverlap.setObjectName(u"_sig_noverlap")
        self._sig_noverlap.setMaximum(10000000)
        self._sig_noverlap.setValue(128)

        self.gridLayout_16.addWidget(self._sig_noverlap, 1, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_7, 3, 0, 1, 1)

        self._sig_nperseg = QSpinBox(self.page)
        self._sig_nperseg.setObjectName(u"_sig_nperseg")
        self._sig_nperseg.setMaximum(100000)
        self._sig_nperseg.setValue(256)

        self.gridLayout_16.addWidget(self._sig_nperseg, 0, 2, 1, 1)

        self.label_36 = QLabel(self.page)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)

        self.gridLayout_16.addWidget(self.label_36, 0, 0, 1, 1)

        self.label_37 = QLabel(self.page)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)

        self.gridLayout_16.addWidget(self.label_37, 1, 0, 1, 1)

        self.line_30 = QFrame(self.page)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.Shape.VLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_16.addWidget(self.line_30, 0, 1, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_26, 2, 2, 1, 1)

        self._PlottingForm.addWidget(self.page)

        self.gridLayout_6.addWidget(self._PlottingForm, 4, 0, 1, 3)

        self._sig_smooth = QCheckBox(self.groupBox_5)
        self._sig_smooth.setObjectName(u"_sig_smooth")

        self.gridLayout_6.addWidget(self._sig_smooth, 1, 0, 1, 3)


        self.verticalLayout_12.addWidget(self.groupBox_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.QuickSettings.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_4 = QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_21 = QGridLayout(self.groupBox_4)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self._grid_lw = QDoubleSpinBox(self.groupBox_4)
        self._grid_lw.setObjectName(u"_grid_lw")
        self._grid_lw.setDecimals(1)
        self._grid_lw.setMinimum(1.000000000000000)

        self.gridLayout_21.addWidget(self._grid_lw, 0, 2, 1, 1)

        self.label_45 = QLabel(self.groupBox_4)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_21.addWidget(self.label_45, 0, 0, 1, 1)

        self._grid_smooth = QCheckBox(self.groupBox_4)
        self._grid_smooth.setObjectName(u"_grid_smooth")

        self.gridLayout_21.addWidget(self._grid_smooth, 2, 0, 1, 3)

        self.line_40 = QFrame(self.groupBox_4)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.Shape.VLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_21.addWidget(self.line_40, 0, 1, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_31, 1, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_20 = QGridLayout(self.groupBox)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_43 = QLabel(self.groupBox)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font1)

        self.gridLayout_20.addWidget(self.label_43, 0, 0, 1, 1)

        self._grid_ncols = QSpinBox(self.groupBox)
        self._grid_ncols.setObjectName(u"_grid_ncols")
        self._grid_ncols.setMinimum(1)

        self.gridLayout_20.addWidget(self._grid_ncols, 1, 2, 1, 1)

        self.label_44 = QLabel(self.groupBox)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font1)

        self.gridLayout_20.addWidget(self.label_44, 1, 0, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_28, 3, 2, 1, 1)

        self._grid_nrows = QSpinBox(self.groupBox)
        self._grid_nrows.setObjectName(u"_grid_nrows")
        self._grid_nrows.setMinimum(1)

        self.gridLayout_20.addWidget(self._grid_nrows, 0, 2, 1, 1)

        self.line_38 = QFrame(self.groupBox)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.Shape.VLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_20.addWidget(self.line_38, 0, 1, 1, 1)

        self.line_39 = QFrame(self.groupBox)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.Shape.VLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_20.addWidget(self.line_39, 1, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_29)

        self._grid_reorg_apply = QPushButton(self.groupBox)
        self._grid_reorg_apply.setObjectName(u"_grid_reorg_apply")
        self._grid_reorg_apply.setEnabled(False)

        self.horizontalLayout_11.addWidget(self._grid_reorg_apply)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_30)


        self.gridLayout_20.addLayout(self.horizontalLayout_11, 2, 0, 1, 3)


        self.verticalLayout_5.addWidget(self.groupBox)

        self._grid_titles = QGroupBox(self.tab_4)
        self._grid_titles.setObjectName(u"_grid_titles")
        self._grid_titles.setCheckable(True)
        self.gridLayout_19 = QGridLayout(self._grid_titles)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.line_34 = QFrame(self._grid_titles)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.Shape.VLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_19.addWidget(self.line_34, 0, 1, 1, 1)

        self.label_39 = QLabel(self._grid_titles)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.gridLayout_19.addWidget(self.label_39, 0, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_8, 2, 0, 1, 1)

        self.label_41 = QLabel(self._grid_titles)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font1)

        self.gridLayout_19.addWidget(self.label_41, 1, 0, 1, 1)

        self.line_36 = QFrame(self._grid_titles)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.Shape.VLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_19.addWidget(self.line_36, 1, 1, 1, 1)

        self._grid_titles_color = QLineEdit(self._grid_titles)
        self._grid_titles_color.setObjectName(u"_grid_titles_color")

        self.gridLayout_19.addWidget(self._grid_titles_color, 1, 2, 1, 1)

        self._grid_color_picker = QToolButton(self._grid_titles)
        self._grid_color_picker.setObjectName(u"_grid_color_picker")

        self.gridLayout_19.addWidget(self._grid_color_picker, 1, 3, 1, 1)

        self._grid_titles_fz = QDoubleSpinBox(self._grid_titles)
        self._grid_titles_fz.setObjectName(u"_grid_titles_fz")
        self._grid_titles_fz.setDecimals(1)
        self._grid_titles_fz.setMinimum(1.000000000000000)
        self._grid_titles_fz.setValue(10.000000000000000)

        self.gridLayout_19.addWidget(self._grid_titles_fz, 0, 2, 1, 2)


        self.verticalLayout_5.addWidget(self._grid_titles)

        self.QuickSettings.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_6 = QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_17 = QGridLayout(self.groupBox_6)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, -1, 0, -1)
        self.line_20 = QFrame(self.groupBox_6)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_17.addWidget(self.line_20, 0, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.gridLayout_17.addWidget(self.label_28, 0, 0, 1, 1)

        self._set_bgcolor = QLineEdit(self.groupBox_6)
        self._set_bgcolor.setObjectName(u"_set_bgcolor")

        self.gridLayout_17.addWidget(self._set_bgcolor, 0, 2, 1, 1)

        self._set_bgd_picker = QToolButton(self.groupBox_6)
        self._set_bgd_picker.setObjectName(u"_set_bgd_picker")

        self.gridLayout_17.addWidget(self._set_bgd_picker, 0, 3, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_6)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self._sig_demean = QCheckBox(self.groupBox_2)
        self._sig_demean.setObjectName(u"_sig_demean")

        self.horizontalLayout.addWidget(self._sig_demean)

        self._sig_detrend = QCheckBox(self.groupBox_2)
        self._sig_detrend.setObjectName(u"_sig_detrend")

        self.horizontalLayout.addWidget(self._sig_detrend)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self._sig_filt = QGroupBox(self.groupBox_2)
        self._sig_filt.setObjectName(u"_sig_filt")
        self._sig_filt.setCheckable(True)
        self._sig_filt.setChecked(False)
        self.gridLayout_4 = QGridLayout(self._sig_filt)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self._sig_disp = QComboBox(self._sig_filt)
        self._sig_disp.addItem("")
        self._sig_disp.addItem("")
        self._sig_disp.addItem("")
        self._sig_disp.addItem("")
        self._sig_disp.setObjectName(u"_sig_disp")

        self.gridLayout_4.addWidget(self._sig_disp, 0, 2, 1, 1)

        self.label_42 = QLabel(self._sig_filt)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font1)

        self.gridLayout_4.addWidget(self.label_42, 3, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.line_37 = QFrame(self._sig_filt)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_37, 1, 1, 1, 1)

        self.label_10 = QLabel(self._sig_filt)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)

        self._sig_fmin = QDoubleSpinBox(self._sig_filt)
        self._sig_fmin.setObjectName(u"_sig_fmin")
        self._sig_fmin.setMinimum(0.010000000000000)
        self._sig_fmin.setMaximum(10000.000000000000000)
        self._sig_fmin.setValue(8.000000000000000)

        self.gridLayout_10.addWidget(self._sig_fmin, 0, 2, 1, 1)

        self._sig_fmax = QDoubleSpinBox(self._sig_filt)
        self._sig_fmax.setObjectName(u"_sig_fmax")
        self._sig_fmax.setMinimum(0.010000000000000)
        self._sig_fmax.setMaximum(10000.000000000000000)
        self._sig_fmax.setValue(13.000000000000000)

        self.gridLayout_10.addWidget(self._sig_fmax, 1, 2, 1, 1)

        self.line_13 = QFrame(self._sig_filt)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_13, 0, 1, 1, 1)

        self.label_11 = QLabel(self._sig_filt)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_10.addWidget(self.label_11, 1, 0, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_22, 2, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_10, 2, 2, 1, 1)

        self.line_11 = QFrame(self._sig_filt)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_11, 2, 1, 1, 1)

        self.line_7 = QFrame(self._sig_filt)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_7, 1, 1, 1, 1)

        self.label_8 = QLabel(self._sig_filt)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)

        self._sig_filter = QComboBox(self._sig_filt)
        self._sig_filter.addItem("")
        self._sig_filter.addItem("")
        self._sig_filter.addItem("")
        self._sig_filter.addItem("")
        self._sig_filter.setObjectName(u"_sig_filter")

        self.gridLayout_4.addWidget(self._sig_filter, 1, 2, 1, 1)

        self.label_5 = QLabel(self._sig_filt)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.line_43 = QFrame(self._sig_filt)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.Shape.VLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_43, 3, 1, 1, 1)

        self.line_5 = QFrame(self._sig_filt)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_5, 0, 1, 1, 1)

        self.label_7 = QLabel(self._sig_filt)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.line_50 = QFrame(self._sig_filt)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.Shape.VLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_25.addWidget(self.line_50, 1, 1, 1, 1)

        self._sig_order = QSpinBox(self._sig_filt)
        self._sig_order.setObjectName(u"_sig_order")
        self._sig_order.setValue(1)

        self.gridLayout_25.addWidget(self._sig_order, 1, 2, 1, 1)

        self.label_49 = QLabel(self._sig_filt)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font1)

        self.gridLayout_25.addWidget(self.label_49, 1, 0, 1, 1)

        self._sig_meth = QComboBox(self._sig_filt)
        self._sig_meth.addItem("")
        self._sig_meth.addItem("")
        self._sig_meth.setObjectName(u"_sig_meth")

        self.gridLayout_25.addWidget(self._sig_meth, 0, 2, 1, 1)

        self.line_51 = QFrame(self._sig_filt)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.Shape.VLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_25.addWidget(self.line_51, 0, 1, 1, 1)

        self.label_57 = QLabel(self._sig_filt)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font1)

        self.gridLayout_25.addWidget(self.label_57, 0, 0, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_27, 2, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_25, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 4, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self._sig_filt_apply = QPushButton(self._sig_filt)
        self._sig_filt_apply.setObjectName(u"_sig_filt_apply")

        self.horizontalLayout_4.addWidget(self._sig_filt_apply)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 5, 0, 1, 3)


        self.verticalLayout_11.addWidget(self._sig_filt)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.QuickSettings.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self._annot_table = QTableWidget(self.tab_3)
        if (self._annot_table.columnCount() < 4):
            self._annot_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self._annot_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self._annot_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self._annot_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self._annot_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self._annot_table.setObjectName(u"_annot_table")
        self._annot_table.setAlternatingRowColors(True)

        self.verticalLayout_6.addWidget(self._annot_table)

        self._annot_viz = QGroupBox(self.tab_3)
        self._annot_viz.setObjectName(u"_annot_viz")
        self._annot_viz.setCheckable(True)
        self._annot_viz.setChecked(False)
        self.gridLayout_18 = QGridLayout(self._annot_viz)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.line_33 = QFrame(self._annot_viz)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.Shape.VLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_18.addWidget(self.line_33, 1, 1, 1, 1)

        self._annot_color = QLineEdit(self._annot_viz)
        self._annot_color.setObjectName(u"_annot_color")

        self.gridLayout_18.addWidget(self._annot_color, 2, 2, 1, 1)

        self.label_35 = QLabel(self._annot_viz)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font1)

        self.gridLayout_18.addWidget(self.label_35, 0, 0, 1, 1)

        self.line_35 = QFrame(self._annot_viz)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.Shape.VLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_18.addWidget(self.line_35, 2, 1, 1, 1)

        self.line_32 = QFrame(self._annot_viz)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.Shape.VLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_18.addWidget(self.line_32, 0, 1, 1, 1)

        self.label_38 = QLabel(self._annot_viz)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)

        self.gridLayout_18.addWidget(self.label_38, 1, 0, 1, 1)

        self.label_40 = QLabel(self._annot_viz)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)

        self.gridLayout_18.addWidget(self.label_40, 2, 0, 1, 1)

        self._sig_annot_picker = QToolButton(self._annot_viz)
        self._sig_annot_picker.setObjectName(u"_sig_annot_picker")

        self.gridLayout_18.addWidget(self._sig_annot_picker, 2, 3, 1, 1)

        self._annot_marksz = QDoubleSpinBox(self._annot_viz)
        self._annot_marksz.setObjectName(u"_annot_marksz")
        self._annot_marksz.setMinimum(1.000000000000000)
        self._annot_marksz.setMaximum(500.000000000000000)
        self._annot_marksz.setValue(13.000000000000000)

        self.gridLayout_18.addWidget(self._annot_marksz, 1, 2, 1, 2)

        self._annot_txtsz = QDoubleSpinBox(self._annot_viz)
        self._annot_txtsz.setObjectName(u"_annot_txtsz")
        self._annot_txtsz.setDecimals(1)
        self._annot_txtsz.setMinimum(1.000000000000000)
        self._annot_txtsz.setMaximum(500.000000000000000)
        self._annot_txtsz.setValue(14.000000000000000)

        self.gridLayout_18.addWidget(self._annot_txtsz, 0, 2, 1, 2)


        self.verticalLayout_6.addWidget(self._annot_viz)

        self.QuickSettings.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.QuickSettings)

        self.splitter.addWidget(self.q_widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self._GridWidget = QWidget(self.widget1)
        self._GridWidget.setObjectName(u"_GridWidget")
        self.verticalLayout_8 = QVBoxLayout(self._GridWidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self._GridLayout = QVBoxLayout()
        self._GridLayout.setObjectName(u"_GridLayout")
        self._GridLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._GridLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addLayout(self._GridLayout)


        self.horizontalLayout_7.addWidget(self._GridWidget)

        self._SignalWidget = QWidget(self.widget1)
        self._SignalWidget.setObjectName(u"_SignalWidget")
        self.verticalLayout_7 = QVBoxLayout(self._SignalWidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self._SignalLayout = QVBoxLayout()
        self._SignalLayout.setObjectName(u"_SignalLayout")
        self._SignalLayout.setContentsMargins(-1, 0, 0, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._SignalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self._SignalLayout)


        self.horizontalLayout_7.addWidget(self._SignalWidget)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self._sig_next = QPushButton(self.widget1)
        self._sig_next.setObjectName(u"_sig_next")

        self.gridLayout_8.addWidget(self._sig_next, 0, 6, 1, 1)

        self._txt_shape = QLabel(self.widget1)
        self._txt_shape.setObjectName(u"_txt_shape")

        self.gridLayout_8.addWidget(self._txt_shape, 0, 4, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_14, 0, 5, 1, 1)

        self._sig_prev = QPushButton(self.widget1)
        self._sig_prev.setObjectName(u"_sig_prev")

        self.gridLayout_8.addWidget(self._sig_prev, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 0, 7, 1, 1)

        self._sig_index = QSpinBox(self.widget1)
        self._sig_index.setObjectName(u"_sig_index")

        self.gridLayout_8.addWidget(self._sig_index, 0, 3, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_8)

        self.splitter.addWidget(self.widget1)

        self.horizontalLayout_10.addWidget(self.splitter)

        self.widget1.raise_()
        self.q_widget.raise_()
        self.widget1.raise_()
        self.q_widget.raise_()

        self.horizontalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1197, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSave = QMenu(self.menuFile)
        self.menuSave.setObjectName(u"menuSave")
        self.menuLoad = QMenu(self.menuFile)
        self.menuLoad.setObjectName(u"menuLoad")
        self.menuDisplay = QMenu(self.menubar)
        self.menuDisplay.setObjectName(u"menuDisplay")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.QuickSettings, self._sig_title)
        QWidget.setTabOrder(self._sig_title, self._sig_form)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addAction(self.menuLoad.menuAction())
        self.menuFile.addAction(self.menuScreenshot)
        self.menuSave.addAction(self.saveAnnotations)
        self.menuLoad.addAction(self.loadAnnotations)
        self.menuDisplay.addAction(self.actionQSP)
        self.menuDisplay.addAction(self.actionGrid)
        self.menuDisplay.addAction(self.actionSignal)

        self.retranslateUi(MainWindow)

        self.QuickSettings.setCurrentIndex(0)
        self._PlottingForm.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Signal", None))
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
        self.menuScreenshot.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
#if QT_CONFIG(shortcut)
        self.menuScreenshot.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionGrid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
#if QT_CONFIG(shortcut)
        self.actionGrid.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.actionSignal.setText(QCoreApplication.translate("MainWindow", u"Signal", None))
#if QT_CONFIG(shortcut)
        self.actionSignal.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.actionQSP.setText(QCoreApplication.translate("MainWindow", u"Quick settings panel", None))
#if QT_CONFIG(shortcut)
        self.actionQSP.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.saveAnnotations.setText(QCoreApplication.translate("MainWindow", u"Annotations", None))
        self.loadAnnotations.setText(QCoreApplication.translate("MainWindow", u"Annotations", None))
#if QT_CONFIG(tooltip)
        self.QuickSettings.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Axis and label", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"title", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Axis\n"
"color", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"ticks", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"label", None))
        self._axis_color.setPlaceholderText(QCoreApplication.translate("MainWindow", u"black, #ab4642, (0, 0, 0)...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Signal\n"
"color", None))
        self._sig_color.setPlaceholderText(QCoreApplication.translate("MainWindow", u"black, #ab4642, (0, 0, 0)...", None))
        self._sig_ax_picker.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Font\n"
"size", None))
        self._sig_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title for the signal layout", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"x-label", None))
        self._sig_xlab.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X-label for the signal layout", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Font\n"
"size", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"y-label", None))
        self._sig_ylab.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y-label for the signal layout", None))
        self._sig_sig_picker.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Plotting form", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Form", None))
        self._sig_form.setItemText(0, QCoreApplication.translate("MainWindow", u"line", None))
        self._sig_form.setItemText(1, QCoreApplication.translate("MainWindow", u"marker", None))
        self._sig_form.setItemText(2, QCoreApplication.translate("MainWindow", u"histogram", None))
        self._sig_form.setItemText(3, QCoreApplication.translate("MainWindow", u"tf", None))
        self._sig_form.setItemText(4, QCoreApplication.translate("MainWindow", u"psd", None))
        self._sig_form.setItemText(5, QCoreApplication.translate("MainWindow", u"butterfly", None))

        self._sig_amp.setTitle(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self._sig_th.setTitle(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"linewidth", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Symbol", None))
        self._sig_symbol.setItemText(0, QCoreApplication.translate("MainWindow", u"disc", None))
        self._sig_symbol.setItemText(1, QCoreApplication.translate("MainWindow", u"arrow", None))
        self._sig_symbol.setItemText(2, QCoreApplication.translate("MainWindow", u"ring", None))
        self._sig_symbol.setItemText(3, QCoreApplication.translate("MainWindow", u"clobber", None))
        self._sig_symbol.setItemText(4, QCoreApplication.translate("MainWindow", u"square", None))
        self._sig_symbol.setItemText(5, QCoreApplication.translate("MainWindow", u"diamond", None))
        self._sig_symbol.setItemText(6, QCoreApplication.translate("MainWindow", u"vbar", None))
        self._sig_symbol.setItemText(7, QCoreApplication.translate("MainWindow", u"hbar", None))
        self._sig_symbol.setItemText(8, QCoreApplication.translate("MainWindow", u"cross", None))
        self._sig_symbol.setItemText(9, QCoreApplication.translate("MainWindow", u"tailed_arrow", None))
        self._sig_symbol.setItemText(10, QCoreApplication.translate("MainWindow", u"x", None))
        self._sig_symbol.setItemText(11, QCoreApplication.translate("MainWindow", u"triangle_up", None))
        self._sig_symbol.setItemText(12, QCoreApplication.translate("MainWindow", u"triangle_down", None))
        self._sig_symbol.setItemText(13, QCoreApplication.translate("MainWindow", u"star", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"nbins", None))
        self._sig_tf_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self._sig_tf_interp.setItemText(0, QCoreApplication.translate("MainWindow", u"gaussian", None))
        self._sig_tf_interp.setItemText(1, QCoreApplication.translate("MainWindow", u"nearest", None))
        self._sig_tf_interp.setItemText(2, QCoreApplication.translate("MainWindow", u"bilinear", None))
        self._sig_tf_interp.setItemText(3, QCoreApplication.translate("MainWindow", u"quadric", None))
        self._sig_tf_interp.setItemText(4, QCoreApplication.translate("MainWindow", u"bicubic", None))
        self._sig_tf_interp.setItemText(5, QCoreApplication.translate("MainWindow", u"hanning", None))
        self._sig_tf_interp.setItemText(6, QCoreApplication.translate("MainWindow", u"hamming", None))
        self._sig_tf_interp.setItemText(7, QCoreApplication.translate("MainWindow", u"blackman", None))
        self._sig_tf_interp.setItemText(8, QCoreApplication.translate("MainWindow", u"kaiser", None))
        self._sig_tf_interp.setItemText(9, QCoreApplication.translate("MainWindow", u"hermite", None))
        self._sig_tf_interp.setItemText(10, QCoreApplication.translate("MainWindow", u"catrom", None))
        self._sig_tf_interp.setItemText(11, QCoreApplication.translate("MainWindow", u"mitchell", None))
        self._sig_tf_interp.setItemText(12, QCoreApplication.translate("MainWindow", u"spline16", None))
        self._sig_tf_interp.setItemText(13, QCoreApplication.translate("MainWindow", u"spline36", None))
        self._sig_tf_interp.setItemText(14, QCoreApplication.translate("MainWindow", u"bessel", None))
        self._sig_tf_interp.setItemText(15, QCoreApplication.translate("MainWindow", u"sinc", None))
        self._sig_tf_interp.setItemText(16, QCoreApplication.translate("MainWindow", u"lanczos", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Interpolation", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Normalization", None))
        self._sig_baseline.setTitle(QCoreApplication.translate("MainWindow", u"Baseline", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self._sig_averaging.setTitle(QCoreApplication.translate("MainWindow", u"Averaging", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Overlap", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self._sig_norm.setItemText(0, QCoreApplication.translate("MainWindow", u"No normalization", None))
        self._sig_norm.setItemText(1, QCoreApplication.translate("MainWindow", u"Subtract the mean", None))
        self._sig_norm.setItemText(2, QCoreApplication.translate("MainWindow", u"Divide by the mean", None))
        self._sig_norm.setItemText(3, QCoreApplication.translate("MainWindow", u"Subtract then divide by the mean", None))
        self._sig_norm.setItemText(4, QCoreApplication.translate("MainWindow", u"Z-score", None))

        self._sig_tf_clim.setTitle(QCoreApplication.translate("MainWindow", u"Colorbar limits", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Colormap", None))
        self._sig_tf_rev.setText(QCoreApplication.translate("MainWindow", u"Reversed", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"nperseg", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"noverlap", None))
        self._sig_smooth.setText(QCoreApplication.translate("MainWindow", u"Use smooth lines", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Signal", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Line\n"
"width", None))
        self._grid_smooth.setText(QCoreApplication.translate("MainWindow", u"Use smooth lines", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Grid organization", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Number of\n"
"rows", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Number of\n"
"columns", None))
        self._grid_reorg_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self._grid_titles.setTitle(QCoreApplication.translate("MainWindow", u"Titles", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Font\n"
"size", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self._grid_titles_color.setPlaceholderText(QCoreApplication.translate("MainWindow", u"black, #ab4642, (0, 0, 0)...", None))
        self._grid_color_picker.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Grid", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Background", None))
        self._set_bgcolor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"black, #ab4642, (0, 0, 0)...", None))
        self._set_bgd_picker.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Signal processing", None))
        self._sig_demean.setText(QCoreApplication.translate("MainWindow", u"Demean", None))
        self._sig_detrend.setText(QCoreApplication.translate("MainWindow", u"Detrend", None))
        self._sig_filt.setTitle(QCoreApplication.translate("MainWindow", u"Filtering", None))
        self._sig_disp.setItemText(0, QCoreApplication.translate("MainWindow", u"filter", None))
        self._sig_disp.setItemText(1, QCoreApplication.translate("MainWindow", u"amplitude", None))
        self._sig_disp.setItemText(2, QCoreApplication.translate("MainWindow", u"power", None))
        self._sig_disp.setItemText(3, QCoreApplication.translate("MainWindow", u"phase", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Fmin", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Fmax", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self._sig_filter.setItemText(0, QCoreApplication.translate("MainWindow", u"bandpass", None))
        self._sig_filter.setItemText(1, QCoreApplication.translate("MainWindow", u"bandstop", None))
        self._sig_filter.setItemText(2, QCoreApplication.translate("MainWindow", u"lowpass", None))
        self._sig_filter.setItemText(3, QCoreApplication.translate("MainWindow", u"highpass", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Filter\n"
"type", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self._sig_meth.setItemText(0, QCoreApplication.translate("MainWindow", u"butterworth", None))
        self._sig_meth.setItemText(1, QCoreApplication.translate("MainWindow", u"bessel", None))

        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self._sig_filt_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
        ___qtablewidgetitem = self._annot_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem1 = self._annot_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None));
        ___qtablewidgetitem2 = self._annot_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Signal", None));
        ___qtablewidgetitem3 = self._annot_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        self._annot_viz.setTitle(QCoreApplication.translate("MainWindow", u"Appearance", None))
        self._annot_color.setPlaceholderText(QCoreApplication.translate("MainWindow", u"black, #ab4642, (0, 0, 0)...", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Text size", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Marker size", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self._sig_annot_picker.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Annotations", None))
        self._sig_next.setText(QCoreApplication.translate("MainWindow", u"Next >>", None))
        self._txt_shape.setText(QCoreApplication.translate("MainWindow", u"[shape]", None))
        self._sig_prev.setText(QCoreApplication.translate("MainWindow", u" << Previous", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuLoad.setTitle(QCoreApplication.translate("MainWindow", u"Load", None))
        self.menuDisplay.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
    # retranslateUi

