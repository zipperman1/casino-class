from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QBrush, QImage, QFont
import sys


class PyQtLayout(QWidget):
    credit = 100000

    def __init__(self):
        super().__init__()
        self.InitializeUI()

    def InitializeUI(self):
        window_size = QSize(1100, 600)
        palette = QPalette()

        self.setFixedSize(window_size)
        self.setWindowTitle('Casino')
        palette.setBrush(QPalette.Window, QBrush(QImage('background.jpg').scaled(window_size)))
        self.setPalette(palette)
        self.displayGUI()

        self.show()

    def displayGUI(self):

        self.displayCasino()
        self.displayUser()

    def displayCasino(self):
        counter = 0
        button_size = 40

        button_list = list()
        for i in range(1, 37):
            button_list.append(QPushButton(str(i), self))
            button_list[i - 1].setFixedSize(button_size, button_size)
            if i % 2 == 0:
                button_list[i - 1].setStyleSheet("background-color : red")
            else:
                button_list[i - 1].setStyleSheet("background-color: #333333; color: white;")

        for i in range(0, 3):
            for j in range(0, 12):
                button_list[counter].move(button_size * 2 + button_size * j, button_size + button_size * i)
                counter += 1
        button_list.append(QPushButton('0', self))
        button_list[36].setFixedSize(button_size, button_size)
        button_list[36].setStyleSheet("background-color : green")
        button_list[36].move(button_size, button_size)

        button_list.append(QPushButton('00', self))
        button_list[37].move(button_size, button_size*3)
        button_list[37].setFixedSize(button_size, button_size)
        button_list[37].setStyleSheet("background-color : green")

        placeholder = QFrame()
        placeholder.setFixedSize(200, 200)
        placeholder.setStyleSheet("background-color : violet")


    def displayUser(self):
        credit_counter = QLabel(str(self.credit), self)
        credit_counter.move(40, 400)
        credit_counter.setStyleSheet("color: white")
        credit_counter.setFont(QFont('Arial', 20))


app = QApplication(sys.argv)
win = PyQtLayout()
sys.exit(app.exec_())
