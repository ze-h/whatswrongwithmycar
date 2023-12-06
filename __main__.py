from random import randint
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

def question_manager(window: lib.gui.ui_main.Ui_MainWindow, q: Question=qlist[0]):
    window.display_question(q)
    
def question_answer(window: lib.gui.ui_main.Ui_MainWindow, question: Question, answer: int):
    nq = get_question(question.answers[answer])
    if nq == None:
        return question_manager(window, qlist[randint(0, len(qlist))])
    return question_manager(window, nq)
    
def get_question(id):
    for q in qlist:
        if q.question_id == id:
            return q
    return None

if __name__ == "__main__":
    main()