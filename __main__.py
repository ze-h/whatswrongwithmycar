import sys
import lib.gui.ui_main
from PyQt5.QtWidgets import QApplication
from lib.question import Question
from lib.question_list import qlist

def main():
    qlist.sort(key= lambda x : x.question_id)
    app = QApplication(sys.argv)
    window = lib.gui.ui_main.Ui_MainWindow()
    window.setupUi(window)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()