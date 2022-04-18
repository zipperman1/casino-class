from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys

class PyQtLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.InitializeUI()

    def InitializeUI(self):
        self.setGeometry(0,0, 800, 600)
        self.setWindowTitle('Casino')

        self.show()

app = QApplication(sys.argv)
win = PyQtLayout()
sys.exit(app.exec_())
