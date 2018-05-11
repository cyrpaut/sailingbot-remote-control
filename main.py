#!/usr/bin/python3

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_SailBotMainWindow

class actuatorData:
    def __init__(self):
        self.tillerPos = 0
        self.mainLine = 0

class MWindow(Ui_SailBotMainWindow):
    def __init__(self, qtwidgetadress, _actData):

        self.actData = _actData

        # Set-up user interface layout (made with qtdesigner)
        self.setupUi(qtwidgetadress)

        self.tillerZeroBtn.clicked.connect(self.tillerZeroBtnClicked)
        self.tillerLeftBtn.clicked.connect(self.tillerLeftBtnClicked)
        self.tillerRightBtn.clicked.connect(self.tillerRightBtnClicked)

        self.mainSailDnBtn.clicked.connect(self.mainSailDnBtnClicked)
        self.mainSailUpBtn.clicked.connect(self.mainSailUpBtnClicked)

        self.connectBtn.clicked.connect(self.connectBtnClicked)
        self.disconnectBtn.clicked.connect(self.disconnectBtnClicked)
        self.startLogBtn.clicked.connect(self.startLogBtnClicked)
        self.stopLogBtn.clicked.connect(self.stopLogBtnClicked)

        self.holdDirectionTickBox.clicked.connect(self.holdDirectionTickBoxClicked)
        self.holdSailTickBox.clicked.connect(self.holdSailTickBoxClicked)

        qtwidgetadress.show()

    def tillerZeroBtnClicked(self):
        '''Catch tiller Zero Btn event'''
        self.actData.tillerPos = 0
        print("Tiller Rezero")

    def tillerLeftBtnClicked(self):
        '''Catch tiller Left Btn event'''
        if (self.actData.tillerPos > -25):
            self.actData.tillerPos -= 1
        print("Tiller: " + str(self.actData.tillerPos))

    def tillerRightBtnClicked(self):
        '''Catch tiller Right Btn event'''
        if (self.actData.tillerPos < 25):
            self.actData.tillerPos += 1
        print("Tiller: " + str(self.actData.tillerPos))

    def mainSailDnBtnClicked(self):
        '''Catch main line down btn event'''
        if (self.actData.mainLine > 0):
            self.actData.mainLine -=1
        print("Line: " + str(self.actData.mainLine))

    def mainSailUpBtnClicked(self):
        '''Catch main line up btn event'''
        if (self.actData.mainLine < 20):
            self.actData.mainLine +=1
        print("Line: " + str(self.actData.mainLine))

    def connectBtnClicked(self):
        '''Catch Connect btn event'''
        pass

    def disconnectBtnClicked(self):
        '''Catch Disconnect btn event'''
        pass

    def startLogBtnClicked(self):
        '''Catch start log btn event'''
        pass

    def stopLogBtnClicked(self):
        '''Catch stop log btn event'''
        pass

    def holdDirectionTickBoxClicked(self):
        '''Catch Hold direction tickbox event'''
        pass

    def holdSailTickBoxClicked(self):
        '''Catch hold main line sail tickbox event'''
        pass

if __name__ == "__main__":

    actData = actuatorData()

    # Create window
    app = QtWidgets.QApplication(sys.argv)
    SailBotMainWindow = QtWidgets.QMainWindow()

    # Initialize layout and event catchers
    ui = MWindow(SailBotMainWindow, actData)

    #Exit control
    sys.exit(app.exec_())