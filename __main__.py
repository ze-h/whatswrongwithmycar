import sys
import lib.gui.ui_main
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = lib.gui.ui_main.Ui_MainWindow()
    window.setupUi(window)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
