# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainrzsUCR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.11
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from lib.fetch import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import lib.gui.ui_vin_input as ui_vin_input

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        MainWindow.setSizePolicy(sizePolicy)
        self.setFixedSize(800, 600)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 781, 17))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 361, 531))
        self.label_2.setPixmap(QPixmap(u":/images/images/secret.jpg"))
        self.label_2.setScaledContents(False)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(380, 30, 411, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_7 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.verticalLayout.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.verticalLayout.addWidget(self.radioButton_8)

        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.radioButton_6 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.verticalLayout.addWidget(self.radioButton_6)

        self.radioButton_5 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout.addWidget(self.radioButton_5)

        self.radioButton_4 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout.addWidget(self.radioButton_4)

        self.radioButton = QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)

        self.vin_dialog = QInputDialog(MainWindow)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("What's Wrong With My Car?")
        self.msg.setText("Please enter a valid VIN number.")
        
        self.abt_msg = QMessageBox()
        self.abt_msg.setWindowTitle("What's Wrong With My Car?")
        self.abt_msg.setText(u"<html><head/><body><p>Created by Ziad El-Hefnawy, Nicole Schmitt, Dawson Gomez, and Illia Biblyi.</p><p>Copyright 2023.</p><p>Created with PyQT5</p></body></html>")

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label.setText("")
        self.label_2.setText("")
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Choice1", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Choice2", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Choice3", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Choice4", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Choice5", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Choice6", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Choice7", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Choice8", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

    def show(self) -> None:
        filename = ""
        text = self.vin_dialog.getText(self, "What's Wrong With My Car?", "Input VIN number")[0]
        car = get_car(text)
        filename = download_file(get_image_url(get_wiki_page(car)))
        pmap = QPixmap(filename).scaled(361, 300, Qt.KeepAspectRatio)
        self.label_2.setPixmap(pmap)
        print(text)
        print(car)
        print(filename)
        return super().show()
    
    def actionAbout(self) -> None:
        return self.abt_msg.show()
