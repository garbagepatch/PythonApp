from UserInputWindow import Ui_MainWindow
from PySide2 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtPrintSupport import QPrintDialog, QPrinter
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QStylePainter
from PySide2.QtUiTools import QUiLoader
from LaelDialog import Ui_LabelWindow
import io
from datetime import date
import qrcode
from PIL import Image
from PySide2.QtWidgets import QWidget
class Label(QDialog, Ui_LabelWindow):
    def __init__(self, listInfo,   parent= None):
        self.listInfo = listInfo
        super(Label, self).__init__(parent)
        self.setupUi(self)
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.isFlam = self.isHHM = self.isTox = self.isHaz = self.isResp = self.isCorr = self.isEnv = False
        self.corr.clear()
        self.flam.clear()
        self.hhm.clear()
        self.tox.clear()
        self.resp.clear()
        self.non.clear()
        self.env.clear()
        self.haz.clear()
        self.corrImg = QImage("corrosive.png")
        self.corrPix = QPixmap(self.corrImg)
        self.flamImg = QImage("flammable.png")
        self.flamPix = QPixmap(self.flamImg)
        self.respImg = QImage("respiratory.png")
        self.respPix = QPixmap(self.respImg)
        self.envImg = QImage("environment.png")
        self.envPix = QPixmap(self.envImg)
        self.nonImg = QImage("Non haz.png")
        self.nonPix = QPixmap(self.nonImg)
        self.toxImg = QImage("toxic.png")
        self.toxPix = QPixmap(self.toxImg)
        self.hmmImg = QImage("hhm.png")
        self.hhmPix = QPixmap(self.hmmImg)
        self.hazImg = QImage("warning.png")
        self.hazPix = QPixmap(self.hazImg)
        self.dateLabel.setText(str(date.today()))
        self.batch_title.setText(listInfo[0])
        self.emailLabel.setText("Email: " + listInfo[1])
        self.lotLabel.setText("Lot: "+ listInfo[2])
        self.deliveryLabel.setText("Drop Zone: " + listInfo [3])
        self.expLabel.setText("Exp: "+listInfo[4])
        self.dialog = None
        self.pHLabel.setText("pH: " + listInfo[5]+" @ "+listInfo[6] + "C")
       
        self.conLabel.setText("Conductivity: " + listInfo[7]+"mS/cm @ " + listInfo[8]+ "C")
        self.printer = None
        self.buttonBox.accepted.connect(self.print_preview_dialog)
        img = self.createBarcode( listInfo[1], listInfo[0],listInfo[2])
        self.qrLabel.setPixmap(self.pil2pixmap(img))
        self.qrLabel.setScaledContents(True)
        self.checkShit(listInfo[0], listInfo[5])
    def createBarcode(self, batch, email, lot):
        codeStr = batch + "*" + email + "*" + lot
        img = qrcode.make(codeStr)
        return img
    def pil2pixmap(self, image):
        bytes_img = io.BytesIO()
        image.save(bytes_img, format='JPEG')

        qimg = QImage()
        qimg.loadFromData(bytes_img.getvalue())

        return QPixmap.fromImage(qimg)
    def print_preview_dialog(self):
     
        sshot = QWidget.grab(self.frame)
        sshot.save('sshot.png')
        if self.printer is None:
            self.printer = QPrinter(QPrinter.HighResolution)
        form = QPrintDialog(self.printer, self)
        if form.exec_():
            painter = QPainter()
            painter.begin(self.printer)
            painter.drawPixmap(0,0, sshot)
            painter.end()

    def checkShit(self, batch, pH):
        fpH = float(pH)
        corrosive_list = ['Phosphoric', 'Hydroxide', 'Acid', 'Formic', 'Sodium Sulfate', 'Ethylmaleidmide', 'Sodium Cyanoborohydride', 'NaOH' ]
        flam_list = ['Acetonitrile', 'Acetone', 'Methanol', 'Formic Acid', 'Sodium Dodecyl Sulfate', 'SDS', 'Ethanol', 'Sodium Cyanoborohydride', 'Sodium Perchlorate']
        tox_list = ['Methanol', 'Formic Acid', 'Ethylmaleidmide', 'Azide', 'Sodium Cyanoborohydride']
        env_list = ['Azide', 'Sodium Cyanoborohydride']
        haz_list = ['Benzyl Alcohol', 'EDTA', 'Ammonium Acetate', 'Ammonium Hydroxide', 'Acetone', 'DMSO', 'Guanidine', 'Methanol', 'Ammonium Formate', 'Ethylmaleidmide', 'Sodium Sulfate', 'Sodium Dodecyl Sulfate', 'Urea', 'Tris', 'Sodium Perchlorate']
        resp_list = ['Acetone']
        hhm_list = ['Azide', 'Sodium Cyanoborohydride', 'Sodium Perchlorate']
        if fpH <= 5.5 or fpH >= 10.5:
            self.isCorr = True
            img = QImage("corrosive.png")
            corrpix = QPixmap(img)
            self.corr.setPixmap(corrpix)

        if "Phosphoric" in batch:
            self.corr.setPixmap(self.corrPix)

        if "Acid" in batch:
            self.corr.setPixmap(self.corrPix)

      
  
        if any(ele in batch for ele in corrosive_list):
            self.isCorr = True
            self.corr.setPixmap(self.corrPix)

        elif any(ele in batch for ele in flam_list):
            self.isFlam = True
            self.flam.setPixmap(self.flamPix)
        elif any(ele in batch for ele in tox_list):
            self.isTox = True
            self.tox.setPixmap(self.toxPix)
        elif any(ele in batch for ele in resp_list):
            self.isResp = True
            self.resp.setPixmap(self.respPix)
        elif any(ele in batch for ele in env_list):
            self.isEnv = True
            self.env.setPixmap(self.envPix)
        elif any(ele in batch for ele in hhm_list):
            self.isHHM = True
            self.hhm.setPixmap(self.hhmPix)
        elif any(ele in batch for ele in haz_list):
            self.isHaz = True
            self.haz.setPixmap(self.hazPix)
        else:
            if self.isFlam is False  and self.isHHM is False  and self.isTox is False and self.isHaz is False and self.isResp is False and self.isCorr is False and self.isEnv is False:
                self.non.setPixmap(self.nonPix)
 
 
 
 




