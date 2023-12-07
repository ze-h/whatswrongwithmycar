# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainrzsUCR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.11
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import __main__
from lib.fetch import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from lib.question import Question


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("What's Wrong With My Car?")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        MainWindow.setSizePolicy(sizePolicy)
        self.setFixedSize(800, 600)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 10, 781, 17))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(10, 30, 361, 531))
        self.label_2.setPixmap(QPixmap(":/images/images/secret.jpg"))
        self.label_2.setScaledContents(False)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(380, 30, 411, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rb_choice1 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice1.setObjectName("rb_choice1")

        self.verticalLayout.addWidget(self.rb_choice1)

        self.rb_choice2 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice2.setObjectName("rb_choice2")

        self.verticalLayout.addWidget(self.rb_choice2)

        self.rb_choice3 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice3.setObjectName("rb_choice3")

        self.verticalLayout.addWidget(self.rb_choice3)

        self.rb_choice4 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice4.setObjectName("rb_choice4")

        self.verticalLayout.addWidget(self.rb_choice4)

        self.rb_choice5 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice5.setObjectName("rb_choice5")

        self.verticalLayout.addWidget(self.rb_choice5)

        self.rb_choice6 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice6.setObjectName("rb_choice6")

        self.verticalLayout.addWidget(self.rb_choice6)

        self.rb_choice7 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice7.setObjectName("rb_choice7")

        self.verticalLayout.addWidget(self.rb_choice7)

        self.rb_choice8 = QRadioButton(self.verticalLayoutWidget)
        self.rb_choice8.setObjectName("rb_choice8")

        self.verticalLayout.addWidget(self.rb_choice8)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.carimage = None

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)

        self.vin_dialog = QInputDialog(MainWindow)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("What's Wrong With My Car?")
        self.msg.setText("Please enter a valid VIN number.")

        self.abt_msg = QMessageBox()
        self.abt_msg.setWindowTitle("What's Wrong With My Car?")
        self.abt_msg.setText(
            "<html><head/><body><p>Created by Ziad El-Hefnawy, Nicole Schmitt, Dawson Gomez, and Illia Biblyi.</p><p>Copyright 2023.</p><p>Created with PyQT5</p></body></html>"
        )

        self.final_msg = QMessageBox()
        self.final_msg.setWindowTitle("What's Wrong With My Car?")
        self.abt_msg.setText("meek_mill.jpg")

        self.retranslateUi(MainWindow)
        self.currentQuestion = None

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", "About", None)
        )
        self.label.setText("")
        self.label_2.setText("")
        self.rb_choice1.setText(
            QCoreApplication.translate("MainWindow", "Choice1", None)
        )
        self.rb_choice2.setText(
            QCoreApplication.translate("MainWindow", "Choice2", None)
        )
        self.rb_choice3.setText(
            QCoreApplication.translate("MainWindow", "Choice3", None)
        )
        self.rb_choice4.setText(
            QCoreApplication.translate("MainWindow", "Choice4", None)
        )
        self.rb_choice5.setText(
            QCoreApplication.translate("MainWindow", "Choice5", None)
        )
        self.rb_choice6.setText(
            QCoreApplication.translate("MainWindow", "Choice6", None)
        )
        self.rb_choice7.setText(
            QCoreApplication.translate("MainWindow", "Choice7", None)
        )
        self.rb_choice8.setText(
            QCoreApplication.translate("MainWindow", "Choice8", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "Submit", None)
        )
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi

    def submit_answer(self) -> None:
        send = lambda x: __main__.question_answer(self, self.currentQuestion, x)

        if self.rb_choice1.isChecked():
            return send(0)
        if self.rb_choice2.isChecked():
            return send(1)
        if self.rb_choice3.isChecked():
            return send(2)
        if self.rb_choice4.isChecked():
            return send(3)
        if self.rb_choice5.isChecked():
            return send(4)
        if self.rb_choice6.isChecked():
            return send(5)
        if self.rb_choice7.isChecked():
            return send(6)
        if self.rb_choice8.isChecked():
            return send(7)

    def show(self) -> None:
        filename = ""
        text = self.vin_dialog.getText(
            self, "What's Wrong With My Car?", "Input VIN number"
        )[0]
        car = get_car(text).to_string()
        filename = download_file(get_image_url(get_wiki_page(car)))
        pmap = QPixmap(filename).scaled(361, 300, Qt.KeepAspectRatio)
        self.carimage = pmap
        self.label_2.setPixmap(pmap)
        print(text)
        print(car)
        print(filename)
        self.pushButton.clicked.connect(self.submit_answer)
        super().show()
        # return __main__.question_manager(self)
        return __main__.question_manager(self)

    def display_question(self, q: Question):
        self.currentQuestion = q

        self.label.setText(q.text)

        self.rb_choice1.setEnabled(q.answers[0] != "")
        self.rb_choice1.setText(q.answers[0])

        self.rb_choice2.setEnabled(q.answers[1] != "")
        self.rb_choice2.setText(q.answers[1])

        self.rb_choice3.setEnabled(q.answers[2] != "")
        self.rb_choice3.setText(q.answers[2])

        self.rb_choice4.setEnabled(q.answers[3] != "")
        self.rb_choice4.setText(q.answers[3])

        self.rb_choice5.setEnabled(q.answers[4] != "")
        self.rb_choice5.setText(q.answers[4])

        self.rb_choice6.setEnabled(q.answers[5] != "")
        self.rb_choice6.setText(q.answers[5])

        self.rb_choice7.setText(q.answers[6])
        self.rb_choice7.setEnabled(q.answers[5] != "")

        self.rb_choice8.setText(q.answers[7])
        self.rb_choice8.setEnabled(q.answers[7] != "")
        
        pmap = None
        if q.image != "":
            pmap = QPixmap(q.image).scaled(361, 300, Qt.KeepAspectRatio)
            print(q.image)
            self.label_2.setPixmap(pmap)
        else:
            self.label_2.setPixmap(self.carimage)

    def end(self) -> None:
        from lib.Problems import VehicleIssues

        # Print end of program statement
        V = VehicleIssues()
        string = "End of program. The top three vehicle issues with their probabilities are as follows:\n"

        # Sort the problems by their float values in descending order
        sorted_problems = sorted(
            V.problemlist.items(), key=lambda x: x[1], reverse=True
        )

        # Print the first three problems
        for problem, value in sorted_problems[:3]:
            string += f"{problem}: {100 * value}%\n"
        self.final_msg.setText(string)
        self.final_msg.show()
        return self.close()

    def actionAbout(self) -> None:
        return self.abt_msg.show()