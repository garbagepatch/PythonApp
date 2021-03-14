# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'label.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Resourcing_rc
import Resourcing_rc

class Ui_LabelWindow(object):
    def setupUi(self, LabelWindow):
        if not LabelWindow.objectName():
            LabelWindow.setObjectName(u"LabelWindow")
        LabelWindow.resize(699, 388)
        self.buttonBox = QDialogButtonBox(LabelWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(360, 340, 311, 31))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.frame = QFrame(LabelWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 651, 331))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 651, 331))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 1, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 100))
        self.label.setPixmap(QPixmap(u":/newPrefix/ULS.jpg"))

        self.verticalLayout_2.addWidget(self.label)

        self.batch_title = QLabel(self.horizontalLayoutWidget)
        self.batch_title.setObjectName(u"batch_title")
        self.batch_title.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setPointSize(12)
        self.batch_title.setFont(font)

        self.verticalLayout_2.addWidget(self.batch_title)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridGroupBox_2 = QGroupBox(self.horizontalLayoutWidget)
        self.gridGroupBox_2.setObjectName(u"gridGroupBox_2")
        self.gridLayout_2 = QGridLayout(self.gridGroupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.conLabel = QLabel(self.gridGroupBox_2)
        self.conLabel.setObjectName(u"conLabel")
        self.conLabel.setScaledContents(True)

        self.gridLayout_2.addWidget(self.conLabel, 3, 1, 1, 1)

        self.pHLabel = QLabel(self.gridGroupBox_2)
        self.pHLabel.setObjectName(u"pHLabel")
        self.pHLabel.setScaledContents(True)

        self.gridLayout_2.addWidget(self.pHLabel, 2, 1, 1, 1)

        self.deliveryLabel = QLabel(self.gridGroupBox_2)
        self.deliveryLabel.setObjectName(u"deliveryLabel")
        self.deliveryLabel.setScaledContents(True)

        self.gridLayout_2.addWidget(self.deliveryLabel, 5, 1, 1, 1)

        self.lotLabel = QLabel(self.gridGroupBox_2)
        self.lotLabel.setObjectName(u"lotLabel")
        self.lotLabel.setScaledContents(True)

        self.gridLayout_2.addWidget(self.lotLabel, 6, 1, 1, 1)

        self.dateLabel = QLabel(self.gridGroupBox_2)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setScaledContents(True)

        self.gridLayout_2.addWidget(self.dateLabel, 4, 1, 1, 1)

        self.expLabel = QLabel(self.gridGroupBox_2)
        self.expLabel.setObjectName(u"expLabel")
        self.expLabel.setInputMethodHints(Qt.ImhDate)

        self.gridLayout_2.addWidget(self.expLabel, 4, 2, 1, 1)

        self.emailLabel = QLabel(self.gridGroupBox_2)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setScaledContents(True)

        self.gridLayout_2.addWidget(self.emailLabel, 5, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.gridGroupBox_2)

        self.qrLabel = QLabel(self.horizontalLayoutWidget)
        self.qrLabel.setObjectName(u"qrLabel")
        self.qrLabel.setMinimumSize(QSize(100, 100))
        self.qrLabel.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_2.addWidget(self.qrLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.env = QLabel(self.horizontalLayoutWidget)
        self.env.setObjectName(u"env")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.env.sizePolicy().hasHeightForWidth())
        self.env.setSizePolicy(sizePolicy)
        self.env.setPixmap(QPixmap(u":/newPrefix/environment.png"))

        self.gridLayout.addWidget(self.env, 2, 0, 1, 1)

        self.resp = QLabel(self.horizontalLayoutWidget)
        self.resp.setObjectName(u"resp")
        sizePolicy.setHeightForWidth(self.resp.sizePolicy().hasHeightForWidth())
        self.resp.setSizePolicy(sizePolicy)
        self.resp.setPixmap(QPixmap(u":/newPrefix/respiratory.png"))

        self.gridLayout.addWidget(self.resp, 0, 1, 1, 1)

        self.haz = QLabel(self.horizontalLayoutWidget)
        self.haz.setObjectName(u"haz")
        sizePolicy.setHeightForWidth(self.haz.sizePolicy().hasHeightForWidth())
        self.haz.setSizePolicy(sizePolicy)
        self.haz.setPixmap(QPixmap(u":/newPrefix/warning.png"))

        self.gridLayout.addWidget(self.haz, 1, 1, 1, 1)

        self.non = QLabel(self.horizontalLayoutWidget)
        self.non.setObjectName(u"non")
        sizePolicy.setHeightForWidth(self.non.sizePolicy().hasHeightForWidth())
        self.non.setSizePolicy(sizePolicy)
        self.non.setPixmap(QPixmap(u":/newPrefix/Non haz.png"))

        self.gridLayout.addWidget(self.non, 3, 0, 1, 1)

        self.hhm = QLabel(self.horizontalLayoutWidget)
        self.hhm.setObjectName(u"hhm")
        sizePolicy.setHeightForWidth(self.hhm.sizePolicy().hasHeightForWidth())
        self.hhm.setSizePolicy(sizePolicy)
        self.hhm.setPixmap(QPixmap(u":/newPrefix/HHM.png"))

        self.gridLayout.addWidget(self.hhm, 3, 1, 1, 1)

        self.flam = QLabel(self.horizontalLayoutWidget)
        self.flam.setObjectName(u"flam")
        sizePolicy.setHeightForWidth(self.flam.sizePolicy().hasHeightForWidth())
        self.flam.setSizePolicy(sizePolicy)
        self.flam.setPixmap(QPixmap(u":/newPrefix/flammable.png"))

        self.gridLayout.addWidget(self.flam, 2, 1, 1, 1)

        self.tox = QLabel(self.horizontalLayoutWidget)
        self.tox.setObjectName(u"tox")
        sizePolicy.setHeightForWidth(self.tox.sizePolicy().hasHeightForWidth())
        self.tox.setSizePolicy(sizePolicy)
        self.tox.setPixmap(QPixmap(u":/newPrefix/toxic.png"))

        self.gridLayout.addWidget(self.tox, 1, 0, 1, 1)

        self.corr = QLabel(self.horizontalLayoutWidget)
        self.corr.setObjectName(u"corr")
        sizePolicy.setHeightForWidth(self.corr.sizePolicy().hasHeightForWidth())
        self.corr.setSizePolicy(sizePolicy)
        self.corr.setPixmap(QPixmap(u":/newPrefix/corrosive.png"))

        self.gridLayout.addWidget(self.corr, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(LabelWindow)
        self.buttonBox.rejected.connect(LabelWindow.reject)

        QMetaObject.connectSlotsByName(LabelWindow)
    # setupUi

    def retranslateUi(self, LabelWindow):
        LabelWindow.setWindowTitle(QCoreApplication.translate("LabelWindow", u"Dialog", None))
        self.label.setText("")
        self.batch_title.setText("")
        self.gridGroupBox_2.setTitle("")
        self.conLabel.setText(QCoreApplication.translate("LabelWindow", u"TextLabel", None))
        self.pHLabel.setText(QCoreApplication.translate("LabelWindow", u"TextLabel", None))
        self.deliveryLabel.setText(QCoreApplication.translate("LabelWindow", u"TextLabel", None))
        self.lotLabel.setText(QCoreApplication.translate("LabelWindow", u"TextLabel", None))
        self.dateLabel.setText(QCoreApplication.translate("LabelWindow", u"TextLabel", None))
        self.expLabel.setText("")
        self.emailLabel.setText(QCoreApplication.translate("LabelWindow", u"TextLabel", None))
        self.qrLabel.setText(QCoreApplication.translate("LabelWindow", u"TextLabel", None))
        self.env.setText("")
        self.resp.setText("")
        self.haz.setText("")
        self.non.setText("")
        self.hhm.setText("")
        self.flam.setText("")
        self.tox.setText("")
        self.corr.setText("")
    # retranslateUi

