# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CbarPyQtGui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from visbrain.qt import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(489, 881)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self._cbar_grp = QtWidgets.QGroupBox(Form)
        self._cbar_grp.setObjectName(u"_cbar_grp")
        self._cbar_grp.setCheckable(True)
        self._cbar_grp.setChecked(False)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self._cbar_grp)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.CbarLayout = QtWidgets.QVBoxLayout()
        self.CbarLayout.setObjectName(u"CbarLayout")
        self.CbarLayout.setContentsMargins(-1, 0, -1, -1)
        self.groupBox_4 = QtWidgets.QGroupBox(self._cbar_grp)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.object = QtWidgets.QComboBox(self.groupBox_4)
        self.object.setObjectName(u"object")

        self.gridLayout_9.addWidget(self.object, 0, 2, 1, 1)

        self.line_12 = QtWidgets.QFrame(self.groupBox_4)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_12, 0, 1, 1, 1)

        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_9.addWidget(self.label_18, 0, 0, 1, 1)

        self.horizontalSpacer = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 1, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_9)


        self.CbarLayout.addWidget(self.groupBox_4)

        self.groupBox_3 = QtWidgets.QGroupBox(self._cbar_grp)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.border = QtWidgets.QCheckBox(self.groupBox_3)
        self.border.setObjectName(u"border")
        font = QtGui.QFont()
        font.setItalic(True)
        self.border.setFont(font)

        self.gridLayout_7.addWidget(self.border, 4, 0, 1, 1)

        self.line_7 = QtWidgets.QFrame(self.groupBox_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_7, 1, 1, 1, 1)

        self.bw = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.bw.setObjectName(u"bw")
        self.bw.setDecimals(1)
        self.bw.setMinimum(0.100000000000000)

        self.gridLayout_7.addWidget(self.bw, 4, 2, 1, 1)

        self.width = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.width.setObjectName(u"width")
        self.width.setSingleStep(0.010000000000000)

        self.gridLayout_7.addWidget(self.width, 3, 2, 1, 1)

        self.txtCol = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtCol.setObjectName(u"txtCol")

        self.gridLayout_7.addWidget(self.txtCol, 1, 2, 1, 1)

        self.ndigits = QtWidgets.QSpinBox(self.groupBox_3)
        self.ndigits.setObjectName(u"ndigits")
        self.ndigits.setMinimum(1)
        self.ndigits.setMaximum(10)
        self.ndigits.setValue(1)

        self.gridLayout_7.addWidget(self.ndigits, 2, 2, 1, 1)

        self.line_9 = QtWidgets.QFrame(self.groupBox_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_9, 2, 1, 1, 1)

        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_7.addWidget(self.label_16, 2, 0, 1, 1)

        self.line_10 = QtWidgets.QFrame(self.groupBox_3)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_10, 3, 1, 1, 1)

        self.bckCol = QtWidgets.QLineEdit(self.groupBox_3)
        self.bckCol.setObjectName(u"bckCol")

        self.gridLayout_7.addWidget(self.bckCol, 0, 2, 1, 1)

        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout_7.addWidget(self.label_17, 3, 0, 1, 1)

        self.line_11 = QtWidgets.QFrame(self.groupBox_3)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_11, 4, 1, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.line_6 = QtWidgets.QFrame(self.groupBox_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_6, 0, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_7)


        self.CbarLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QtWidgets.QGroupBox(self._cbar_grp)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cmapRev = QtWidgets.QCheckBox(self.groupBox_2)
        self.cmapRev.setObjectName(u"cmapRev")

        self.gridLayout.addWidget(self.cmapRev, 1, 3, 1, 1)

        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 4, 1, 1, 1)

        self.vmaxW = QtWidgets.QWidget(self.groupBox_2)
        self.vmaxW.setObjectName(u"vmaxW")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.vmaxW)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(9)
        self.over = QtWidgets.QLineEdit(self.vmaxW)
        self.over.setObjectName(u"over")

        self.gridLayout_3.addWidget(self.over, 1, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.vmaxW)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.vmax = QtWidgets.QDoubleSpinBox(self.vmaxW)
        self.vmax.setObjectName(u"vmax")

        self.gridLayout_3.addWidget(self.vmax, 0, 1, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.vmaxW)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.gridLayout.addWidget(self.vmaxW, 4, 2, 1, 2)

        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.line_4 = QtWidgets.QFrame(self.groupBox_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 1, 1, 1, 1)

        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.isvmin = QtWidgets.QCheckBox(self.groupBox_2)
        self.isvmin.setObjectName(u"isvmin")
        self.isvmin.setFont(font)

        self.gridLayout.addWidget(self.isvmin, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.cmap = QtWidgets.QComboBox(self.groupBox_2)
        self.cmap.setObjectName(u"cmap")

        self.gridLayout.addWidget(self.cmap, 1, 2, 1, 1)

        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.climm = QtWidgets.QDoubleSpinBox(self.widget)
        self.climm.setObjectName(u"climm")
        self.climm.setMinimum(-16777215.000000000000000)
        self.climm.setMaximum(16777215.000000000000000)

        self.horizontalLayout_3.addWidget(self.climm)

        self.climM = QtWidgets.QDoubleSpinBox(self.widget)
        self.climM.setObjectName(u"climM")
        self.climM.setMinimum(-16777215.000000000000000)
        self.climM.setMaximum(16777215.000000000000000)
        self.climM.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.climM)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.widget, 2, 2, 1, 2)

        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 1, 1, 1)

        self.limTxt = QtWidgets.QCheckBox(self.groupBox_2)
        self.limTxt.setObjectName(u"limTxt")
        self.limTxt.setChecked(True)

        self.gridLayout.addWidget(self.limTxt, 5, 0, 1, 4)

        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 3, 1, 1, 1)

        self.vminW = QtWidgets.QWidget(self.groupBox_2)
        self.vminW.setObjectName(u"vminW")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.vminW)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(9)
        self.label_3 = QtWidgets.QLabel(self.vminW)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.vmin = QtWidgets.QDoubleSpinBox(self.vminW)
        self.vmin.setObjectName(u"vmin")
        self.vmin.setDecimals(3)

        self.gridLayout_2.addWidget(self.vmin, 0, 1, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.vminW)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.under = QtWidgets.QLineEdit(self.vminW)
        self.under.setObjectName(u"under")

        self.gridLayout_2.addWidget(self.under, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.gridLayout.addWidget(self.vminW, 3, 2, 1, 2)

        self.isvmax = QtWidgets.QCheckBox(self.groupBox_2)
        self.isvmax.setObjectName(u"isvmax")
        self.isvmax.setFont(font)

        self.gridLayout.addWidget(self.isvmax, 4, 0, 1, 1)

        self.widget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.autoscale = QtWidgets.QPushButton(self.widget_2)
        self.autoscale.setObjectName(u"autoscale")

        self.horizontalLayout.addWidget(self.autoscale)

        self.horizontalSpacer_5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout.addWidget(self.widget_2, 6, 0, 1, 4)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.CbarLayout.addWidget(self.groupBox_2)

        self.groupBox = QtWidgets.QGroupBox(self._cbar_grp)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_5, 0, 1, 1, 1)

        self.widget_3 = QtWidgets.QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cblabel = QtWidgets.QLineEdit(self.widget_3)
        self.cblabel.setObjectName(u"cblabel")

        self.gridLayout_5.addWidget(self.cblabel, 0, 1, 1, 1)

        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.cbTxtSz = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.cbTxtSz.setObjectName(u"cbTxtSz")
        self.cbTxtSz.setDecimals(1)

        self.gridLayout_5.addWidget(self.cbTxtSz, 1, 1, 1, 1)

        self.label_13 = QtWidgets.QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)

        self.cbTxtSh = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.cbTxtSh.setObjectName(u"cbTxtSh")
        self.cbTxtSh.setDecimals(1)
        self.cbTxtSh.setSingleStep(0.100000000000000)

        self.gridLayout_5.addWidget(self.cbTxtSh, 2, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_5)


        self.gridLayout_4.addWidget(self.widget_3, 0, 2, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)

        self.line_8 = QtWidgets.QFrame(self.groupBox)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_8, 1, 1, 1, 1)

        self.widget_4 = QtWidgets.QWidget(self.groupBox)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.txtSh = QtWidgets.QDoubleSpinBox(self.widget_4)
        self.txtSh.setObjectName(u"txtSh")
        self.txtSh.setDecimals(1)
        self.txtSh.setSingleStep(0.100000000000000)

        self.gridLayout_6.addWidget(self.txtSh, 1, 1, 1, 1)

        self.txtSz = QtWidgets.QDoubleSpinBox(self.widget_4)
        self.txtSz.setObjectName(u"txtSz")
        self.txtSz.setDecimals(1)

        self.gridLayout_6.addWidget(self.txtSz, 0, 1, 1, 1)

        self.label_14 = QtWidgets.QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_6)


        self.gridLayout_4.addWidget(self.widget_4, 1, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.CbarLayout.addWidget(self.groupBox)


        self.verticalLayout_10.addLayout(self.CbarLayout)


        self.verticalLayout.addWidget(self._cbar_grp)


        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCore.QCoreApplication.translate("Form", u"Form", None))
        self._cbar_grp.setTitle(QtCore.QCoreApplication.translate("Form", u"Display", None))
        self.groupBox_4.setTitle(QtCore.QCoreApplication.translate("Form", u"Objects", None))
