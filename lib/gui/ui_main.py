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
from lib.question import Question

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"What's Wrong With My Car?")
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
        self.rb_choice1 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice1.setObjectName(u"rb_choice1")

        self.verticalLayout.addWidget(self.rb_choice1)

        self.rb_choice2 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice2.setObjectName(u"rb_choice2")

        self.verticalLayout.addWidget(self.rb_choice2)

        self.rb_choice3 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice3.setObjectName(u"rb_choice3")

        self.verticalLayout.addWidget(self.rb_choice3)

        self.rb_choice4 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice4.setObjectName(u"rb_choice4")

        self.verticalLayout.addWidget(self.rb_choice4)

        self.rb_choice5 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice5.setObjectName(u"rb_choice5")

        self.verticalLayout.addWidget(self.rb_choice5)

        self.rb_choice6 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice6.setObjectName(u"rb_choice6")

        self.verticalLayout.addWidget(self.rb_choice6)

        self.rb_choice7 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice7.setObjectName(u"rb_choice7")

        self.verticalLayout.addWidget(self.rb_choice7)

        self.rb_choice8 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice8.setObjectName(u"rb_choice8")

        self.verticalLayout.addWidget(self.rb_choice8)

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
        self.rb_choice1.setText(QCoreApplication.translate("MainWindow", u"Choice1", None))
        self.rb_choice2.setText(QCoreApplication.translate("MainWindow", u"Choice2", None))
        self.rb_choice3.setText(QCoreApplication.translate("MainWindow", u"Choice3", None))
        self.rb_choice4.setText(QCoreApplication.translate("MainWindow", u"Choice4", None))
        self.rb_choice5.setText(QCoreApplication.translate("MainWindow", u"Choice5", None))
        self.rb_choice6.setText(QCoreApplication.translate("MainWindow", u"Choice6", None))
        self.rb_choice7.setText(QCoreApplication.translate("MainWindow", u"Choice7", None))
        self.rb_choice8.setText(QCoreApplication.translate("MainWindow", u"Choice8", None))
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
    
    def display_question(self, q: Question):
        self.label.setText(q.text)
        if q.answers[0] == "":
            self.rb_choice1.setEnabled(False)
        else:
            self.rb_choice1.setEnabled(True)
            self.rb_choice1.setText(q.answers[0])
            
        if q.answers[1] == "":
            self.rb_choice2.setEnabled(False)
        else:
            self.rb_choice2.setEnabled(True)
            self.rb_choice2.setText(q.answers[1])
            
        if q.answers[2] == "":
            self.rb_choice3.setEnabled(False)
        else:
            self.rb_choice3.setEnabled(True)
            self.rb_choice3.setText(q.answers[2])
            
        if q.answers[3] == "":
            self.rb_choice4.setEnabled(False)
        else:
            self.rb_choice4.setEnabled(True)
            self.rb_choice4.setText(q.answers[3])
            
        if q.answers[4] == "":
            self.rb_choice5.setEnabled(False)
        else:
            self.rb_choice5.setEnabled(True)
            self.rb_choice5.setText(q.answers[4])
            
        if q.answers[5] == "":
            self.rb_choice6.setEnabled(False)
        else:
            self.rb_choice6.setEnabled(True)
            self.rb_choice6.setText(q.answers[5])
            
        if q.answers[6] == "":
            self.rb_choice7.setEnabled(False)
        else:
            self.rb_choice7.setEnabled(True)
            self.rb_choice7.setText(q.answers[6])
            
        if q.answers[7] == "":
            self.rb_choice8.setEnabled(False)
        else:
            self.rb_choice8.setEnabled(True)
            self.rb_choice8.setText(q.answers[7])

    
    def actionAbout(self) -> None:
        return self.abt_msg.show()
