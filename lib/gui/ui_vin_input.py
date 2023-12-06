# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vin_inputAuPFhG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.11
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from fileinput import filename
from lib.fetch import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#import __main__
import lib.gui.ui_main as ui_main

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.Reset)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 100, 341, 23))
        self.lineEdit.setMaximumSize(QSize(341, 23))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 161, 17))
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        rst = self.buttonBox.button(QDialogButtonBox.Reset)
        # rst.clicked.connect(self.reset())

        self.msg = QMessageBox()
        self.msg.setWindowTitle("What's Wrong With My Car?")
        self.msg.setText("Please enter a valid VIN number.")

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"VIN Number", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Enter Your VIN Number:", None))
    # retranslateUi
    
    def reset(self):
        self.lineEdit.setText("")
        
    def accept(self) -> None:
        #action if submit is clicked
        text = self.lineEdit.text()
        if text == "":
            self.msg.exec()
        else:
            car = get_car(text).to_string()
            if car != "None None None":
                #get the picture
                filename = download_file(get_image_url(get_wiki_page(car)))
                super().accept()
                return filename
            else:
                self.msg.exec()
                