#if QT_CONFIG(tooltip)
        self.object.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Colorbar object to control</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QtCore.QCoreApplication.translate("Form", u"Colorbar of", None))
        self.groupBox_3.setTitle(QtCore.QCoreApplication.translate("Form", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.border.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Display / hide the border of the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.border.setText(QtCore.QCoreApplication.translate("Form", u"Border", None))
#if QT_CONFIG(tooltip)
        self.bw.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Width of the border</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.width.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Width of the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txtCol.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Color of the text and of the border (if shown)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ndigits.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Number of digits a fine control of clim/vmin/vmax</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QtCore.QCoreApplication.translate("Form", u"Textcolor", None))
        self.label_16.setText(QtCore.QCoreApplication.translate("Form", u"Number of\n"
"digits", None))
#if QT_CONFIG(tooltip)
        self.bckCol.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Background color of the colorbar canvas</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QtCore.QCoreApplication.translate("Form", u"Colorbar\n"
"width", None))
        self.label_8.setText(QtCore.QCoreApplication.translate("Form", u"Background\n"
"color", None))
        self.groupBox_2.setTitle(QtCore.QCoreApplication.translate("Form", u"Color properties", None))
#if QT_CONFIG(tooltip)
        self.cmapRev.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Reverse the colormap's colors</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cmapRev.setText(QtCore.QCoreApplication.translate("Form", u"Reversed", None))
