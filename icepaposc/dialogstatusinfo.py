from PyQt4 import QtGui
from ui.ui_dialogstatusinfo import Ui_DialogStatusInfo
#from lib_icepapcms import IcepapController
from pyIcePAP import EthIcePAPController
from PyQt4 import QtCore, Qt
import re


class DialogStatusInfo(QtGui.QDialog):

    def __init__(self, parent, icepapsys, addr):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_DialogStatusInfo()
        #self.driver = IcepapController().iPaps[drv.icepapsystem_name]
        self.icepapsys=icepapsys
        self.driver = icepapsys[addr]
        self.icepapAddress = icepapsys[addr].addr
        self.ui.setupUi(self)
        #self.setWindowTitle('Status Info  |  ' + drv.icepapsystem_name + '  |  ' + str(self.icepapAddress) + ' ' + drv.name)
        self.setWindowTitle('Status Info  |  ' + self.driver._ctrl._host + '  |  ' + str(self.icepapAddress) + ' ' + self.driver.name)
        self.show()
        self.connectSignals()
        self.doVstatus()
        self.allDriversCommands = ['?cfg extdisable', '?ver info', '?power',
                                   '?positions', '?warning', '?alarm', '?isg ?ssierrtoggles',
                                   '#isg ssiwarningrst', 'm ?ver info', 'm ?rdispol', '?vstatus DISABLE', '?vstatus STOPCODE'
                                   ]
        for cmd in self.allDriversCommands:
            self.ui.cbAllDrivers.addItem(cmd)
        
        self.version_keys = [
            'CONTROLLER',
            'DSP',
            'FPGA',
            'MCPU1',
            'MCPU0',
            'MCPU2',
            'DRIVER']
        self.version_reg_exp = re.compile(
            "(%s)\s*:\s*(\d+\.\d+)" %
            "|".join(self.version_keys),
            re.VERBOSE)

    def connectSignals(self):
        self.ui.btnUpdate.clicked.connect(self.doVstatus)
        #self.ui.btnEsync.clicked.connect(self.doEsync)
        self.ui.btnUpdate.setDefault(False)
        #self.ui.btnEsync.setDefault(False)
        self.ui.btnUpdate.setAutoDefault(False)
        #self.ui.btnEsync.setAutoDefault(False)
        self.ui.txt1Command.returnPressed.connect(self.sendCommand)
        #self.ui.txt1Command.returnPressed.connect(lambda: self.sendCommand())
        #self.ui.txt1Command.returnPressed()
        QtCore.QObject.connect(self.ui.txt1Command,QtCore.SIGNAL("editingFinished()"),self.sendCommand)
        self.ui.cbAllDrivers.activated.connect(self.sendCommandToDrivers)
        #QtCore.QObject.connect(self.ui.txt1Command,QtCore.SIGNAL("returnPressed()"),self.sendCommand)
        #self.ui.btnCommand.clicked.connect(self.sendCommand)



    def doVstatus(self):
        val = ""
        try:
            #val = self.driver.getVStatus(self.icepapAddress)
            val = self.driver.vstatus
        except Exception, e:
            print(e)
        self.ui.textBrowser.setText(val)

    #def doEsync(self):
    #    try:
    #        self.driver.syncEncoders(self.icepapAddress)
    #    except Exception, e:
    #        print(e)

    def sendCommand(self):
        val = ""
        comm = ""
        try:

            #val = self.ui.txt1Command.text()
            comm = "" + str(self.ui.txt1Command.text())
            print comm
            #val = self.driver.getVStatus(self.icepapAddress)
            val = self.driver.vstatus
            #val = self.driver.sendWriteReadCommand(comm)
            val = self.driver.send_cmd(comm)
            #val = IcepapController().iPaps[self.icepap_driver.icepapsystem_name].
            val = ' '.join(val)
            val= comm.upper() + " " + val
            print val
        except Exception, e:
            print(e)
        self.ui.textBrowser.setText(comm + "\n" + val)

    def sendCommandToDrivers(self):
        sel = '%s'%self.ui.cbAllDrivers.currentText()
        sel_split = sel.split(' ' )
        txt = ''
        if sel == '?positions':
            header = 'dr name axis absenc encin inpos tgtenc'
            txt = header + '\n'
            #for driver in self.driver.getDriversAlive():
            for driver in self.icepapsys.find_axes(only_alive=True):
                try:
                    val0 = self.icepapsys[driver].name
                    val1 = self.icepapsys[driver].pos
                    val2 = self.icepapsys[driver].enc_absenc
                    val3 = self.icepapsys[driver].enc_encin
                    val4 = self.icepapsys[driver].enc_inpos
                    val5 = self.icepapsys[driver].get_cfg('TGTENC')
                    val5 = val5['TGTENC']
                    if val0 == '': val0 = 'noname'
                    txt = txt + '%s '%driver + '%s '%val0 + '%s '%val1 + '%s '%val2 + '%s '%val3 + '%s '%val4 + '%s '%val5 + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
        elif sel == '?ver info':
            #for driver in self.driver.getDriversAlive():
            for driver in self.icepapsys.find_axes(only_alive=True):
                try:
                    #val = self.icepapsys[driver].ver                    
                    val = self.getVersionInfoDict(driver)
                    txt = txt + '%s '%driver + str(val) + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        elif sel == 'm ?ver info':
            for contr in self.getRacksAlive():
                try:
                    val = self.getVersionInfoDict(contr)
                    txt = txt + '%s '%contr + str(val) + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        elif sel.startswith('?vstatus') and len(sel_split) == 2:
            #for driver in self.driver.getDriversAlive():
            for driver in self.icepapsys.find_axes(only_alive=True):
                try:
                    comm = ('%s:%s')%(driver, '?vstatus')
                    #val = self.driver.sendWriteReadCommand(comm)
                    val_lines = self.icepapsys.send_cmd(comm)
                    #val_lines = val.split('\n')
                    for l in val_lines:
                        if sel_split[1] in l:
                            txt = txt + '%s '%driver + l + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        elif sel.startswith('m '):
            print 'master'
            contr_comm = sel.replace('m ', '')
            for contr in self.getRacksAlive():
                try:
                    comm = ('%s:%s')%(contr, contr_comm)
                    #val = self.driver.sendWriteReadCommand(comm)
                    val = self.icepapsys.send_cmd(comm)
                    val = ' '.join(val)
                    val= comm.upper() + " " + val
                    txt = txt + '%s '%contr + str(val) + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        else:
            for driver in self.icepapsys.find_axes(only_alive=True):
                try:
                    comm = ('%s:%s')%(driver, self.ui.cbAllDrivers.currentText())
                    val = self.icepapsys.send_cmd(comm)
                    val = ' '.join(val)
                    val= comm.upper() + " " + val
                    txt = txt + '%s '%driver + str(val) + '\n'
                    self.ui.textBrowser.setText(txt)
                except Exception, e:
                    print(e)
            self.ui.textBrowser.setText(txt)

    def getVersionInfoDict(self, addr):
        command = "%d:?VER INFO" % (addr)
        ans = self.icepapsys.send_cmd(command)
        info = self.version_reg_exp.findall(str(ans))
        return dict(info)

    def getRacksAlive(self):
        racks = []
        rackMask = 0
        try:
            rackMask = int(self.icepapsys.send_cmd('?sysstat')[0], 16)
        except BaseException:
            pass
        for rack in range(16):
            if (rackMask & (1 << rack)) != 0:
                racks.append(rack)
        return racks
