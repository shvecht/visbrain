# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screenshot_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from visbrain.qt import QtCore, QtGui, QtWidgets


class Ui_Screenshot(object):
    def setupUi(self, Screenshot):
        if not Screenshot.objectName():
            Screenshot.setObjectName(u"Screenshot")
        Screenshot.resize(341, 563)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Screenshot)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QtWidgets.QLabel(Screenshot)
        self.label.setObjectName(u"label")
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self._ssSelect = QtWidgets.QComboBox(Screenshot)
        self._ssSelect.addItem("")
        self._ssSelect.addItem("")
        self._ssSelect.setObjectName(u"_ssSelect")

        self.gridLayout_5.addWidget(self._ssSelect, 0, 2, 1, 1)

        self.line = QtWidgets.QFrame(Screenshot)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_5)

        self._ssCanvasW = QtWidgets.QWidget(Screenshot)
        self._ssCanvasW.setObjectName(u"_ssCanvasW")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self._ssCanvasW)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self._ssCustomW = QtWidgets.QWidget(self._ssCanvasW)
        self._ssCustomW.setObjectName(u"_ssCustomW")
        self.verticalLayout = QtWidgets.QVBoxLayout(self._ssCustomW)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self._ssCustomW)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self._ssWidth = QtWidgets.QDoubleSpinBox(self._ssCustomW)
        self._ssWidth.setObjectName(u"_ssWidth")
        self._ssWidth.setMaximum(10000.000000000000000)
        self._ssWidth.setValue(10.000000000000000)

        self.gridLayout.addWidget(self._ssWidth, 0, 1, 1, 1)

        self.label_6 = QtWidgets.QLabel(self._ssCustomW)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QtWidgets.QLabel(self._ssCustomW)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self._ssHeight = QtWidgets.QDoubleSpinBox(self._ssCustomW)
        self._ssHeight.setObjectName(u"_ssHeight")
        self._ssHeight.setMaximum(10000.000000000000000)
        self._ssHeight.setValue(10.000000000000000)

        self.gridLayout.addWidget(self._ssHeight, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 2, 1, 1)

        self.label_3 = QtWidgets.QLabel(self._ssCustomW)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.line_6 = QtWidgets.QFrame(self._ssCustomW)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 5, 2, 1, 1)

        self._ssBgcolor = QtWidgets.QLineEdit(self._ssCustomW)
        self._ssBgcolor.setObjectName(u"_ssBgcolor")
        self._ssBgcolor.setEnabled(False)

        self.gridLayout_3.addWidget(self._ssBgcolor, 3, 2, 1, 1)

        self._ssUnit = QtWidgets.QComboBox(self._ssCustomW)
        self._ssUnit.addItem("")
        self._ssUnit.addItem("")
        self._ssUnit.addItem("")
        self._ssUnit.addItem("")
        self._ssUnit.setObjectName(u"_ssUnit")

        self.gridLayout_3.addWidget(self._ssUnit, 1, 2, 1, 1)

        self._ssDpi = QtWidgets.QSpinBox(self._ssCustomW)
        self._ssDpi.setObjectName(u"_ssDpi")
        self._ssDpi.setMinimum(100)
        self._ssDpi.setMaximum(600)
        self._ssDpi.setValue(300)

        self.gridLayout_3.addWidget(self._ssDpi, 2, 2, 1, 1)

        self.line_5 = QtWidgets.QFrame(self._ssCustomW)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 1, 1, 1, 1)

        self.line_4 = QtWidgets.QFrame(self._ssCustomW)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 0, 1, 1, 1)

        self.line_8 = QtWidgets.QFrame(self._ssCustomW)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_8, 3, 1, 1, 1)

        self.label_4 = QtWidgets.QLabel(self._ssCustomW)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self._ssTransp = QtWidgets.QCheckBox(self._ssCustomW)
        self._ssTransp.setObjectName(u"_ssTransp")

        self.gridLayout_3.addWidget(self._ssTransp, 4, 0, 1, 3)

        self._ssBgcolorChk = QtWidgets.QCheckBox(self._ssCustomW)
        self._ssBgcolorChk.setObjectName(u"_ssBgcolorChk")
        self._ssBgcolorChk.setFont(font)

        self.gridLayout_3.addWidget(self._ssBgcolorChk, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.gridLayout_2.addWidget(self._ssCustomW, 3, 0, 1, 3)

        self._ssFactorW = QtWidgets.QWidget(self._ssCanvasW)
        self._ssFactorW.setObjectName(u"_ssFactorW")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self._ssFactorW)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_6 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.label_9 = QtWidgets.QLabel(self._ssFactorW)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self._ssFactor = QtWidgets.QDoubleSpinBox(self._ssFactorW)
        self._ssFactor.setObjectName(u"_ssFactor")
        self._ssFactor.setMinimum(0.100000000000000)
        self._ssFactor.setMaximum(20.000000000000000)
        self._ssFactor.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self._ssFactor, 0, 2, 1, 1)

        self.line_7 = QtWidgets.QFrame(self._ssFactorW)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_7, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)


        self.gridLayout_2.addWidget(self._ssFactorW, 4, 0, 1, 3)

        self._ssCanvasName = QtWidgets.QComboBox(self._ssCanvasW)
        self._ssCanvasName.setObjectName(u"_ssCanvasName")

        self.gridLayout_2.addWidget(self._ssCanvasName, 0, 2, 1, 1)

        self._ssResolution = QtWidgets.QComboBox(self._ssCanvasW)
        self._ssResolution.addItem("")
        self._ssResolution.addItem("")
        self._ssResolution.setObjectName(u"_ssResolution")

        self.gridLayout_2.addWidget(self._ssResolution, 2, 2, 1, 1)

        self.horizontalSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self._ssAutocrop = QtWidgets.QCheckBox(self._ssCanvasW)
        self._ssAutocrop.setObjectName(u"_ssAutocrop")

        self.gridLayout_2.addWidget(self._ssAutocrop, 5, 0, 1, 3)

        self.label_8 = QtWidgets.QLabel(self._ssCanvasW)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self._ssCanvasW)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.line_2 = QtWidgets.QFrame(self._ssCanvasW)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 0, 1, 1, 1)

        self.line_3 = QtWidgets.QFrame(self._ssCanvasW)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self._ssCanvasW)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self._ssRun = QtWidgets.QPushButton(Screenshot)
        self._ssRun.setObjectName(u"_ssRun")

        self.horizontalLayout_2.addWidget(self._ssRun)

        self.horizontalSpacer_4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(Screenshot)

        QtCore.QMetaObject.connectSlotsByName(Screenshot)
    # setupUi

    def retranslateUi(self, Screenshot):
        Screenshot.setWindowTitle(QtCore.QCoreApplication.translate("Screenshot", u"Screenshot", None))
        self.label.setText(QtCore.QCoreApplication.translate("Screenshot", u"Render", None))
        self._ssSelect.setItemText(0, QtCore.QCoreApplication.translate("Screenshot", u"Selected canvas", None))
        self._ssSelect.setItemText(1, QtCore.QCoreApplication.translate("Screenshot", u"Entire window", None))

