# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserInputWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Resourcing_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1083, 595)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(179, 240, 227, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(90, 136, 131, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(89, 120, 113, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(119, 160, 151, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush6 = QBrush(QColor(217, 247, 241, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette1 = QPalette()
        brush11 = QBrush(QColor(222, 255, 237, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush11)
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1061, 538))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setSpacing(7)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.formLayout_2.setHorizontalSpacing(8)
        self.formLayout_2.setContentsMargins(22, 22, 19, 22)
        self.requestTypeLabel = QLabel(self.horizontalLayoutWidget)
        self.requestTypeLabel.setObjectName(u"requestTypeLabel")
        font = QFont()
        font.setFamily(u"MS PGothic")
        font.setPointSize(12)
        font.setUnderline(True)
        self.requestTypeLabel.setFont(font)
        self.requestTypeLabel.setFrameShape(QFrame.NoFrame)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.requestTypeLabel)

        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush2)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(225, 225, 225, 255))
        gradient.setColorAt(0.4, QColor(221, 221, 221, 255))
        gradient.setColorAt(0.5, QColor(216, 216, 216, 255))
        gradient.setColorAt(1, QColor(211, 211, 211, 255))
        brush13 = QBrush(gradient)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(0, 0, 0, 1)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(225, 225, 225, 255))
        gradient1.setColorAt(0.4, QColor(221, 221, 221, 255))
        gradient1.setColorAt(0.5, QColor(216, 216, 216, 255))
        gradient1.setColorAt(1, QColor(211, 211, 211, 255))
        brush14 = QBrush(gradient1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        gradient2 = QLinearGradient(0, 0, 0, 1)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(225, 225, 225, 255))
        gradient2.setColorAt(0.4, QColor(221, 221, 221, 255))
        gradient2.setColorAt(0.5, QColor(216, 216, 216, 255))
        gradient2.setColorAt(1, QColor(211, 211, 211, 255))
        brush15 = QBrush(gradient2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush16 = QBrush(QColor(0, 0, 0, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(0, 0, 0, 1)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(225, 225, 225, 255))
        gradient3.setColorAt(0.4, QColor(221, 221, 221, 255))
        gradient3.setColorAt(0.5, QColor(216, 216, 216, 255))
        gradient3.setColorAt(1, QColor(211, 211, 211, 255))
        brush17 = QBrush(gradient3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(0, 0, 0, 1)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(225, 225, 225, 255))
        gradient4.setColorAt(0.4, QColor(221, 221, 221, 255))
        gradient4.setColorAt(0.5, QColor(216, 216, 216, 255))
        gradient4.setColorAt(1, QColor(211, 211, 211, 255))
        brush18 = QBrush(gradient4)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        gradient5 = QLinearGradient(0, 0, 0, 1)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(225, 225, 225, 255))
        gradient5.setColorAt(0.4, QColor(221, 221, 221, 255))
        gradient5.setColorAt(0.5, QColor(216, 216, 216, 255))
        gradient5.setColorAt(1, QColor(211, 211, 211, 255))
        brush19 = QBrush(gradient5)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        brush20 = QBrush(QColor(0, 0, 0, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.comboBox.setPalette(palette2)
        font1 = QFont()
        font1.setPointSize(12)
        self.comboBox.setFont(font1)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"	color: black;\n"
"    border: 1px solid ;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-or"
                        "igin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox)

        self.line = QFrame(self.horizontalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.line)

        self.batchTitleLabel = QLabel(self.horizontalLayoutWidget)
        self.batchTitleLabel.setObjectName(u"batchTitleLabel")
        font2 = QFont()
        font2.setFamily(u"MS PGothic")
        font2.setPointSize(12)
        self.batchTitleLabel.setFont(font2)
        self.batchTitleLabel.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.batchTitleLabel)

        self.batchTitleLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.batchTitleLineEdit.setObjectName(u"batchTitleLineEdit")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush21 = QBrush(QColor(247, 255, 224, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush21)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush21)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush21)
        brush22 = QBrush(QColor(169, 169, 169, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Highlight, brush22)
        brush23 = QBrush(QColor(0, 0, 0, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush23)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush21)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush21)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush21)
        palette3.setBrush(QPalette.Inactive, QPalette.Highlight, brush22)
        brush24 = QBrush(QColor(0, 0, 0, 128))
        brush24.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush21)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush21)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush21)
        palette3.setBrush(QPalette.Disabled, QPalette.Highlight, brush22)
        brush25 = QBrush(QColor(0, 0, 0, 128))
        brush25.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush25)
