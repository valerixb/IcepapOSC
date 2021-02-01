# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogstatusinfo.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogStatusInfo(object):
    def setupUi(self, DialogStatusInfo):
        DialogStatusInfo.setObjectName("DialogStatusInfo")
        DialogStatusInfo.resize(428, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogStatusInfo.sizePolicy().hasHeightForWidth())
        DialogStatusInfo.setSizePolicy(sizePolicy)
        DialogStatusInfo.setMinimumSize(QtCore.QSize(50, 0))
        DialogStatusInfo.setStyleSheet("font: 9pt ;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DialogStatusInfo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(DialogStatusInfo)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnUpdate = QtWidgets.QPushButton(DialogStatusInfo)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.txt1Command = QtWidgets.QLineEdit(DialogStatusInfo)
        self.txt1Command.setObjectName("txt1Command")
        self.horizontalLayout.addWidget(self.txt1Command)
        self.cbAllDrivers = QtWidgets.QComboBox(DialogStatusInfo)
        self.cbAllDrivers.setEditable(True)
        self.cbAllDrivers.setObjectName("cbAllDrivers")
        self.horizontalLayout.addWidget(self.cbAllDrivers)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DialogStatusInfo)
        QtCore.QMetaObject.connectSlotsByName(DialogStatusInfo)

    def retranslateUi(self, DialogStatusInfo):
        _translate = QtCore.QCoreApplication.translate
        DialogStatusInfo.setWindowTitle(_translate("DialogStatusInfo", "Status Info"))
        self.btnUpdate.setText(_translate("DialogStatusInfo", "VSTATUS"))


