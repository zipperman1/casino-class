from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

class PyQtLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.InitializeUI()

    def InitializeUI(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle('Casino')
        self.displayButtons()
        self.displayRoulette()

        self.show()

    def displayButtons(self):
        counter = 0
        self.box = QHBoxLayout()
        grid = QGridLayout()
        grid.setSpacing(0)
        
        button_list = list()
        for i in range(1, 37):
            button_list.append(QPushButton(str(i), self))
            button_list[i - 1].setFixedSize(40, 40)
            if i % 2 == 0:
                button_list[i - 1].setStyleSheet("background-color : red")
            else:
                button_list[i - 1].setStyleSheet("background-color : grey")

        for i in range(0, 3):
            for j in range(0, 12):
                grid.addWidget(button_list[counter], i, j)
                counter += 1
        self.box.addLayout(grid)
        self.setLayout(self.box)

    def displayRoulette(self):
        square = QFrame()
        square.setFixedSize(200, 200)
        square.setStyleSheet("background-color : grey")
        self.box.addWidget(square)
    

app = QApplication(sys.argv)
win = PyQtLayout()
sys.exit(app.exec_())
