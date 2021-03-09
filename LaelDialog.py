# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(895, 466)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(350, 440, 311, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 10, 731, 401))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 661, 324))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/ULS.jpg"))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridGroupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.gridGroupBox_2.setObjectName("gridGroupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridGroupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 4, 1, 1)
        self.dateLabel = QtWidgets.QLabel(self.gridGroupBox_2)
        self.dateLabel.setObjectName("dateLabel")
        self.gridLayout_2.addWidget(self.dateLabel, 4, 2, 1, 1)
        self.deliveryLabel = QtWidgets.QLabel(self.gridGroupBox_2)
        self.deliveryLabel.setObjectName("deliveryLabel")
        self.gridLayout_2.addWidget(self.deliveryLabel, 5, 2, 1, 1)
        self.labvasdv = QtWidgets.QLabel(self.gridGroupBox_2)
        self.labvasdv.setObjectName("labvasdv")
        self.gridLayout_2.addWidget(self.labvasdv, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 1, 1, 1)
        self.Date = QtWidgets.QLabel(self.gridGroupBox_2)
        self.Date.setObjectName("Date")
        self.gridLayout_2.addWidget(self.Date, 4, 1, 1, 1)
        self.conLabel = QtWidgets.QLabel(self.gridGroupBox_2)
        self.conLabel.setObjectName("conLabel")
        self.gridLayout_2.addWidget(self.conLabel, 3, 2, 1, 1)
        self.expLabel = QtWidgets.QLabel(self.gridGroupBox_2)
        self.expLabel.setObjectName("expLabel")
        self.gridLayout_2.addWidget(self.expLabel, 4, 5, 1, 1)
        self.lotLabel = QtWidgets.QLabel(self.gridGroupBox_2)
        self.lotLabel.setObjectName("lotLabel")
        self.gridLayout_2.addWidget(self.lotLabel, 6, 2, 1, 1)
        self.edfasdf = QtWidgets.QLabel(self.gridGroupBox_2)
        self.edfasdf.setObjectName("edfasdf")
        self.gridLayout_2.addWidget(self.edfasdf, 6, 1, 1, 1)
        self.pHLabel = QtWidgets.QLabel(self.gridGroupBox_2)
        self.pHLabel.setObjectName("pHLabel")
        self.gridLayout_2.addWidget(self.pHLabel, 2, 2, 1, 1)
        self.conTemp = QtWidgets.QLabel(self.gridGroupBox_2)
        self.conTemp.setObjectName("conTemp")
        self.gridLayout_2.addWidget(self.conTemp, 3, 3, 1, 1)
        self.batch_title = QtWidgets.QLabel(self.gridGroupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.batch_title.setFont(font)
        self.batch_title.setObjectName("batch_title")
        self.gridLayout_2.addWidget(self.batch_title, 0, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 2, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 3, 4, 1, 1)
        self.pHtemp = QtWidgets.QLabel(self.gridGroupBox_2)
        self.pHtemp.setObjectName("pHtemp")
        self.gridLayout_2.addWidget(self.pHtemp, 2, 3, 1, 1)
        self.expLabel_2 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.expLabel_2.setObjectName("expLabel_2")
        self.gridLayout_2.addWidget(self.expLabel_2, 5, 3, 1, 1)
        self.emailLabel = QtWidgets.QLabel(self.gridGroupBox_2)
        self.emailLabel.setObjectName("emailLabel")
        self.gridLayout_2.addWidget(self.emailLabel, 5, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.gridGroupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/environment.png"))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/respiratory.png"))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/warning.png"))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/newPrefix/Non haz.png"))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/HHM.png"))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/flammable.png"))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/toxic.png"))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/corrosive.png"))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_11.setText(_translate("Dialog", "Conductivity"))
        self.label_17.setText(_translate("Dialog", "Exp"))
        self.dateLabel.setText(_translate("Dialog", "TextLabel"))
        self.deliveryLabel.setText(_translate("Dialog", "TextLabel"))
        self.labvasdv.setText(_translate("Dialog", "Delivery Room"))
        self.label_12.setText(_translate("Dialog", "pH"))
        self.Date.setText(_translate("Dialog", "Date"))
        self.conLabel.setText(_translate("Dialog", "TextLabel"))
        self.expLabel.setText(_translate("Dialog", "TextLabel"))
        self.lotLabel.setText(_translate("Dialog", "TextLabel"))
        self.edfasdf.setText(_translate("Dialog", "Lot Number"))
        self.pHLabel.setText(_translate("Dialog", "TextLabel"))
        self.conTemp.setText(_translate("Dialog", "TextLabel"))
        self.batch_title.setText(_translate("Dialog", "Batch_Title"))
        self.label_25.setText(_translate("Dialog", "C"))
        self.label_26.setText(_translate("Dialog", "C"))
        self.pHtemp.setText(_translate("Dialog", "TextLabel"))
        self.expLabel_2.setText(_translate("Dialog", "Email"))
        self.emailLabel.setText(_translate("Dialog", "TextLabel"))
import Resourcing_rc
