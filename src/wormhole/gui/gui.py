import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QListView, QTextEdit, QVBoxLayout, QHBoxLayout
from qt import Ui_main_gui

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_gui()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())