#if QT_CONFIG(tooltip)
        self.over.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Every value under vmax are going to be set to this color</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QtCore.QCoreApplication.translate("Form", u"Value", None))
#if QT_CONFIG(tooltip)
        self.vmax.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Value of the maximum threshold</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QtCore.QCoreApplication.translate("Form", u"Over\n"
"color", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("Form", u"Clim", None))
        self.label.setText(QtCore.QCoreApplication.translate("Form", u"Colormap", None))
#if QT_CONFIG(tooltip)
        self.isvmin.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Enable / Disable a minimum threshold</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.isvmin.setText(QtCore.QCoreApplication.translate("Form", u"Vmin", None))
#if QT_CONFIG(tooltip)
        self.cmap.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Colormap to use</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.climm.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Minimum of the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.climM.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Maximum of the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.limTxt.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Display vmin/vmax on the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.limTxt.setText(QtCore.QCoreApplication.translate("Form", u"Display vmin/vmax text", None))
        self.label_3.setText(QtCore.QCoreApplication.translate("Form", u"Value", None))
#if QT_CONFIG(tooltip)
        self.vmin.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Value of the minimum threshold</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QtCore.QCoreApplication.translate("Form", u"Under\n"
"color", None))
#if QT_CONFIG(tooltip)
        self.under.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Every values over vmin are going to be set to this color</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.isvmax.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Enable / Disable a maximum threshold</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.isvmax.setText(QtCore.QCoreApplication.translate("Form", u"Vmax", None))
#if QT_CONFIG(tooltip)
        self.autoscale.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Automatically scale the colorbar limits to fit with the (minimum, maximum) of currently displayed object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.autoscale.setText(QtCore.QCoreApplication.translate("Form", u"Autoscale", None))
        self.groupBox.setTitle(QtCore.QCoreApplication.translate("Form", u"Text properties", None))
#if QT_CONFIG(tooltip)
        self.cblabel.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Title of the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QtCore.QCoreApplication.translate("Form", u"Size", None))
        self.label_10.setText(QtCore.QCoreApplication.translate("Form", u"Value", None))
#if QT_CONFIG(tooltip)
        self.cbTxtSz.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Text size of the colorbar label</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QtCore.QCoreApplication.translate("Form", u"Shift", None))
#if QT_CONFIG(tooltip)
        self.cbTxtSh.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Shift between the colorbar and the text</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QtCore.QCoreApplication.translate("Form", u"Title", None))
        self.label_12.setText(QtCore.QCoreApplication.translate("Form", u"Limits", None))
#if QT_CONFIG(tooltip)
        self.txtSh.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Shift between the colorbar and limits (clim / vmin / vmax)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txtSz.setToolTip(QtCore.QCoreApplication.translate("Form", u"<html><head/><body><p>Text size of limits (clim / vmin / vmax)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QtCore.QCoreApplication.translate("Form", u"Size", None))
        self.label_15.setText(QtCore.QCoreApplication.translate("Form", u"Shift", None))
    # retranslateUi

