from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys


class PyQtLayout(QWidget):


    def __init__(self):
        super().__init__()
        self.main_layout = None
        self.InitializeUI()

    def InitializeUI(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle('Casino')
        self.displayGUI()

        self.show()

    def displayGUI(self):
        self.main_layout = QVBoxLayout()

        self.displayCasino()
        #self.displayUser()

        self.setLayout(self.main_layout)


    def displayCasino(self):
        counter = 0
        box = QHBoxLayout()
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

        grid.setRowStretch(3, 1)
        box.addLayout(grid)

        square = QFrame()
        square.setFixedSize(200, 200)
        square.setStyleSheet("background-color : grey")
        box.addWidget(square)

        self.main_layout.addLayout(box)


    #def displayUser(self):


app = QApplication(sys.argv)
win = PyQtLayout()
sys.exit(app.exec_())