#endif
        self.batchTitleLineEdit.setPalette(palette3)
        self.batchTitleLineEdit.setFont(font1)
        self.batchTitleLineEdit.setStyleSheet(u"QLineEdit {\n"
"color:  black;\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background:rgb(247, 255, 224);\n"
"    selection-background-color: darkgray;\n"
"}")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.batchTitleLineEdit)

        self.verticalSpacer_9 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout_2.setItem(4, QFormLayout.LabelRole, self.verticalSpacer_9)

        self.emailLabel = QLabel(self.horizontalLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setFont(font2)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setFont(font1)
        self.emailLineEdit.setStyleSheet(u"QLineEdit {\n"
"color:  black;\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background:rgb(247, 255, 224);\n"
"    selection-background-color: darkgray;\n"
"}")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.emailLineEdit)

        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout_2.setItem(6, QFormLayout.LabelRole, self.verticalSpacer_8)

        self.lotNumberLabel = QLabel(self.horizontalLayoutWidget)
        self.lotNumberLabel.setObjectName(u"lotNumberLabel")
        self.lotNumberLabel.setFont(font2)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.lotNumberLabel)

        self.lotNumberLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lotNumberLineEdit.setObjectName(u"lotNumberLineEdit")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush21)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush21)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush21)
        palette4.setBrush(QPalette.Active, QPalette.Highlight, brush22)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush21)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush21)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush21)
        palette4.setBrush(QPalette.Inactive, QPalette.Highlight, brush22)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush21)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush21)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush21)
        palette4.setBrush(QPalette.Disabled, QPalette.Highlight, brush22)
        self.lotNumberLineEdit.setPalette(palette4)
        self.lotNumberLineEdit.setFont(font1)
        self.lotNumberLineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background:rgb(247, 255, 224);\n"
