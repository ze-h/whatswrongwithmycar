import lib.sample as sample
from lib.fetch import *
from PyQt5 import QtCore, QtGui, QtWidgets 
import sys 

class Ui_MainWindow(object): 

	def setupUi(self, MainWindow : QtWidgets.QMainWindow): 
		MainWindow.resize(600, 150)
		MainWindow.setFixedSize(600, 150)
		self.centralwidget = QtWidgets.QWidget(MainWindow) 
		
		# adding pushbutton 
		self.pushButton = QtWidgets.QPushButton(self.centralwidget) 
		self.pushButton.setGeometry(QtCore.QRect(200, 75, 200, 28)) 

		# adding signal and slot 
		self.pushButton.clicked.connect(self.changelabeltext) 
	
		self.label = QtWidgets.QLabel(self.centralwidget) 
		self.label.setGeometry(QtCore.QRect(100, 75, 400, 20))

		# keeping the text of label empty before button get clicked 
		self.label.setText("")	 
		
		MainWindow.setCentralWidget(self.centralwidget) 
		self.retranslateUi(MainWindow) 
		QtCore.QMetaObject.connectSlotsByName(MainWindow) 

	def retranslateUi(self, MainWindow): 
		_translate = QtCore.QCoreApplication.translate 
		MainWindow.setWindowTitle(_translate("MainWindow", "QT5 Test")) 
		self.pushButton.setText(_translate("MainWindow", "Click for more information...")) 
		
	def changelabeltext(self):

		# changing the text of label after button get clicked 
		self.label.setText("According to NHTSA: a 2013 BMW X3 has a {} cylinder engine.".format(sample.x3()))

		# Hiding pushbutton from the main window 
		# after button get clicked. 
		self.pushButton.hide()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv) 
	MainWindow = QtWidgets.QMainWindow() 
	ui = Ui_MainWindow() 
	ui.setupUi(MainWindow) 
	MainWindow.show()
	sys.exit(app.exec_()) 