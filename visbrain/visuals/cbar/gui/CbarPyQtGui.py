# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CbarPyQtGui.ui'
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
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(489, 881)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self._cbar_grp = QGroupBox(Form)
        self._cbar_grp.setObjectName(u"_cbar_grp")
        self._cbar_grp.setCheckable(True)
        self._cbar_grp.setChecked(False)
        self.verticalLayout_10 = QVBoxLayout(self._cbar_grp)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.CbarLayout = QVBoxLayout()
        self.CbarLayout.setObjectName(u"CbarLayout")
        self.CbarLayout.setContentsMargins(-1, 0, -1, -1)
        self.groupBox_4 = QGroupBox(self._cbar_grp)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.object = QComboBox(self.groupBox_4)
        self.object.setObjectName(u"object")

        self.gridLayout_9.addWidget(self.object, 0, 2, 1, 1)

        self.line_12 = QFrame(self.groupBox_4)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_12, 0, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_9.addWidget(self.label_18, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 1, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_9)


        self.CbarLayout.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self._cbar_grp)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.border = QCheckBox(self.groupBox_3)
        self.border.setObjectName(u"border")
        font = QFont()
        font.setItalic(True)
        self.border.setFont(font)

        self.gridLayout_7.addWidget(self.border, 4, 0, 1, 1)

        self.line_7 = QFrame(self.groupBox_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_7, 1, 1, 1, 1)

        self.bw = QDoubleSpinBox(self.groupBox_3)
        self.bw.setObjectName(u"bw")
        self.bw.setDecimals(1)
        self.bw.setMinimum(0.100000000000000)

        self.gridLayout_7.addWidget(self.bw, 4, 2, 1, 1)

        self.width = QDoubleSpinBox(self.groupBox_3)
        self.width.setObjectName(u"width")
        self.width.setSingleStep(0.010000000000000)

        self.gridLayout_7.addWidget(self.width, 3, 2, 1, 1)

        self.txtCol = QLineEdit(self.groupBox_3)
        self.txtCol.setObjectName(u"txtCol")

        self.gridLayout_7.addWidget(self.txtCol, 1, 2, 1, 1)

        self.ndigits = QSpinBox(self.groupBox_3)
        self.ndigits.setObjectName(u"ndigits")
        self.ndigits.setMinimum(1)
        self.ndigits.setMaximum(10)
        self.ndigits.setValue(1)

        self.gridLayout_7.addWidget(self.ndigits, 2, 2, 1, 1)

        self.line_9 = QFrame(self.groupBox_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_9, 2, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_7.addWidget(self.label_16, 2, 0, 1, 1)

        self.line_10 = QFrame(self.groupBox_3)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_10, 3, 1, 1, 1)

        self.bckCol = QLineEdit(self.groupBox_3)
        self.bckCol.setObjectName(u"bckCol")

        self.gridLayout_7.addWidget(self.bckCol, 0, 2, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout_7.addWidget(self.label_17, 3, 0, 1, 1)

        self.line_11 = QFrame(self.groupBox_3)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_11, 4, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.line_6 = QFrame(self.groupBox_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_6, 0, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_7)


        self.CbarLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self._cbar_grp)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cmapRev = QCheckBox(self.groupBox_2)
        self.cmapRev.setObjectName(u"cmapRev")

        self.gridLayout.addWidget(self.cmapRev, 1, 3, 1, 1)

        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 4, 1, 1, 1)

        self.vmaxW = QWidget(self.groupBox_2)
        self.vmaxW.setObjectName(u"vmaxW")
        self.verticalLayout_3 = QVBoxLayout(self.vmaxW)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(9)
        self.over = QLineEdit(self.vmaxW)
        self.over.setObjectName(u"over")

        self.gridLayout_3.addWidget(self.over, 1, 1, 1, 1)

        self.label_5 = QLabel(self.vmaxW)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.vmax = QDoubleSpinBox(self.vmaxW)
        self.vmax.setObjectName(u"vmax")

        self.gridLayout_3.addWidget(self.vmax, 0, 1, 1, 1)

        self.label_6 = QLabel(self.vmaxW)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.gridLayout.addWidget(self.vmaxW, 4, 2, 1, 2)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.line_4 = QFrame(self.groupBox_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.isvmin = QCheckBox(self.groupBox_2)
        self.isvmin.setObjectName(u"isvmin")
        self.isvmin.setFont(font)

        self.gridLayout.addWidget(self.isvmin, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.cmap = QComboBox(self.groupBox_2)
        self.cmap.setObjectName(u"cmap")

        self.gridLayout.addWidget(self.cmap, 1, 2, 1, 1)

        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.climm = QDoubleSpinBox(self.widget)
        self.climm.setObjectName(u"climm")
        self.climm.setMinimum(-16777215.000000000000000)
        self.climm.setMaximum(16777215.000000000000000)

        self.horizontalLayout_3.addWidget(self.climm)

        self.climM = QDoubleSpinBox(self.widget)
        self.climM.setObjectName(u"climM")
        self.climM.setMinimum(-16777215.000000000000000)
        self.climM.setMaximum(16777215.000000000000000)
        self.climM.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.climM)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.widget, 2, 2, 1, 2)

        self.line_3 = QFrame(self.groupBox_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 1, 1, 1)

        self.limTxt = QCheckBox(self.groupBox_2)
        self.limTxt.setObjectName(u"limTxt")
        self.limTxt.setChecked(True)

        self.gridLayout.addWidget(self.limTxt, 5, 0, 1, 4)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 3, 1, 1, 1)

        self.vminW = QWidget(self.groupBox_2)
        self.vminW.setObjectName(u"vminW")
        self.verticalLayout_2 = QVBoxLayout(self.vminW)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(9)
        self.label_3 = QLabel(self.vminW)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.vmin = QDoubleSpinBox(self.vminW)
        self.vmin.setObjectName(u"vmin")
        self.vmin.setDecimals(3)

        self.gridLayout_2.addWidget(self.vmin, 0, 1, 1, 1)

        self.label_4 = QLabel(self.vminW)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.under = QLineEdit(self.vminW)
        self.under.setObjectName(u"under")

        self.gridLayout_2.addWidget(self.under, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.gridLayout.addWidget(self.vminW, 3, 2, 1, 2)

        self.isvmax = QCheckBox(self.groupBox_2)
        self.isvmax.setObjectName(u"isvmax")
        self.isvmax.setFont(font)

        self.gridLayout.addWidget(self.isvmax, 4, 0, 1, 1)

        self.widget_2 = QWidget(self.groupBox_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.autoscale = QPushButton(self.widget_2)
        self.autoscale.setObjectName(u"autoscale")

        self.horizontalLayout.addWidget(self.autoscale)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout.addWidget(self.widget_2, 6, 0, 1, 4)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.CbarLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self._cbar_grp)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.line_5 = QFrame(self.groupBox)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_5, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cblabel = QLineEdit(self.widget_3)
        self.cblabel.setObjectName(u"cblabel")

        self.gridLayout_5.addWidget(self.cblabel, 0, 1, 1, 1)

        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.cbTxtSz = QDoubleSpinBox(self.widget_3)
        self.cbTxtSz.setObjectName(u"cbTxtSz")
        self.cbTxtSz.setDecimals(1)

        self.gridLayout_5.addWidget(self.cbTxtSz, 1, 1, 1, 1)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)

        self.cbTxtSh = QDoubleSpinBox(self.widget_3)
        self.cbTxtSh.setObjectName(u"cbTxtSh")
        self.cbTxtSh.setDecimals(1)
        self.cbTxtSh.setSingleStep(0.100000000000000)

        self.gridLayout_5.addWidget(self.cbTxtSh, 2, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_5)


        self.gridLayout_4.addWidget(self.widget_3, 0, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)

        self.line_8 = QFrame(self.groupBox)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_8, 1, 1, 1, 1)

        self.widget_4 = QWidget(self.groupBox)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_8 = QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.txtSh = QDoubleSpinBox(self.widget_4)
        self.txtSh.setObjectName(u"txtSh")
        self.txtSh.setDecimals(1)
        self.txtSh.setSingleStep(0.100000000000000)

        self.gridLayout_6.addWidget(self.txtSh, 1, 1, 1, 1)

        self.txtSz = QDoubleSpinBox(self.widget_4)
        self.txtSz.setObjectName(u"txtSz")
        self.txtSz.setDecimals(1)

        self.gridLayout_6.addWidget(self.txtSz, 0, 1, 1, 1)

        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_6)


        self.gridLayout_4.addWidget(self.widget_4, 1, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.CbarLayout.addWidget(self.groupBox)


        self.verticalLayout_10.addLayout(self.CbarLayout)


        self.verticalLayout.addWidget(self._cbar_grp)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self._cbar_grp.setTitle(QCoreApplication.translate("Form", u"Display", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Objects", None))
#if QT_CONFIG(tooltip)
        self.object.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Colorbar object to control</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("Form", u"Colorbar of", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.border.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Display / hide the border of the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.border.setText(QCoreApplication.translate("Form", u"Border", None))
#if QT_CONFIG(tooltip)
        self.bw.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Width of the border</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.width.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Width of the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txtCol.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Color of the text and of the border (if shown)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ndigits.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Number of digits a fine control of clim/vmin/vmax</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Form", u"Textcolor", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Number of\n"
"digits", None))
#if QT_CONFIG(tooltip)
        self.bckCol.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Background color of the colorbar canvas</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("Form", u"Colorbar\n"
"width", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Background\n"
"color", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Color properties", None))
#if QT_CONFIG(tooltip)
        self.cmapRev.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Reverse the colormap's colors</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cmapRev.setText(QCoreApplication.translate("Form", u"Reversed", None))
#if QT_CONFIG(tooltip)
        self.over.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Every value under vmax are going to be set to this color</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Value", None))
#if QT_CONFIG(tooltip)
        self.vmax.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Value of the maximum threshold</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Over\n"
"color", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Clim", None))
        self.label.setText(QCoreApplication.translate("Form", u"Colormap", None))
#if QT_CONFIG(tooltip)
        self.isvmin.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Enable / Disable a minimum threshold</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.isvmin.setText(QCoreApplication.translate("Form", u"Vmin", None))
#if QT_CONFIG(tooltip)
        self.cmap.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Colormap to use</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.climm.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Minimum of the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.climM.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Maximum of the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.limTxt.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Display vmin/vmax on the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.limTxt.setText(QCoreApplication.translate("Form", u"Display vmin/vmax text", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Value", None))
#if QT_CONFIG(tooltip)
        self.vmin.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Value of the minimum threshold</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Under\n"
"color", None))
#if QT_CONFIG(tooltip)
        self.under.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Every values over vmin are going to be set to this color</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.isvmax.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Enable / Disable a maximum threshold</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.isvmax.setText(QCoreApplication.translate("Form", u"Vmax", None))
#if QT_CONFIG(tooltip)
        self.autoscale.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Automatically scale the colorbar limits to fit with the (minimum, maximum) of currently displayed object</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.autoscale.setText(QCoreApplication.translate("Form", u"Autoscale", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Text properties", None))
#if QT_CONFIG(tooltip)
        self.cblabel.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Title of the colorbar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("Form", u"Size", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Value", None))
#if QT_CONFIG(tooltip)
        self.cbTxtSz.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Text size of the colorbar label</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("Form", u"Shift", None))
#if QT_CONFIG(tooltip)
        self.cbTxtSh.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Shift between the colorbar and the text</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Form", u"Title", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Limits", None))
#if QT_CONFIG(tooltip)
        self.txtSh.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Shift between the colorbar and limits (clim / vmin / vmax)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txtSz.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Text size of limits (clim / vmin / vmax)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("Form", u"Size", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Shift", None))
    # retranslateUi

