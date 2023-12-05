from lib.question import Question
import csv

qlist = list()

with open('questions.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        try:
            qn = Question(row[0], row[1], row[2], row[3:10], row[11:18], row[19:])
            qlist.append(qn)
        except(IndexError):
            pass