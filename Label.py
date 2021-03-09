from UserInputWindow import Ui_MainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtUiTools import QUiLoader
from LaelDialog import Ui_Dialog
class Label(QDialog, Ui_Dialog):
    def __init__(self, listInfo,   parent= None):
        self.listInfo = listInfo
        super(Label, self).__init__(parent)
        self.setupUi(self)
        self.batch_title.text = listInfo[0]
        self.emailLabel.text = listInfo[1]
        self.lotLabel.text =listInfo[2]
        self.deliveryLabel.text = listInfo [3]
        self.expLabel = listInfo[4]

        self.pHLabel.text = listInfo [5]
        self.pHtemp.text = listInfo[6]
        self.conLabel.text = listInfo[7]
        self.conTemp.text = listInfo[8]
        self.show()





