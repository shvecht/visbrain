# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screenshot_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Screenshot(object):
    def setupUi(self, Screenshot):
        if not Screenshot.objectName():
            Screenshot.setObjectName(u"Screenshot")
        Screenshot.resize(341, 563)
        self.verticalLayout_3 = QVBoxLayout(Screenshot)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(Screenshot)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setItalic(True)
        self.label.setFont(font)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self._ssSelect = QComboBox(Screenshot)
        self._ssSelect.addItem("")
        self._ssSelect.addItem("")
        self._ssSelect.setObjectName(u"_ssSelect")

        self.gridLayout_5.addWidget(self._ssSelect, 0, 2, 1, 1)

        self.line = QFrame(Screenshot)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_5)

        self._ssCanvasW = QWidget(Screenshot)
        self._ssCanvasW.setObjectName(u"_ssCanvasW")
        self.verticalLayout_2 = QVBoxLayout(self._ssCanvasW)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self._ssCustomW = QWidget(self._ssCanvasW)
        self._ssCustomW.setObjectName(u"_ssCustomW")
        self.verticalLayout = QVBoxLayout(self._ssCustomW)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self._ssCustomW)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self._ssWidth = QDoubleSpinBox(self._ssCustomW)
        self._ssWidth.setObjectName(u"_ssWidth")
        self._ssWidth.setMaximum(10000.000000000000000)
        self._ssWidth.setValue(10.000000000000000)

        self.gridLayout.addWidget(self._ssWidth, 0, 1, 1, 1)

        self.label_6 = QLabel(self._ssCustomW)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self._ssCustomW)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self._ssHeight = QDoubleSpinBox(self._ssCustomW)
        self._ssHeight.setObjectName(u"_ssHeight")
        self._ssHeight.setMaximum(10000.000000000000000)
        self._ssHeight.setValue(10.000000000000000)

        self.gridLayout.addWidget(self._ssHeight, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 2, 1, 1)

        self.label_3 = QLabel(self._ssCustomW)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.line_6 = QFrame(self._ssCustomW)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 5, 2, 1, 1)

        self._ssBgcolor = QLineEdit(self._ssCustomW)
        self._ssBgcolor.setObjectName(u"_ssBgcolor")
        self._ssBgcolor.setEnabled(False)

        self.gridLayout_3.addWidget(self._ssBgcolor, 3, 2, 1, 1)

        self._ssUnit = QComboBox(self._ssCustomW)
        self._ssUnit.addItem("")
        self._ssUnit.addItem("")
        self._ssUnit.addItem("")
        self._ssUnit.addItem("")
        self._ssUnit.setObjectName(u"_ssUnit")

        self.gridLayout_3.addWidget(self._ssUnit, 1, 2, 1, 1)

        self._ssDpi = QSpinBox(self._ssCustomW)
        self._ssDpi.setObjectName(u"_ssDpi")
        self._ssDpi.setMinimum(100)
        self._ssDpi.setMaximum(600)
        self._ssDpi.setValue(300)

        self.gridLayout_3.addWidget(self._ssDpi, 2, 2, 1, 1)

        self.line_5 = QFrame(self._ssCustomW)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 1, 1, 1, 1)

        self.line_4 = QFrame(self._ssCustomW)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 0, 1, 1, 1)

        self.line_8 = QFrame(self._ssCustomW)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_8, 3, 1, 1, 1)

        self.label_4 = QLabel(self._ssCustomW)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self._ssTransp = QCheckBox(self._ssCustomW)
        self._ssTransp.setObjectName(u"_ssTransp")

        self.gridLayout_3.addWidget(self._ssTransp, 4, 0, 1, 3)

        self._ssBgcolorChk = QCheckBox(self._ssCustomW)
        self._ssBgcolorChk.setObjectName(u"_ssBgcolorChk")
        self._ssBgcolorChk.setFont(font)

        self.gridLayout_3.addWidget(self._ssBgcolorChk, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.gridLayout_2.addWidget(self._ssCustomW, 3, 0, 1, 3)

        self._ssFactorW = QWidget(self._ssCanvasW)
        self._ssFactorW.setObjectName(u"_ssFactorW")
        self.verticalLayout_4 = QVBoxLayout(self._ssFactorW)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.label_9 = QLabel(self._ssFactorW)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self._ssFactor = QDoubleSpinBox(self._ssFactorW)
        self._ssFactor.setObjectName(u"_ssFactor")
        self._ssFactor.setMinimum(0.100000000000000)
        self._ssFactor.setMaximum(20.000000000000000)
        self._ssFactor.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self._ssFactor, 0, 2, 1, 1)

        self.line_7 = QFrame(self._ssFactorW)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_7, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)


        self.gridLayout_2.addWidget(self._ssFactorW, 4, 0, 1, 3)

        self._ssCanvasName = QComboBox(self._ssCanvasW)
        self._ssCanvasName.setObjectName(u"_ssCanvasName")

        self.gridLayout_2.addWidget(self._ssCanvasName, 0, 2, 1, 1)

        self._ssResolution = QComboBox(self._ssCanvasW)
        self._ssResolution.addItem("")
        self._ssResolution.addItem("")
        self._ssResolution.setObjectName(u"_ssResolution")

        self.gridLayout_2.addWidget(self._ssResolution, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self._ssAutocrop = QCheckBox(self._ssCanvasW)
        self._ssAutocrop.setObjectName(u"_ssAutocrop")

        self.gridLayout_2.addWidget(self._ssAutocrop, 5, 0, 1, 3)

        self.label_8 = QLabel(self._ssCanvasW)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_2 = QLabel(self._ssCanvasW)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.line_2 = QFrame(self._ssCanvasW)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 0, 1, 1, 1)

        self.line_3 = QFrame(self._ssCanvasW)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self._ssCanvasW)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self._ssRun = QPushButton(Screenshot)
        self._ssRun.setObjectName(u"_ssRun")

        self.horizontalLayout_2.addWidget(self._ssRun)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(Screenshot)

        QMetaObject.connectSlotsByName(Screenshot)
    # setupUi

    def retranslateUi(self, Screenshot):
        Screenshot.setWindowTitle(QCoreApplication.translate("Screenshot", u"Form", None))
        self.label.setText(QCoreApplication.translate("Screenshot", u"Render", None))
        self._ssSelect.setItemText(0, QCoreApplication.translate("Screenshot", u"Selected canvas", None))
        self._ssSelect.setItemText(1, QCoreApplication.translate("Screenshot", u"Entire window", None))

