from UserInputWindow import Ui_MainWindow
from Label import Label
from PySide2 import QtWidgets

from PySide2.QtGui import QIcon, QImage, QPixmap
from PySide2.QtWidgets import  QMainWindow, QAction
from EditStuff import EditStuff
from datetime import date
import sys

class HappyLabels(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(HappyLabels, self).__init__()
        self.setupUi(self)
        sys.stdout = self
        self.pushButton.clicked.connect(self.OpenLabels)
        self.comboBox.currentTextChanged.connect(self.SetLabels)
        self.setWindowTitle("Sup")
        self.pH = 0
        self.isMedia = False
        self.cond = 0
        self.batchTitle = "Batch"
        self.deliveryZoneComboBox.addItems(["1-B-32", "2-G-12", "3-B-11", "3-J-11", "4th Floor Rt", "4th Floor Cold", "4th Floor H-Room", "5th Floor Rt", "5th Floor Cold", "5th Floor H-Room", "6th Floor RT", "6th Floor Cold", "6th Floor BST", "6th Floor H-Room", "SUL"])
        self.pHtemp = 27
        self.contemp = 25
        self.email = "email@email.com"
        self.lotnumber = "A20111111"
        self.date = date.today()
        self.expdate = date.today()
        self.listInfo = []
        self.label = None
        self.createMenu()

    def createMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        viewMenu = mainMenu.addMenu('View')
        editMenu = mainMenu.addMenu('Edit')
        fontMenu = mainMenu.addMenu('Font')
        helpMenu = mainMenu.addMenu('Help')
 
 
        openAction = QAction(QIcon('open.png'), "Open", self)
        openAction.setShortcut('Ctrl+O')
 
 
        saveAction = QAction(QIcon('save.png'), "Save", self)
        saveAction.setShortcut('Ctrl+S')
 
        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut('Ctrl+X')
        editAction = QAction(QIcon('save.png'), "edit", self)
        editAction.setShortcut('Ctrl+R')
 
 
 
        exitAction.triggered.connect(self.exit_app)
 

 

        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        editAction.triggered.connect(self.editStuff)
        fileMenu.addAction(exitAction)
        editMenu.addAction(editAction)
 
    def exit_app(self):
        self.close()
    def editStuff(self):
        editStuff = EditStuff()
        editStuff.show()
    def SetLabels(self):
        if(self.comboBox.currentText() == "Media"):
            self.conductivityLabel.setText("pCO2")
            self.conductivityTemperatureLabel.setText("Osmolality")
            self.isMedia = True
            
        if(self.comboBox.currentText() == "Buffers"):
            self.conductivityLabel.setText("Conductivity")
            self.conductivityTemperatureLabel.setText("Conductivity Temp")
            self.isMedia = False
    def OpenLabels(self):
        try: 
            self.listInfo = [self.batchTitleLineEdit.text(),self.emailLineEdit.text(), self.lotNumberLineEdit.text(),  self.deliveryZoneComboBox.currentText(), self.expirationDateDateTimeEdit.date().toString("yyyy-MM-dd"), self.pHLineEdit.text(), self.pHTemperatureLineEdit.text(), self.conductivityLineEdit.text(), self.conductivityTemperatureLineEdit.text() ]    
            self.label = Label(self.listInfo, self.textEdit.toPlainText(), self.isMedia )
            self.label.show()
            
        except Exception as e: 
            print(e)
        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    app.setStyle('Fusion')
    main = HappyLabels()
    main.show()
    sys.exit(app.exec_())