"    selection-background-color: darkgray;\n"
"}")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.lotNumberLineEdit)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout_2.setItem(8, QFormLayout.LabelRole, self.verticalSpacer_7)

        self.deliveryZoneLabel = QLabel(self.horizontalLayoutWidget)
        self.deliveryZoneLabel.setObjectName(u"deliveryZoneLabel")
        self.deliveryZoneLabel.setFont(font2)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.deliveryZoneLabel)

        self.deliveryZoneComboBox = QComboBox(self.horizontalLayoutWidget)
        self.deliveryZoneComboBox.setObjectName(u"deliveryZoneComboBox")
        self.deliveryZoneComboBox.setFont(font1)
        self.deliveryZoneComboBox.setStyleSheet(u"QComboBox {\n"
"	color:  black;\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontr"
                        "ol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.deliveryZoneComboBox)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout_2.setItem(10, QFormLayout.LabelRole, self.verticalSpacer_6)

        self.pHLabel = QLabel(self.horizontalLayoutWidget)
        self.pHLabel.setObjectName(u"pHLabel")
        self.pHLabel.setFont(font2)

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.pHLabel)

        self.pHLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.pHLineEdit.setObjectName(u"pHLineEdit")
        self.pHLineEdit.setFont(font1)
        self.pHLineEdit.setStyleSheet(u"QLineEdit {\n"
"color:  black;\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background:rgb(247, 255, 224);\n"
"    selection-background-color: darkgray;\n"
"}")

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.pHLineEdit)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout_2.setItem(12, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.pHTemperatureLabel = QLabel(self.horizontalLayoutWidget)
        self.pHTemperatureLabel.setObjectName(u"pHTemperatureLabel")
        self.pHTemperatureLabel.setFont(font2)

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.pHTemperatureLabel)

        self.pHTemperatureLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.pHTemperatureLineEdit.setObjectName(u"pHTemperatureLineEdit")
        self.pHTemperatureLineEdit.setFont(font1)
        self.pHTemperatureLineEdit.setStyleSheet(u"QLineEdit {\n"
"color:  black;\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background:rgb(247, 255, 224);\n"
"    selection-background-color: darkgray;\n"
"}")

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.pHTemperatureLineEdit)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.formLayout_2.setItem(14, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.conductivityLabel = QLabel(self.horizontalLayoutWidget)
        self.conductivityLabel.setObjectName(u"conductivityLabel")
        self.conductivityLabel.setFont(font2)

        self.formLayout_2.setWidget(15, QFormLayout.LabelRole, self.conductivityLabel)

        self.conductivityLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.conductivityLineEdit.setObjectName(u"conductivityLineEdit")
        self.conductivityLineEdit.setFont(font1)
        self.conductivityLineEdit.setStyleSheet(u"QLineEdit {\n"
"color:  black;\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background:rgb(247, 255, 224);\n"
"    selection-background-color: darkgray;\n"
"}")

        self.formLayout_2.setWidget(15, QFormLayout.FieldRole, self.conductivityLineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout_2.setItem(16, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.conductivityTemperatureLabel = QLabel(self.horizontalLayoutWidget)
        self.conductivityTemperatureLabel.setObjectName(u"conductivityTemperatureLabel")
        self.conductivityTemperatureLabel.setFont(font2)

        self.formLayout_2.setWidget(17, QFormLayout.LabelRole, self.conductivityTemperatureLabel)

        self.conductivityTemperatureLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.conductivityTemperatureLineEdit.setObjectName(u"conductivityTemperatureLineEdit")
        self.conductivityTemperatureLineEdit.setFont(font1)
        self.conductivityTemperatureLineEdit.setStyleSheet(u"QLineEdit {\n"
"color:  black;\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background:rgb(247, 255, 224);\n"
"    selection-background-color: darkgray;\n"
"}")

        self.formLayout_2.setWidget(17, QFormLayout.FieldRole, self.conductivityTemperatureLineEdit)

        self.verticalSpacer = QSpacerItem(5, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout_2.setItem(18, QFormLayout.LabelRole, self.verticalSpacer)

        self.expirationDateLabel = QLabel(self.horizontalLayoutWidget)
        self.expirationDateLabel.setObjectName(u"expirationDateLabel")
        self.expirationDateLabel.setFont(font2)

        self.formLayout_2.setWidget(19, QFormLayout.LabelRole, self.expirationDateLabel)

        self.expirationDateDateTimeEdit = QDateTimeEdit(self.horizontalLayoutWidget)
        self.expirationDateDateTimeEdit.setObjectName(u"expirationDateDateTimeEdit")
        self.expirationDateDateTimeEdit.setDateTime(QDateTime(QDate(2021, 3, 16), QTime(0, 0, 0)))
        self.expirationDateDateTimeEdit.setCalendarPopup(True)
        self.expirationDateDateTimeEdit.setCurrentSectionIndex(0)

        self.formLayout_2.setWidget(19, QFormLayout.FieldRole, self.expirationDateDateTimeEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout_2.setItem(20, QFormLayout.LabelRole, self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(206)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(22, 21, 30, 19)
        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1083, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.requestTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Request Type", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Buffers", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Media", None))

        self.batchTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Batch Title", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lotNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Lot Number", None))
        self.deliveryZoneLabel.setText(QCoreApplication.translate("MainWindow", u"Delivery Zone", None))
        self.pHLabel.setText(QCoreApplication.translate("MainWindow", u"pH", None))
        self.pHTemperatureLabel.setText(QCoreApplication.translate("MainWindow", u"pH temperature", None))
        self.conductivityLabel.setText(QCoreApplication.translate("MainWindow", u"Conductivity", None))
        self.conductivityTemperatureLabel.setText(QCoreApplication.translate("MainWindow", u"Conductivity Temperature ", None))
        self.expirationDateLabel.setText(QCoreApplication.translate("MainWindow", u"Expiration Date", None))
        self.expirationDateDateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy ", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add the reagents here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Make Label", None))
    # retranslateUi

