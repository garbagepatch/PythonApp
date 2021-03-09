from UserInputWindow import Ui_MainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtUiTools import QUiLoader
from LaelDialog import Ui_Dialog
class Label(QDialog, Ui_Dialog):
    def __init__(self, batch, email, lot, delivery, exp, pH, phtempval, con, contempval,   parent= None):
        super(Label, self).__init__(parent)
        self.setupUi(self)
        self.batch_title.text = batch
        self.emailLabel.text = email
        self.lotLabel.text =lot
        self.deliveryLabel.text = delivery
        self.expLabel = exp
        self.pHLabel.text =pH
        self.pHtemp.text = phtempval
        self.conLabel.text = con
        self.conTemp.text = contempval
        self.show()





