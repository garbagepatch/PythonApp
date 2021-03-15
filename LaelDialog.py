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

class Ui_LabelWindow(object):
    def setupUi(self, LabelWindow):
        if not LabelWindow.objectName():
            LabelWindow.setObjectName(u"LabelWindow")
        LabelWindow.resize(683, 748)
        self.buttonBox = QDialogButtonBox(LabelWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(360, 340, 311, 31))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.frame = QFrame(LabelWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 681, 331))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.frame.setPalette(palette)
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
        self.frame2 = QFrame(LabelWindow)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setGeometry(QRect(0, 440, 671, 301))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.frame2.setPalette(palette1)
        self.frame2.setAutoFillBackground(True)
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 671, 327))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lot2 = QLabel(self.verticalLayoutWidget)
        self.lot2.setObjectName(u"lot2")

        self.horizontalLayout_3.addWidget(self.lot2)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(28, 22))
        self.line.setBaseSize(QSize(23, 14))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.line.setPalette(palette2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.resuls = QLabel(self.verticalLayoutWidget)
        self.resuls.setObjectName(u"resuls")
        self.resuls.setMinimumSize(QSize(0, 250))
        self.resuls.setInputMethodHints(Qt.ImhMultiLine)
        self.resuls.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.resuls)


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
        self.lot2.setText(QCoreApplication.translate("LabelWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("LabelWindow", u"TextLabel", None))
        self.resuls.setText(QCoreApplication.translate("LabelWindow", u"TextLabel", None))
    # retranslateUi

