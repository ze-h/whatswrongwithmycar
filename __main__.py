import sys
from lib.fetch import *
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


#generate main window
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("What's Wrong With My Car?")
        self.setFixedSize(400, 300)
        
        #create a layout
        layout = QVBoxLayout()

        #create top label
        self.top_label = QLabel("Enter VIN:")
        self.top_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.top_label)

        #create a label that contains the image
        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)

        #create a text box
        self.text_box = QLineEdit(self)
        layout.addWidget(self.text_box)

        #create a submit button
        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def submit(self):
        #action if submit is clicked
        text = self.text_box.text()
        car = get_car(text)
        print(car)
        
        #get the picture
        filename = download_file(get_image_url(get_wiki_page(car)))
        pixmap = QPixmap(filename)
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.top_label.setText(car)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
