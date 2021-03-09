from UserInputWindow import Ui_MainWindow
from Label import Label
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader
from datetime import date
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        sys.stdout = self
        self.pushButton.clicked.connect(self.OpenLabels)
        self.setWindowTitle("Sup")
        self.pH = 0
        self.cond = 0
        self.batchTitle = "Batch"
        self.deliveryZoneComboBox.addItems(["1-B-32", "2-G-12", "3-B-11", "3-J-11", "4th Floor Rt", "4th Floor Cold", "4th Floor H-Room", "5th Floor Rt", "5th Floor Cold", "5th Floor H-Room", "6th Floor RT", "6th Floor Cold", "6th Floor BST", "6th Floor H-Room", "SUL"])
        self.pHtemp = 27
        self.contemp = 25
        self.email = "email@email.com"
        self.lotnumber = "A20111111"
        self.date = date.today()
        self.expdate = date.today()

    def OpenLabels(self):
        self.batchTitle = self.batchTitleLineEdit.text()
        self.email = self.emailLineEdit.text()
        self.lotnumber = self.lotNumberLineEdit.text()
        
        label = Label(self.batchTitle,self.email, self.lotnumber,  self.deliveryZoneComboBox.currentText, self.expirationDateDateTimeEdit, self.pHLineEdit.text(), self.pHTemperatureLineEdit.text(), self.conductivityLabel.text(), self.conductivityTemperatureLineEdit.text() )
        label.showNormal()
        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