#if QT_CONFIG(tooltip)
        self._ssSelect.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Render either :</p><p>- The entire window</p><p>- One selected canvas</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QtCore.QCoreApplication.translate("Screenshot", u"Size", None))
#if QT_CONFIG(tooltip)
        self._ssWidth.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Width (in centimeter, millimeter, pixel or inch) of rendered image at the dpi level</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QtCore.QCoreApplication.translate("Screenshot", u"Width", None))
        self.label_7.setText(QtCore.QCoreApplication.translate("Screenshot", u"Height", None))
#if QT_CONFIG(tooltip)
        self._ssHeight.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Height (in centimeter, millimeter, pixel or inch) of rendered image at the dpi level</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QtCore.QCoreApplication.translate("Screenshot", u"dpi", None))
#if QT_CONFIG(tooltip)
        self._ssBgcolor.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Use either the name of the color (e.g. black, white...), a RGB tuple (e.g. (0., 1., 0.)...) or an hexadecimal string (e.g. #ab4642)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssBgcolor.setPlaceholderText(QtCore.QCoreApplication.translate("Screenshot", u"black, (.1, .1, .1), #ab4642...", None))
        self._ssUnit.setItemText(0, QtCore.QCoreApplication.translate("Screenshot", u"centimeter", None))
        self._ssUnit.setItemText(1, QtCore.QCoreApplication.translate("Screenshot", u"millimeter", None))
        self._ssUnit.setItemText(2, QtCore.QCoreApplication.translate("Screenshot", u"pixel", None))
        self._ssUnit.setItemText(3, QtCore.QCoreApplication.translate("Screenshot", u"inch", None))

#if QT_CONFIG(tooltip)
        self._ssUnit.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Size unit</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._ssDpi.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>dpi level for the rendered image</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QtCore.QCoreApplication.translate("Screenshot", u"Unit", None))
#if QT_CONFIG(tooltip)
        self._ssTransp.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Force to have a transparent background</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssTransp.setText(QtCore.QCoreApplication.translate("Screenshot", u"Use transparent background", None))
#if QT_CONFIG(tooltip)
        self._ssBgcolorChk.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p><span style=\" font-style:normal;\">Change the background color.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssBgcolorChk.setText(QtCore.QCoreApplication.translate("Screenshot", u"Background\n"
"color", None))
        self.label_9.setText(QtCore.QCoreApplication.translate("Screenshot", u"Factor", None))
#if QT_CONFIG(tooltip)
        self._ssFactor.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Multiply the original canvas size by this factor. For instance, if the canvas has a size of (1020, 800) and factor is 2. then the rendered image will have a size of (2040, 1600)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._ssCanvasName.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Choose the canvas to render</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssResolution.setItemText(0, QtCore.QCoreApplication.translate("Screenshot", u"Custom image size", None))
        self._ssResolution.setItemText(1, QtCore.QCoreApplication.translate("Screenshot", u"Proportional to screen size", None))

#if QT_CONFIG(tooltip)
        self._ssResolution.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Change the image resolution for rendering :</p><p>- <span style=\" font-weight:600;\">Custom  :</span> specify the image size (controlled by unit) at a specific dpi level. Note that the rendering might not have the exact desired size but will try instead to conserve the proportion width/height</p><p>- <span style=\" font-weight:600;\">Proportional :</span> increase the size of the image proportionaly to the original canvas size.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self._ssAutocrop.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Automatically crop the image to non-background values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssAutocrop.setText(QtCore.QCoreApplication.translate("Screenshot", u"autocrop", None))
        self.label_8.setText(QtCore.QCoreApplication.translate("Screenshot", u"Image resolution", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("Screenshot", u"Canvas name", None))
#if QT_CONFIG(tooltip)
        self._ssRun.setToolTip(QtCore.QCoreApplication.translate("Screenshot", u"<html><head/><body><p>Run the screenshot</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self._ssRun.setText(QtCore.QCoreApplication.translate("Screenshot", u"Run", None))
    # retranslateUi

