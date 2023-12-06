import sys
import lib.gui.ui_main
from PyQt5.QtWidgets import QApplication
from lib.question import Question
import csv

qlist = list()
with open('questions.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        try:
            qn = Question(row[0], row[1], row[18], row[2:10], row[10:18])
            qlist.append(qn)
        except(IndexError):
            print("A non-fatal IndexError has occured")
            pass

def main():
    #qlist.sort(key= lambda x : x.question_id)
    app = QApplication(sys.argv)
    window = lib.gui.ui_main.Ui_MainWindow()
    window.setupUi(window)
    window.show()
    app.exec()

def question_manager(window: lib.gui.ui_main.Ui_MainWindow):
    window.display_question(qlist[1])

if __name__ == "__main__":
    main()