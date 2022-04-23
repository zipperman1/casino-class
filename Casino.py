import random
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPalette, QBrush, QImage, QFont, QIntValidator
from PyQt5.QtWidgets import *


class PyQtLayout(QWidget):

    def __init__(self):
        self.credit = 10000
        self.random_value = 0

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

        self.roulette_number = QLabel(str(self.random_value) + ' test', self)                  # temporary
        self.roulette_number.setFont(QFont('Arial', 20))
        self.roulette_number.move(600, 300)

        button_list[0].clicked.connect(lambda: self.rouletteStart(0, self.bet_input.text()))

    def displayUser(self):
        self.credit_counter = QLabel('Credits: ' + str(self.credit) + '\nBet:', self)
        self.credit_counter.move(40, 400)
        self.credit_counter.setStyleSheet("color: white")
        self.credit_counter.setFont(QFont('Arial', 20))

        self.bet_input = QLineEdit(self)
        self.bet_input.setValidator(QIntValidator())
        self.bet_input.resize(100, 22)
        self.bet_input.move(130, 440)

    def rouletteStart(self, num, bet):
        if not self.bet_input.text().isdigit():
            self.roulette_number.setText('Error')
            return

        bet = int(bet)
        self.random_value = random.randint(1, 38)
        self.roulette_number.setText(str(self.random_value) + str())

        if num == self.random_value:
            self.credit += bet
        else:
            self.credit -= bet

        self.credit_counter.setText('Credits: ' + str(self.credit) + '\nBet:')



app = QApplication(sys.argv)
win = PyQtLayout()
sys.exit(app.exec_())
