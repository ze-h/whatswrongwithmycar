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


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("What's Wrong With My Car?")
        self.setFixedSize(400, 300)
        
        # Create a layout
        layout = QVBoxLayout()

        self.top_label = QLabel("Enter VIN:")
        self.top_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.top_label)

        # Create a label for the image
        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)

        # Create a text box
        self.text_box = QLineEdit(self)
        layout.addWidget(self.text_box)

        # Create a submit button
        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def submit(self):
        text = self.text_box.text()
        car = get_car(text)
        print(car)
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
