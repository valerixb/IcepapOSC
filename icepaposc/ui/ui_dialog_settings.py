# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_settings.ui'
#
# Created: Thu Nov 22 07:53:47 2018
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
        DialogSettings.setModal(False)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DialogSettings)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gbSampling = QtGui.QGroupBox(DialogSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbSampling.sizePolicy().hasHeightForWidth())
        self.gbSampling.setSizePolicy(sizePolicy)
        self.gbSampling.setObjectName(_fromUtf8("gbSampling"))
        self.glDataCollection = QtGui.QGridLayout(self.gbSampling)
        self.glDataCollection.setObjectName(_fromUtf8("glDataCollection"))
        self.labelGuiRate = QtGui.QLabel(self.gbSampling)
        self.labelGuiRate.setObjectName(_fromUtf8("labelGuiRate"))
        self.glDataCollection.addWidget(self.labelGuiRate, 2, 1, 1, 1)
        self.sbSampleRate = QtGui.QSpinBox(self.gbSampling)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbSampleRate.sizePolicy().hasHeightForWidth())
        self.sbSampleRate.setSizePolicy(sizePolicy)
        self.sbSampleRate.setMinimumSize(QtCore.QSize(80, 0))
        self.sbSampleRate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sbSampleRate.setObjectName(_fromUtf8("sbSampleRate"))
        self.glDataCollection.addWidget(self.sbSampleRate, 0, 2, 1, 1)
        self.leGuiUpdateRate = QtGui.QLineEdit(self.gbSampling)
        self.leGuiUpdateRate.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leGuiUpdateRate.sizePolicy().hasHeightForWidth())
        self.leGuiUpdateRate.setSizePolicy(sizePolicy)
        self.leGuiUpdateRate.setMinimumSize(QtCore.QSize(80, 0))
        self.leGuiUpdateRate.setMaximumSize(QtCore.QSize(80, 16777215))
        self.leGuiUpdateRate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leGuiUpdateRate.setObjectName(_fromUtf8("leGuiUpdateRate"))
        self.glDataCollection.addWidget(self.leGuiUpdateRate, 2, 2, 1, 1)
        self.labelSampleRate = QtGui.QLabel(self.gbSampling)
        self.labelSampleRate.setObjectName(_fromUtf8("labelSampleRate"))
        self.glDataCollection.addWidget(self.labelSampleRate, 0, 1, 1, 1)
        self.sbDumpRate = QtGui.QSpinBox(self.gbSampling)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbDumpRate.sizePolicy().hasHeightForWidth())
        self.sbDumpRate.setSizePolicy(sizePolicy)
        self.sbDumpRate.setMinimumSize(QtCore.QSize(80, 0))
        self.sbDumpRate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sbDumpRate.setObjectName(_fromUtf8("sbDumpRate"))
        self.glDataCollection.addWidget(self.sbDumpRate, 1, 2, 1, 1)
        self.labelDumpRate = QtGui.QLabel(self.gbSampling)
        self.labelDumpRate.setObjectName(_fromUtf8("labelDumpRate"))
        self.glDataCollection.addWidget(self.labelDumpRate, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.gbSampling)
        self.gbXAxis = QtGui.QGroupBox(DialogSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbXAxis.sizePolicy().hasHeightForWidth())
        self.gbXAxis.setSizePolicy(sizePolicy)
        self.gbXAxis.setMaximumSize(QtCore.QSize(16777215, 170))
        self.gbXAxis.setObjectName(_fromUtf8("gbXAxis"))
        self.glXAxis = QtGui.QGridLayout(self.gbXAxis)
        self.glXAxis.setObjectName(_fromUtf8("glXAxis"))
        self.labelXAxisLength = QtGui.QLabel(self.gbXAxis)
        self.labelXAxisLength.setObjectName(_fromUtf8("labelXAxisLength"))
        self.glXAxis.addWidget(self.labelXAxisLength, 0, 0, 1, 1)
        self.sbLenAxisX = QtGui.QSpinBox(self.gbXAxis)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbLenAxisX.sizePolicy().hasHeightForWidth())
        self.sbLenAxisX.setSizePolicy(sizePolicy)
        self.sbLenAxisX.setMinimumSize(QtCore.QSize(80, 0))
        self.sbLenAxisX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sbLenAxisX.setObjectName(_fromUtf8("sbLenAxisX"))
        self.glXAxis.addWidget(self.sbLenAxisX, 0, 1, 1, 1)
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
        self.labelGuiRate.setText(_translate("DialogSettings", "Resulting GUI Update Rate [ms]", None))
        self.labelSampleRate.setText(_translate("DialogSettings", "Sample Rate [ms]", None))
        self.labelDumpRate.setText(_translate("DialogSettings", "GUI Dump Rate [samples/dump]", None))
        self.gbXAxis.setTitle(_translate("DialogSettings", "X-axis", None))
        self.labelXAxisLength.setText(_translate("DialogSettings", "Default Length [sec]", None))

