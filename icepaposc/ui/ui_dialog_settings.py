# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_settings.ui'
#
# Created: Wed Nov 21 13:11:12 2018
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogSettings(object):
    def setupUi(self, DialogSettings):
        DialogSettings.setObjectName(_fromUtf8("DialogSettings"))
        DialogSettings.resize(396, 249)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogSettings.sizePolicy().hasHeightForWidth())
        DialogSettings.setSizePolicy(sizePolicy)
        DialogSettings.setModal(False)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DialogSettings)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gbSampling = QtGui.QGroupBox(DialogSettings)
        self.gbSampling.setObjectName(_fromUtf8("gbSampling"))
        self.gridLayout = QtGui.QGridLayout(self.gbSampling)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelSampleRate = QtGui.QLabel(self.gbSampling)
        self.labelSampleRate.setObjectName(_fromUtf8("labelSampleRate"))
        self.gridLayout.addWidget(self.labelSampleRate, 0, 0, 1, 1)
        self.sbSampleRate = QtGui.QSpinBox(self.gbSampling)
        self.sbSampleRate.setObjectName(_fromUtf8("sbSampleRate"))
        self.gridLayout.addWidget(self.sbSampleRate, 0, 2, 1, 1)
        self.labelDumpRate = QtGui.QLabel(self.gbSampling)
        self.labelDumpRate.setObjectName(_fromUtf8("labelDumpRate"))
        self.gridLayout.addWidget(self.labelDumpRate, 1, 0, 1, 1)
        self.sbDumpRate = QtGui.QSpinBox(self.gbSampling)
        self.sbDumpRate.setObjectName(_fromUtf8("sbDumpRate"))
        self.gridLayout.addWidget(self.sbDumpRate, 1, 1, 1, 2)
        self.labelGuiRate = QtGui.QLabel(self.gbSampling)
        self.labelGuiRate.setObjectName(_fromUtf8("labelGuiRate"))
        self.gridLayout.addWidget(self.labelGuiRate, 2, 0, 1, 2)
        self.leGuiUpdateRate = QtGui.QLineEdit(self.gbSampling)
        self.leGuiUpdateRate.setEnabled(False)
        self.leGuiUpdateRate.setObjectName(_fromUtf8("leGuiUpdateRate"))
        self.gridLayout.addWidget(self.leGuiUpdateRate, 2, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.gbSampling)
        self.gbXAxis = QtGui.QGroupBox(DialogSettings)
        self.gbXAxis.setMinimumSize(QtCore.QSize(378, 70))
        self.gbXAxis.setMaximumSize(QtCore.QSize(16777215, 170))
        self.gbXAxis.setObjectName(_fromUtf8("gbXAxis"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gbXAxis)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelXAxisLength = QtGui.QLabel(self.gbXAxis)
        self.labelXAxisLength.setObjectName(_fromUtf8("labelXAxisLength"))
        self.gridLayout_2.addWidget(self.labelXAxisLength, 0, 0, 1, 1)
        self.sbLenAxisX = QtGui.QSpinBox(self.gbXAxis)
        self.sbLenAxisX.setObjectName(_fromUtf8("sbLenAxisX"))
        self.gridLayout_2.addWidget(self.sbLenAxisX, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.gbXAxis)
        self.bbApplyClose = QtGui.QDialogButtonBox(DialogSettings)
        self.bbApplyClose.setOrientation(QtCore.Qt.Horizontal)
        self.bbApplyClose.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Close)
        self.bbApplyClose.setObjectName(_fromUtf8("bbApplyClose"))
        self.verticalLayout_2.addWidget(self.bbApplyClose)

        self.retranslateUi(DialogSettings)
        QtCore.QObject.connect(self.bbApplyClose, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogSettings.accept)
        QtCore.QObject.connect(self.bbApplyClose, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogSettings)

    def retranslateUi(self, DialogSettings):
        DialogSettings.setWindowTitle(_translate("DialogSettings", "Oscilloscope Settings", None))
        self.gbSampling.setTitle(_translate("DialogSettings", "Data Collection", None))
        self.labelSampleRate.setText(_translate("DialogSettings", "Sample Rate [ms between samples]", None))
        self.labelDumpRate.setText(_translate("DialogSettings", "GUI Dump Rate [samples/dump]", None))
        self.labelGuiRate.setText(_translate("DialogSettings", "Resulting GUI Update Rate [ms]", None))
        self.gbXAxis.setTitle(_translate("DialogSettings", "X-axis", None))
        self.labelXAxisLength.setText(_translate("DialogSettings", "Default/Reset Length [seconds]", None))

