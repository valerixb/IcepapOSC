# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_WindowMain(object):
    def setupUi(self, WindowMain):
        WindowMain.setObjectName(_fromUtf8("WindowMain"))
        WindowMain.resize(962, 864)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../.designer/backup/IcepapCfg Icons/gnome-monitor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WindowMain.setWindowIcon(icon)
        WindowMain.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(WindowMain)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setMargin(9)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hloAll = QtGui.QHBoxLayout()
        self.hloAll.setObjectName(_fromUtf8("hloAll"))
        self.vloControls = QtGui.QVBoxLayout()
        self.vloControls.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.vloControls.setObjectName(_fromUtf8("vloControls"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelDrivers = QtGui.QLabel(self.centralwidget)
        self.labelDrivers.setMaximumSize(QtCore.QSize(57, 16777215))
        self.labelDrivers.setObjectName(_fromUtf8("labelDrivers"))
        self.horizontalLayout_3.addWidget(self.labelDrivers)
        self.labelSignals = QtGui.QLabel(self.centralwidget)
        self.labelSignals.setMaximumSize(QtCore.QSize(137, 16777215))
        self.labelSignals.setObjectName(_fromUtf8("labelSignals"))
        self.horizontalLayout_3.addWidget(self.labelSignals)
        self.vloControls.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cbDrivers = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDrivers.sizePolicy().hasHeightForWidth())
        self.cbDrivers.setSizePolicy(sizePolicy)
        self.cbDrivers.setMaximumSize(QtCore.QSize(57, 16777215))
        self.cbDrivers.setObjectName(_fromUtf8("cbDrivers"))
        self.horizontalLayout_2.addWidget(self.cbDrivers)
        self.cbSignals = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbSignals.sizePolicy().hasHeightForWidth())
        self.cbSignals.setSizePolicy(sizePolicy)
        self.cbSignals.setMaximumSize(QtCore.QSize(137, 16777215))
        self.cbSignals.setObjectName(_fromUtf8("cbSignals"))
        self.horizontalLayout_2.addWidget(self.cbSignals)
        self.vloControls.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setMaximumSize(QtCore.QSize(200, 16777215))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.vloControls.addWidget(self.line)
        self.hloAxes = QtGui.QHBoxLayout()
        self.hloAxes.setObjectName(_fromUtf8("hloAxes"))
        self.labelAxis = QtGui.QLabel(self.centralwidget)
        self.labelAxis.setObjectName(_fromUtf8("labelAxis"))
        self.hloAxes.addWidget(self.labelAxis)
        self.rbAxis1 = QtGui.QRadioButton(self.centralwidget)
        self.rbAxis1.setObjectName(_fromUtf8("rbAxis1"))
        self.hloAxes.addWidget(self.rbAxis1)
        self.rbAxis2 = QtGui.QRadioButton(self.centralwidget)
        self.rbAxis2.setObjectName(_fromUtf8("rbAxis2"))
        self.hloAxes.addWidget(self.rbAxis2)
        self.rbAxis3 = QtGui.QRadioButton(self.centralwidget)
        self.rbAxis3.setObjectName(_fromUtf8("rbAxis3"))
        self.hloAxes.addWidget(self.rbAxis3)
        self.vloControls.addLayout(self.hloAxes)
        self.btnAdd = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.vloControls.addWidget(self.btnAdd)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelRemove = QtGui.QLabel(self.centralwidget)
        self.labelRemove.setMaximumSize(QtCore.QSize(60, 16777215))
        self.labelRemove.setObjectName(_fromUtf8("labelRemove"))
        self.horizontalLayout.addWidget(self.labelRemove)
        self.btnRemoveSel = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRemoveSel.sizePolicy().hasHeightForWidth())
        self.btnRemoveSel.setSizePolicy(sizePolicy)
        self.btnRemoveSel.setMaximumSize(QtCore.QSize(82, 16777215))
        self.btnRemoveSel.setObjectName(_fromUtf8("btnRemoveSel"))
        self.horizontalLayout.addWidget(self.btnRemoveSel)
        self.btnRemoveAll = QtGui.QPushButton(self.centralwidget)
        self.btnRemoveAll.setMaximumSize(QtCore.QSize(46, 16777215))
        self.btnRemoveAll.setObjectName(_fromUtf8("btnRemoveAll"))
        self.horizontalLayout.addWidget(self.btnRemoveAll)
        self.vloControls.addLayout(self.horizontalLayout)
        self.lvActiveSig = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lvActiveSig.sizePolicy().hasHeightForWidth())
        self.lvActiveSig.setSizePolicy(sizePolicy)
        self.lvActiveSig.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lvActiveSig.setObjectName(_fromUtf8("lvActiveSig"))
        self.vloControls.addWidget(self.lvActiveSig)
        self.btnShift = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnShift.sizePolicy().hasHeightForWidth())
        self.btnShift.setSizePolicy(sizePolicy)
        self.btnShift.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnShift.setObjectName(_fromUtf8("btnShift"))
        self.vloControls.addWidget(self.btnShift)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vloControls.addItem(spacerItem)
        self.btnImportSet = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnImportSet.sizePolicy().hasHeightForWidth())
        self.btnImportSet.setSizePolicy(sizePolicy)
        self.btnImportSet.setMaximumSize(QtCore.QSize(200, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnImportSet.setPalette(palette)
        self.btnImportSet.setObjectName(_fromUtf8("btnImportSet"))
        self.vloControls.addWidget(self.btnImportSet)
        self.btnExportSet = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExportSet.sizePolicy().hasHeightForWidth())
        self.btnExportSet.setSizePolicy(sizePolicy)
        self.btnExportSet.setMaximumSize(QtCore.QSize(200, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnExportSet.setPalette(palette)
        self.btnExportSet.setObjectName(_fromUtf8("btnExportSet"))
        self.vloControls.addWidget(self.btnExportSet)
        self.btnCLoop = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCLoop.sizePolicy().hasHeightForWidth())
        self.btnCLoop.setSizePolicy(sizePolicy)
        self.btnCLoop.setMaximumSize(QtCore.QSize(200, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnCLoop.setPalette(palette)
        self.btnCLoop.setObjectName(_fromUtf8("btnCLoop"))
        self.vloControls.addWidget(self.btnCLoop)
        self.btnCurrents = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCurrents.sizePolicy().hasHeightForWidth())
        self.btnCurrents.setSizePolicy(sizePolicy)
        self.btnCurrents.setMaximumSize(QtCore.QSize(200, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnCurrents.setPalette(palette)
        self.btnCurrents.setObjectName(_fromUtf8("btnCurrents"))
        self.vloControls.addWidget(self.btnCurrents)
        self.btnTarget = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTarget.sizePolicy().hasHeightForWidth())
        self.btnTarget.setSizePolicy(sizePolicy)
        self.btnTarget.setMaximumSize(QtCore.QSize(200, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnTarget.setPalette(palette)
        self.btnTarget.setObjectName(_fromUtf8("btnTarget"))
        self.vloControls.addWidget(self.btnTarget)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.vloControls.addWidget(self.line_2)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.btnESYNC = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnESYNC.sizePolicy().hasHeightForWidth())
        self.btnESYNC.setSizePolicy(sizePolicy)
        self.btnESYNC.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnESYNC.setObjectName(_fromUtf8("btnESYNC"))
        self.horizontalLayout_7.addWidget(self.btnESYNC)
        self.btnVSTATUS = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVSTATUS.sizePolicy().hasHeightForWidth())
        self.btnVSTATUS.setSizePolicy(sizePolicy)
        self.btnVSTATUS.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnVSTATUS.setObjectName(_fromUtf8("btnVSTATUS"))
        self.horizontalLayout_7.addWidget(self.btnVSTATUS)
        self.vloControls.addWidget(self.widget)
        self.hloAll.addLayout(self.vloControls)
        self.vloCurves = QtGui.QVBoxLayout()
        self.vloCurves.setObjectName(_fromUtf8("vloCurves"))
        self.hloCurveButtons = QtGui.QHBoxLayout()
        self.hloCurveButtons.setObjectName(_fromUtf8("hloCurveButtons"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hloCurveButtons.addItem(spacerItem1)
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.hloCurveButtons.addWidget(self.btnClear)
        self.btnSeeAll = QtGui.QPushButton(self.centralwidget)
        self.btnSeeAll.setObjectName(_fromUtf8("btnSeeAll"))
        self.hloCurveButtons.addWidget(self.btnSeeAll)
        self.btnPause = QtGui.QPushButton(self.centralwidget)
        self.btnPause.setObjectName(_fromUtf8("btnPause"))
        self.hloCurveButtons.addWidget(self.btnPause)
        self.btnResetY = QtGui.QPushButton(self.centralwidget)
        self.btnResetY.setObjectName(_fromUtf8("btnResetY"))
        self.hloCurveButtons.addWidget(self.btnResetY)
        self.btnResetX = QtGui.QPushButton(self.centralwidget)
        self.btnResetX.setObjectName(_fromUtf8("btnResetX"))
        self.hloCurveButtons.addWidget(self.btnResetX)
        self.btnNow = QtGui.QPushButton(self.centralwidget)
        self.btnNow.setObjectName(_fromUtf8("btnNow"))
        self.hloCurveButtons.addWidget(self.btnNow)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hloCurveButtons.addItem(spacerItem2)
        self.vloCurves.addLayout(self.hloCurveButtons)
        self.hloAll.addLayout(self.vloCurves)
        self.verticalLayout.addLayout(self.hloAll)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.hlo_enc2mot = QtGui.QHBoxLayout()
        self.hlo_enc2mot.setSpacing(13)
        self.hlo_enc2mot.setObjectName(_fromUtf8("hlo_enc2mot"))
        self.chkEctsTurn = QtGui.QCheckBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkEctsTurn.sizePolicy().hasHeightForWidth())
        self.chkEctsTurn.setSizePolicy(sizePolicy)
        self.chkEctsTurn.setObjectName(_fromUtf8("chkEctsTurn"))
        self.hlo_enc2mot.addWidget(self.chkEctsTurn)
        self.cb_enc_sel = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_enc_sel.sizePolicy().hasHeightForWidth())
        self.cb_enc_sel.setSizePolicy(sizePolicy)
        self.cb_enc_sel.setMinimumSize(QtCore.QSize(70, 32))
        self.cb_enc_sel.setMaximumSize(QtCore.QSize(150, 32))
        self.cb_enc_sel.setObjectName(_fromUtf8("cb_enc_sel"))
        self.cb_enc_sel.addItem(_fromUtf8(""))
        self.cb_enc_sel.addItem(_fromUtf8(""))
        self.hlo_enc2mot.addWidget(self.cb_enc_sel)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 16))
        self.label.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.hlo_enc2mot.addWidget(self.label)
        self.txtEctsTurn = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtEctsTurn.sizePolicy().hasHeightForWidth())
        self.txtEctsTurn.setSizePolicy(sizePolicy)
        self.txtEctsTurn.setReadOnly(True)
        self.txtEctsTurn.setObjectName(_fromUtf8("txtEctsTurn"))
        self.hlo_enc2mot.addWidget(self.txtEctsTurn)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlo_enc2mot.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.hlo_enc2mot)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(100, 16))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(100, 16))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.txtEctsTurn_4 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtEctsTurn_4.sizePolicy().hasHeightForWidth())
        self.txtEctsTurn_4.setSizePolicy(sizePolicy)
        self.txtEctsTurn_4.setReadOnly(True)
        self.txtEctsTurn_4.setObjectName(_fromUtf8("txtEctsTurn_4"))
        self.horizontalLayout_6.addWidget(self.txtEctsTurn_4)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(10, 16))
        self.label_6.setMaximumSize(QtCore.QSize(20, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.txtEctsTurn_5 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtEctsTurn_5.sizePolicy().hasHeightForWidth())
        self.txtEctsTurn_5.setSizePolicy(sizePolicy)
        self.txtEctsTurn_5.setReadOnly(True)
        self.txtEctsTurn_5.setObjectName(_fromUtf8("txtEctsTurn_5"))
        self.horizontalLayout_6.addWidget(self.txtEctsTurn_5)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 16))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.txtEctsTurn_2 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtEctsTurn_2.sizePolicy().hasHeightForWidth())
        self.txtEctsTurn_2.setSizePolicy(sizePolicy)
        self.txtEctsTurn_2.setReadOnly(True)
        self.txtEctsTurn_2.setObjectName(_fromUtf8("txtEctsTurn_2"))
        self.horizontalLayout_5.addWidget(self.txtEctsTurn_2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(10, 16))
        self.label_4.setMaximumSize(QtCore.QSize(20, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.txtEctsTurn_3 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtEctsTurn_3.sizePolicy().hasHeightForWidth())
        self.txtEctsTurn_3.setSizePolicy(sizePolicy)
        self.txtEctsTurn_3.setReadOnly(True)
        self.txtEctsTurn_3.setObjectName(_fromUtf8("txtEctsTurn_3"))
        self.horizontalLayout_5.addWidget(self.txtEctsTurn_3)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        WindowMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(WindowMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSignal_Sets = QtGui.QMenu(self.menubar)
        self.menuSignal_Sets.setObjectName(_fromUtf8("menuSignal_Sets"))
        WindowMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(WindowMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        WindowMain.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(WindowMain)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSettings = QtGui.QAction(WindowMain)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionClosed_Loop = QtGui.QAction(WindowMain)
        self.actionClosed_Loop.setObjectName(_fromUtf8("actionClosed_Loop"))
        self.actionCurrents = QtGui.QAction(WindowMain)
        self.actionCurrents.setObjectName(_fromUtf8("actionCurrents"))
        self.actionTarget = QtGui.QAction(WindowMain)
        self.actionTarget.setObjectName(_fromUtf8("actionTarget"))
        self.actionAdd_Signals = QtGui.QAction(WindowMain)
        self.actionAdd_Signals.setObjectName(_fromUtf8("actionAdd_Signals"))
        self.actionImport_Set = QtGui.QAction(WindowMain)
        self.actionImport_Set.setObjectName(_fromUtf8("actionImport_Set"))
        self.actionExport_Set = QtGui.QAction(WindowMain)
        self.actionExport_Set.setObjectName(_fromUtf8("actionExport_Set"))
        self.actionSave_to_File = QtGui.QAction(WindowMain)
        self.actionSave_to_File.setObjectName(_fromUtf8("actionSave_to_File"))
        self.menuFile.addAction(self.actionAdd_Signals)
        self.menuFile.addAction(self.actionSave_to_File)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuSignal_Sets.addAction(self.actionClosed_Loop)
        self.menuSignal_Sets.addAction(self.actionCurrents)
        self.menuSignal_Sets.addAction(self.actionTarget)
        self.menuSignal_Sets.addAction(self.actionImport_Set)
        self.menuSignal_Sets.addAction(self.actionExport_Set)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSignal_Sets.menuAction())

        self.retranslateUi(WindowMain)
        QtCore.QMetaObject.connectSlotsByName(WindowMain)

    def retranslateUi(self, WindowMain):
        WindowMain.setWindowTitle(_translate("WindowMain", "Dummy Window Title", None))
        self.labelDrivers.setText(_translate("WindowMain", "Driver:", None))
        self.labelSignals.setText(_translate("WindowMain", "Signal:", None))
        self.labelAxis.setText(_translate("WindowMain", "Y-axis:", None))
        self.rbAxis1.setText(_translate("WindowMain", "1", None))
        self.rbAxis2.setText(_translate("WindowMain", "2", None))
        self.rbAxis3.setText(_translate("WindowMain", "3", None))
        self.btnAdd.setText(_translate("WindowMain", "Add Signal", None))
        self.labelRemove.setText(_translate("WindowMain", "Remove:", None))
        self.btnRemoveSel.setText(_translate("WindowMain", "Selected", None))
        self.btnRemoveAll.setText(_translate("WindowMain", "All", None))
        self.btnShift.setText(_translate("WindowMain", "Shift Y-axis", None))
        self.btnImportSet.setText(_translate("WindowMain", "* Import Set *", None))
        self.btnExportSet.setText(_translate("WindowMain", "* Export Set *", None))
        self.btnCLoop.setText(_translate("WindowMain", "* Closed Loop *", None))
        self.btnCurrents.setText(_translate("WindowMain", "* Currents *", None))
        self.btnTarget.setText(_translate("WindowMain", "* Target *", None))
        self.btnESYNC.setText(_translate("WindowMain", "ESYNC", None))
        self.btnVSTATUS.setText(_translate("WindowMain", "VSTATUS", None))
        self.btnClear.setText(_translate("WindowMain", "Clear", None))
        self.btnSeeAll.setText(_translate("WindowMain", "All Data", None))
        self.btnSeeAll.setShortcut(_translate("WindowMain", "Ctrl+S", None))
        self.btnPause.setText(_translate("WindowMain", "Pause", None))
        self.btnResetY.setText(_translate("WindowMain", "Reset Y", None))
        self.btnResetX.setText(_translate("WindowMain", "Reset X", None))
        self.btnNow.setText(_translate("WindowMain", "Now", None))
        self.chkEctsTurn.setText(_translate("WindowMain", "measure", None))
        self.cb_enc_sel.setItemText(0, _translate("WindowMain", "TGTENC", None))
        self.cb_enc_sel.setItemText(1, _translate("WindowMain", "SHFTENC", None))
        self.label.setText(_translate("WindowMain", "counts/axis steps ratio =", None))
        self.label_3.setText(_translate("WindowMain", "Trace Corrections:", None))
        self.label_5.setText(_translate("WindowMain", "trace POSxxx = raw POSxxx * ", None))
        self.txtEctsTurn_4.setText(_translate("WindowMain", "1", None))
        self.label_6.setText(_translate("WindowMain", " -", None))
        self.txtEctsTurn_5.setText(_translate("WindowMain", "0", None))
        self.label_2.setText(_translate("WindowMain", "trace ENCxxx = raw ENCxxx * ", None))
        self.txtEctsTurn_2.setText(_translate("WindowMain", "1", None))
        self.label_4.setText(_translate("WindowMain", " -", None))
        self.txtEctsTurn_3.setText(_translate("WindowMain", "0", None))
        self.menuFile.setTitle(_translate("WindowMain", "File", None))
        self.menuSignal_Sets.setTitle(_translate("WindowMain", "Signal Sets", None))
        self.actionExit.setText(_translate("WindowMain", "Exit", None))
        self.actionExit.setShortcut(_translate("WindowMain", "Ctrl+X", None))
        self.actionSettings.setText(_translate("WindowMain", "Settings", None))
        self.actionClosed_Loop.setText(_translate("WindowMain", "Closed Loop", None))
        self.actionCurrents.setText(_translate("WindowMain", "Currents", None))
        self.actionTarget.setText(_translate("WindowMain", "Target", None))
        self.actionAdd_Signals.setText(_translate("WindowMain", "Add Signals", None))
        self.actionAdd_Signals.setShortcut(_translate("WindowMain", "Ctrl+A", None))
        self.actionImport_Set.setText(_translate("WindowMain", "Import Set", None))
        self.actionExport_Set.setText(_translate("WindowMain", "Export Set", None))
        self.actionSave_to_File.setText(_translate("WindowMain", "Save to File", None))