#if QT_CONFIG(tooltip)
        self._ssSelect.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Render either :</p><p>- The entire window</p><p>- One selected canvas</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Screenshot", u"Size", None))
#if QT_CONFIG(tooltip)
        self._ssWidth.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Width (in centimeter, millimeter, pixel or inch) of rendered image at the dpi level</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Screenshot", u"Width", None))
        self.label_7.setText(QCoreApplication.translate("Screenshot", u"Height", None))
#if QT_CONFIG(tooltip)
        self._ssHeight.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Height (in centimeter, millimeter, pixel or inch) of rendered image at the dpi level</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Screenshot", u"dpi", None))
#if QT_CONFIG(tooltip)
        self._ssBgcolor.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Use either the name of the color (e.g. black, white...), a RGB tuple (e.g. (0., 1., 0.)...) or an hexadecimal string (e.g. #ab4642)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssBgcolor.setPlaceholderText(QCoreApplication.translate("Screenshot", u"black, (.1, .1, .1), #ab4642...", None))
        self._ssUnit.setItemText(0, QCoreApplication.translate("Screenshot", u"centimeter", None))
        self._ssUnit.setItemText(1, QCoreApplication.translate("Screenshot", u"millimeter", None))
        self._ssUnit.setItemText(2, QCoreApplication.translate("Screenshot", u"pixel", None))
        self._ssUnit.setItemText(3, QCoreApplication.translate("Screenshot", u"inch", None))

#if QT_CONFIG(tooltip)
        self._ssUnit.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Size unit</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._ssDpi.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>dpi level for the rendered image</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Screenshot", u"Unit", None))
#if QT_CONFIG(tooltip)
        self._ssTransp.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Force to have a transparent background</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssTransp.setText(QCoreApplication.translate("Screenshot", u"Use transparent background", None))
#if QT_CONFIG(tooltip)
        self._ssBgcolorChk.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p><span style=\" font-style:normal;\">Change the background color.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssBgcolorChk.setText(QCoreApplication.translate("Screenshot", u"Background\n"
"color", None))
        self.label_9.setText(QCoreApplication.translate("Screenshot", u"Factor", None))
#if QT_CONFIG(tooltip)
        self._ssFactor.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Multiply the original canvas size by this factor. For instance, if the canvas has a size of (1020, 800) and factor is 2. then the rendered image will have a size of (2040, 1600)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._ssCanvasName.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Choose the canvas to render</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssResolution.setItemText(0, QCoreApplication.translate("Screenshot", u"Custom image size", None))
        self._ssResolution.setItemText(1, QCoreApplication.translate("Screenshot", u"Proportional to screen size", None))

#if QT_CONFIG(tooltip)
        self._ssResolution.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Change the image resolution for rendering :</p><p>- <span style=\" font-weight:600;\">Custom  :</span> specify the image size (controlled by unit) at a specific dpi level. Note that the rendering might not have the exact desired size but will try instead to conserve the proportion width/height</p><p>- <span style=\" font-weight:600;\">Proportional :</span> increase the size of the image proportionaly to the original canvas size.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._ssAutocrop.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Automatically crop the image to non-background values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssAutocrop.setText(QCoreApplication.translate("Screenshot", u"autocrop", None))
        self.label_8.setText(QCoreApplication.translate("Screenshot", u"Image resolution", None))
        self.label_2.setText(QCoreApplication.translate("Screenshot", u"Canvas name", None))
#if QT_CONFIG(tooltip)
        self._ssRun.setToolTip(QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Run the screenshot</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssRun.setText(QCoreApplication.translate("Screenshot", u"Run", None))
    # retranslateUi

