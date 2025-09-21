# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'figure_gui.ui'
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
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)

class Ui_FigureMainWindow(object):
    def setupUi(self, FigureMainWindow):
        if not FigureMainWindow.objectName():
            FigureMainWindow.setObjectName(u"FigureMainWindow")
        FigureMainWindow.resize(1200, 800)
        self.actionAddImages = QAction(FigureMainWindow)
        self.actionAddImages.setObjectName(u"actionAddImages")
        self.actionSaveLayout = QAction(FigureMainWindow)
        self.actionSaveLayout.setObjectName(u"actionSaveLayout")
        self.actionLoadLayout = QAction(FigureMainWindow)
        self.actionLoadLayout.setObjectName(u"actionLoadLayout")
        self.actionExportFigure = QAction(FigureMainWindow)
        self.actionExportFigure.setObjectName(u"actionExportFigure")
        self.actionApplyGrid = QAction(FigureMainWindow)
        self.actionApplyGrid.setObjectName(u"actionApplyGrid")
        self.actionResetLayout = QAction(FigureMainWindow)
        self.actionResetLayout.setObjectName(u"actionResetLayout")
        self.actionClose = QAction(FigureMainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.centralwidget = QWidget(FigureMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainSplitter = QSplitter(self.centralwidget)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setOrientation(Qt.Horizontal)
        self.controlsPage = QWidget(self.mainSplitter)
        self.controlsPage.setObjectName(u"controlsPage")
        self.controlsLayout = QVBoxLayout(self.controlsPage)
        self.controlsLayout.setObjectName(u"controlsLayout")
        self.controlsLayout.setContentsMargins(0, 0, 0, 0)
        self.filesGroup = QGroupBox(self.controlsPage)
        self.filesGroup.setObjectName(u"filesGroup")
        self.filesLayout = QVBoxLayout(self.filesGroup)
        self.filesLayout.setObjectName(u"filesLayout")
        self.addImagesButton = QPushButton(self.filesGroup)
        self.addImagesButton.setObjectName(u"addImagesButton")

        self.filesLayout.addWidget(self.addImagesButton)

        self.imageList = QListWidget(self.filesGroup)
        self.imageList.setObjectName(u"imageList")

        self.filesLayout.addWidget(self.imageList)

        self.removeSelectedButton = QPushButton(self.filesGroup)
        self.removeSelectedButton.setObjectName(u"removeSelectedButton")

        self.filesLayout.addWidget(self.removeSelectedButton)


        self.controlsLayout.addWidget(self.filesGroup)

        self.canvasGroup = QGroupBox(self.controlsPage)
        self.canvasGroup.setObjectName(u"canvasGroup")
        self.canvasLayout = QGridLayout(self.canvasGroup)
        self.canvasLayout.setObjectName(u"canvasLayout")
        self.rowsLabel = QLabel(self.canvasGroup)
        self.rowsLabel.setObjectName(u"rowsLabel")

        self.canvasLayout.addWidget(self.rowsLabel, 0, 0, 1, 1)

        self.rowsSpin = QSpinBox(self.canvasGroup)
        self.rowsSpin.setObjectName(u"rowsSpin")
        self.rowsSpin.setMinimum(1)
        self.rowsSpin.setMaximum(12)
        self.rowsSpin.setValue(1)

        self.canvasLayout.addWidget(self.rowsSpin, 0, 1, 1, 1)

        self.colsLabel = QLabel(self.canvasGroup)
        self.colsLabel.setObjectName(u"colsLabel")

        self.canvasLayout.addWidget(self.colsLabel, 0, 2, 1, 1)

        self.colsSpin = QSpinBox(self.canvasGroup)
        self.colsSpin.setObjectName(u"colsSpin")
        self.colsSpin.setMinimum(1)
        self.colsSpin.setMaximum(12)
        self.colsSpin.setValue(1)

        self.canvasLayout.addWidget(self.colsSpin, 0, 3, 1, 1)

        self.hspaceLabel = QLabel(self.canvasGroup)
        self.hspaceLabel.setObjectName(u"hspaceLabel")

        self.canvasLayout.addWidget(self.hspaceLabel, 1, 0, 1, 1)

        self.hspaceSpin = QDoubleSpinBox(self.canvasGroup)
        self.hspaceSpin.setObjectName(u"hspaceSpin")
        self.hspaceSpin.setDecimals(2)
        self.hspaceSpin.setSingleStep(0.050000000000000)
        self.hspaceSpin.setMaximum(2.000000000000000)
        self.hspaceSpin.setValue(0.300000000000000)

        self.canvasLayout.addWidget(self.hspaceSpin, 1, 1, 1, 1)

        self.wspaceLabel = QLabel(self.canvasGroup)
        self.wspaceLabel.setObjectName(u"wspaceLabel")

        self.canvasLayout.addWidget(self.wspaceLabel, 1, 2, 1, 1)

        self.wspaceSpin = QDoubleSpinBox(self.canvasGroup)
        self.wspaceSpin.setObjectName(u"wspaceSpin")
        self.wspaceSpin.setDecimals(2)
        self.wspaceSpin.setSingleStep(0.050000000000000)
        self.wspaceSpin.setMaximum(2.000000000000000)
        self.wspaceSpin.setValue(0.100000000000000)

        self.canvasLayout.addWidget(self.wspaceSpin, 1, 3, 1, 1)

        self.leftMarginLabel = QLabel(self.canvasGroup)
        self.leftMarginLabel.setObjectName(u"leftMarginLabel")

        self.canvasLayout.addWidget(self.leftMarginLabel, 2, 0, 1, 1)

        self.leftMarginSpin = QDoubleSpinBox(self.canvasGroup)
        self.leftMarginSpin.setObjectName(u"leftMarginSpin")
        self.leftMarginSpin.setDecimals(2)
        self.leftMarginSpin.setSingleStep(0.050000000000000)
        self.leftMarginSpin.setMaximum(1.000000000000000)
        self.leftMarginSpin.setValue(0.050000000000000)

        self.canvasLayout.addWidget(self.leftMarginSpin, 2, 1, 1, 1)

        self.rightMarginLabel = QLabel(self.canvasGroup)
        self.rightMarginLabel.setObjectName(u"rightMarginLabel")

        self.canvasLayout.addWidget(self.rightMarginLabel, 2, 2, 1, 1)

        self.rightMarginSpin = QDoubleSpinBox(self.canvasGroup)
        self.rightMarginSpin.setObjectName(u"rightMarginSpin")
        self.rightMarginSpin.setDecimals(2)
        self.rightMarginSpin.setSingleStep(0.050000000000000)
        self.rightMarginSpin.setMaximum(1.000000000000000)
        self.rightMarginSpin.setValue(1.000000000000000)

        self.canvasLayout.addWidget(self.rightMarginSpin, 2, 3, 1, 1)

        self.bottomMarginLabel = QLabel(self.canvasGroup)
        self.bottomMarginLabel.setObjectName(u"bottomMarginLabel")

        self.canvasLayout.addWidget(self.bottomMarginLabel, 3, 0, 1, 1)

        self.bottomMarginSpin = QDoubleSpinBox(self.canvasGroup)
        self.bottomMarginSpin.setObjectName(u"bottomMarginSpin")
        self.bottomMarginSpin.setDecimals(2)
        self.bottomMarginSpin.setSingleStep(0.050000000000000)
        self.bottomMarginSpin.setMaximum(1.000000000000000)
        self.bottomMarginSpin.setValue(0.100000000000000)

        self.canvasLayout.addWidget(self.bottomMarginSpin, 3, 1, 1, 1)

        self.topMarginLabel = QLabel(self.canvasGroup)
        self.topMarginLabel.setObjectName(u"topMarginLabel")

        self.canvasLayout.addWidget(self.topMarginLabel, 3, 2, 1, 1)

        self.topMarginSpin = QDoubleSpinBox(self.canvasGroup)
        self.topMarginSpin.setObjectName(u"topMarginSpin")
        self.topMarginSpin.setDecimals(2)
        self.topMarginSpin.setSingleStep(0.050000000000000)
        self.topMarginSpin.setMaximum(1.000000000000000)
        self.topMarginSpin.setValue(0.900000000000000)

        self.canvasLayout.addWidget(self.topMarginSpin, 3, 3, 1, 1)


        self.controlsLayout.addWidget(self.canvasGroup)

        self.figureGroup = QGroupBox(self.controlsPage)
        self.figureGroup.setObjectName(u"figureGroup")
        self.figureLayout = QFormLayout(self.figureGroup)
        self.figureLayout.setObjectName(u"figureLayout")
        self.titleLabel = QLabel(self.figureGroup)
        self.titleLabel.setObjectName(u"titleLabel")

        self.figureLayout.setWidget(0, QFormLayout.LabelRole, self.titleLabel)

        self.figureTitleEdit = QLineEdit(self.figureGroup)
        self.figureTitleEdit.setObjectName(u"figureTitleEdit")

        self.figureLayout.setWidget(0, QFormLayout.FieldRole, self.figureTitleEdit)

        self.widthLabel = QLabel(self.figureGroup)
        self.widthLabel.setObjectName(u"widthLabel")

        self.figureLayout.setWidget(1, QFormLayout.LabelRole, self.widthLabel)

        self.figWidthSpin = QDoubleSpinBox(self.figureGroup)
        self.figWidthSpin.setObjectName(u"figWidthSpin")
        self.figWidthSpin.setDecimals(1)
        self.figWidthSpin.setMinimum(2.000000000000000)
        self.figWidthSpin.setMaximum(40.000000000000000)
        self.figWidthSpin.setSingleStep(0.500000000000000)
        self.figWidthSpin.setValue(10.000000000000000)

        self.figureLayout.setWidget(1, QFormLayout.FieldRole, self.figWidthSpin)

        self.heightLabel = QLabel(self.figureGroup)
        self.heightLabel.setObjectName(u"heightLabel")

        self.figureLayout.setWidget(2, QFormLayout.LabelRole, self.heightLabel)

        self.figHeightSpin = QDoubleSpinBox(self.figureGroup)
        self.figHeightSpin.setObjectName(u"figHeightSpin")
        self.figHeightSpin.setDecimals(1)
        self.figHeightSpin.setMinimum(2.000000000000000)
        self.figHeightSpin.setMaximum(40.000000000000000)
        self.figHeightSpin.setSingleStep(0.500000000000000)
        self.figHeightSpin.setValue(10.000000000000000)

        self.figureLayout.setWidget(2, QFormLayout.FieldRole, self.figHeightSpin)


        self.controlsLayout.addWidget(self.figureGroup)

        self.exportGroup = QGroupBox(self.controlsPage)
        self.exportGroup.setObjectName(u"exportGroup")
        self.exportLayout = QVBoxLayout(self.exportGroup)
        self.exportLayout.setObjectName(u"exportLayout")
        self.exportForm = QFormLayout()
        self.exportForm.setObjectName(u"exportForm")
        self.fileLabel = QLabel(self.exportGroup)
        self.fileLabel.setObjectName(u"fileLabel")

        self.exportForm.setWidget(0, QFormLayout.LabelRole, self.fileLabel)

        self.pathLayout = QHBoxLayout()
        self.pathLayout.setObjectName(u"pathLayout")
        self.exportPathEdit = QLineEdit(self.exportGroup)
        self.exportPathEdit.setObjectName(u"exportPathEdit")

        self.pathLayout.addWidget(self.exportPathEdit)

        self.browseButton = QToolButton(self.exportGroup)
        self.browseButton.setObjectName(u"browseButton")

        self.pathLayout.addWidget(self.browseButton)


        self.exportForm.setLayout(0, QFormLayout.FieldRole, self.pathLayout)

        self.formatLabel = QLabel(self.exportGroup)
        self.formatLabel.setObjectName(u"formatLabel")

        self.exportForm.setWidget(1, QFormLayout.LabelRole, self.formatLabel)

        self.formatCombo = QComboBox(self.exportGroup)
        self.formatCombo.addItem("")
        self.formatCombo.addItem("")
        self.formatCombo.addItem("")
        self.formatCombo.addItem("")
        self.formatCombo.setObjectName(u"formatCombo")

        self.exportForm.setWidget(1, QFormLayout.FieldRole, self.formatCombo)

        self.dpiLabel = QLabel(self.exportGroup)
        self.dpiLabel.setObjectName(u"dpiLabel")

        self.exportForm.setWidget(2, QFormLayout.LabelRole, self.dpiLabel)

        self.dpiSpin = QSpinBox(self.exportGroup)
        self.dpiSpin.setObjectName(u"dpiSpin")
        self.dpiSpin.setMinimum(72)
        self.dpiSpin.setMaximum(1200)
        self.dpiSpin.setValue(300)

        self.exportForm.setWidget(2, QFormLayout.FieldRole, self.dpiSpin)


        self.exportLayout.addLayout(self.exportForm)

        self.openAfterExportCheck = QCheckBox(self.exportGroup)
        self.openAfterExportCheck.setObjectName(u"openAfterExportCheck")

        self.exportLayout.addWidget(self.openAfterExportCheck)

        self.exportButtonsLayout = QHBoxLayout()
        self.exportButtonsLayout.setObjectName(u"exportButtonsLayout")
        self.saveLayoutButton = QPushButton(self.exportGroup)
        self.saveLayoutButton.setObjectName(u"saveLayoutButton")

        self.exportButtonsLayout.addWidget(self.saveLayoutButton)

        self.loadLayoutButton = QPushButton(self.exportGroup)
        self.loadLayoutButton.setObjectName(u"loadLayoutButton")

        self.exportButtonsLayout.addWidget(self.loadLayoutButton)


        self.exportLayout.addLayout(self.exportButtonsLayout)

        self.exportButton = QPushButton(self.exportGroup)
        self.exportButton.setObjectName(u"exportButton")

        self.exportLayout.addWidget(self.exportButton)


        self.controlsLayout.addWidget(self.exportGroup)

        self.controlsSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.controlsLayout.addItem(self.controlsSpacer)

        self.mainSplitter.addWidget(self.controlsPage)
        self.previewPage = QWidget(self.mainSplitter)
        self.previewPage.setObjectName(u"previewPage")
        self.previewLayout = QVBoxLayout(self.previewPage)
        self.previewLayout.setSpacing(6)
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewLayout.setContentsMargins(0, 0, 0, 0)
        self.previewGroup = QGroupBox(self.previewPage)
        self.previewGroup.setObjectName(u"previewGroup")
        self.previewGroupLayout = QVBoxLayout(self.previewGroup)
        self.previewGroupLayout.setObjectName(u"previewGroupLayout")
        self.previewLabel = QLabel(self.previewGroup)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setFrameShape(QFrame.StyledPanel)
        self.previewLabel.setAlignment(Qt.AlignCenter)
        self.previewLabel.setMinimumSize(QSize(400, 400))

        self.previewGroupLayout.addWidget(self.previewLabel)


        self.previewLayout.addWidget(self.previewGroup)

        self.previewButtonsLayout = QHBoxLayout()
        self.previewButtonsLayout.setObjectName(u"previewButtonsLayout")
        self.refreshPreviewButton = QPushButton(self.previewPage)
        self.refreshPreviewButton.setObjectName(u"refreshPreviewButton")

        self.previewButtonsLayout.addWidget(self.refreshPreviewButton)

        self.clearPreviewButton = QPushButton(self.previewPage)
        self.clearPreviewButton.setObjectName(u"clearPreviewButton")

        self.previewButtonsLayout.addWidget(self.clearPreviewButton)

        self.previewButtonsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.previewButtonsLayout.addItem(self.previewButtonsSpacer)


        self.previewLayout.addLayout(self.previewButtonsLayout)

        self.mainSplitter.addWidget(self.previewPage)

        self.mainLayout.addWidget(self.mainSplitter)

        FigureMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FigureMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        FigureMainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(FigureMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuLayout = QMenu(self.menubar)
        self.menuLayout.setObjectName(u"menuLayout")
        FigureMainWindow.setMenuBar(self.menubar)

        FigureMainWindow.addAction(self.actionAddImages)
        FigureMainWindow.addAction(self.actionSaveLayout)
        FigureMainWindow.addAction(self.actionLoadLayout)
        FigureMainWindow.addAction(self.actionExportFigure)
        FigureMainWindow.addAction(self.actionApplyGrid)
        FigureMainWindow.addAction(self.actionResetLayout)
        FigureMainWindow.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLayout.menuAction())
        self.menuFile.addAction(self.actionAddImages)
        self.menuFile.addAction(self.actionSaveLayout)
        self.menuFile.addAction(self.actionLoadLayout)
        self.menuFile.addAction(self.actionExportFigure)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuLayout.addAction(self.actionApplyGrid)
        self.menuLayout.addAction(self.actionResetLayout)

        self.retranslateUi(FigureMainWindow)

        self.exportButton.setDefault(True)


        QMetaObject.connectSlotsByName(FigureMainWindow)
    # setupUi

    def retranslateUi(self, FigureMainWindow):
        FigureMainWindow.setWindowTitle(QCoreApplication.translate("FigureMainWindow", u"Visbrain Figure Builder", None))
        self.actionAddImages.setText(QCoreApplication.translate("FigureMainWindow", u"Add Images\u2026", None))
        self.actionSaveLayout.setText(QCoreApplication.translate("FigureMainWindow", u"Save Layout\u2026", None))
        self.actionLoadLayout.setText(QCoreApplication.translate("FigureMainWindow", u"Load Layout\u2026", None))
        self.actionExportFigure.setText(QCoreApplication.translate("FigureMainWindow", u"Export Figure", None))
        self.actionApplyGrid.setText(QCoreApplication.translate("FigureMainWindow", u"Apply Grid", None))
        self.actionResetLayout.setText(QCoreApplication.translate("FigureMainWindow", u"Reset Layout", None))
        self.actionClose.setText(QCoreApplication.translate("FigureMainWindow", u"Close", None))
        self.filesGroup.setTitle(QCoreApplication.translate("FigureMainWindow", u"Figure content", None))
        self.addImagesButton.setText(QCoreApplication.translate("FigureMainWindow", u"Add Images\u2026", None))
        self.removeSelectedButton.setText(QCoreApplication.translate("FigureMainWindow", u"Remove Selected", None))
        self.canvasGroup.setTitle(QCoreApplication.translate("FigureMainWindow", u"Canvas arrangement", None))
        self.rowsLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Rows:", None))
        self.colsLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Columns:", None))
        self.hspaceLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Vertical spacing:", None))
        self.wspaceLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Horizontal spacing:", None))
        self.leftMarginLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Left margin:", None))
        self.rightMarginLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Right margin:", None))
        self.bottomMarginLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Bottom margin:", None))
        self.topMarginLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Top margin:", None))
        self.figureGroup.setTitle(QCoreApplication.translate("FigureMainWindow", u"Figure settings", None))
        self.titleLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Title:", None))
        self.widthLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Width (in):", None))
        self.heightLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Height (in):", None))
        self.exportGroup.setTitle(QCoreApplication.translate("FigureMainWindow", u"Export", None))
        self.fileLabel.setText(QCoreApplication.translate("FigureMainWindow", u"File:", None))
        self.browseButton.setText(QCoreApplication.translate("FigureMainWindow", u"\u2026", None))
        self.formatLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Format:", None))
        self.formatCombo.setItemText(0, QCoreApplication.translate("FigureMainWindow", u"png", None))
        self.formatCombo.setItemText(1, QCoreApplication.translate("FigureMainWindow", u"jpg", None))
        self.formatCombo.setItemText(2, QCoreApplication.translate("FigureMainWindow", u"tiff", None))
        self.formatCombo.setItemText(3, QCoreApplication.translate("FigureMainWindow", u"pdf", None))

        self.dpiLabel.setText(QCoreApplication.translate("FigureMainWindow", u"DPI:", None))
        self.openAfterExportCheck.setText(QCoreApplication.translate("FigureMainWindow", u"Open file after export", None))
        self.saveLayoutButton.setText(QCoreApplication.translate("FigureMainWindow", u"Save Layout\u2026", None))
        self.loadLayoutButton.setText(QCoreApplication.translate("FigureMainWindow", u"Load Layout\u2026", None))
        self.exportButton.setText(QCoreApplication.translate("FigureMainWindow", u"Export Figure", None))
        self.previewGroup.setTitle(QCoreApplication.translate("FigureMainWindow", u"Preview", None))
        self.previewLabel.setText(QCoreApplication.translate("FigureMainWindow", u"Drop images here or use \u201cAdd Images\u2026\u201d", None))
        self.refreshPreviewButton.setText(QCoreApplication.translate("FigureMainWindow", u"Refresh Preview", None))
        self.clearPreviewButton.setText(QCoreApplication.translate("FigureMainWindow", u"Clear Preview", None))
        self.menuFile.setTitle(QCoreApplication.translate("FigureMainWindow", u"&File", None))
        self.menuLayout.setTitle(QCoreApplication.translate("FigureMainWindow", u"&Layout", None))
    # retranslateUi

