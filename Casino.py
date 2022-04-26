import random
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QImage, QFont, QIntValidator
from PyQt5.QtWidgets import *


class PyQtLayout(QMainWindow):

    def __init__(self):
        self.credit = 10000
        self.random_value = 0

        super().__init__()
        self.red_buttons = list()
        self.black_buttons = list()
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
        self.displayUser()
        self.displayCasino()

    def displayCasino(self):
        counter = 1
        button_size = 40

        self.button_list = list()
        range_buttons = list()

        self.button_list.append(QPushButton('0', self))  # 0 button
        self.button_list[0].setFixedSize(button_size, 3 * button_size)
        self.button_list[0].setStyleSheet("background-color : green")
        self.button_list[0].move(button_size, button_size)
        self.button_list[0].clicked.connect(self.rouletteStart)

        for i in range(0, 12):
            for j in range(0, 3):
                self.button_list.append(QPushButton(str(counter), self))
                self.button_list[counter].move(button_size * 2 + button_size * i, button_size + button_size * j)
                self.button_list[counter].setFixedSize(button_size, button_size)
                self.button_list[counter].clicked.connect(self.rouletteStart)

                counter += 1

        self.rouletteColor(1, 10, 1)
        self.rouletteColor(11, 18, 0)
        self.rouletteColor(19, 28, 1)
        self.rouletteColor(29, 36, 0)

        self.rbutton_names = list(['1 to 18', 'Even', 'Red', 'Black', 'Odd', '19 to 36'])

        for i in range(0, 6):
            range_buttons.append(QPushButton(self.rbutton_names[i], self))
            range_buttons[i].setFixedSize(button_size * 2, button_size)
            range_buttons[i].move(button_size * 2 + button_size * i * 2, button_size * 4)
            range_buttons[i].setStyleSheet("background-color: transparent; border: 2px solid")
            range_buttons[i].clicked.connect(self.rouletteStart)

    def displayUser(self):
        self.credit_counter = QLabel('Credits: ' + str(self.credit) + '\nBet:', self)
        self.credit_counter.setFixedSize(1000, 65)
        self.credit_counter.move(40, 400)
        self.credit_counter.setStyleSheet("color: white")
        self.credit_counter.setFont(QFont('Arial', 20))

        self.bet_input = QLineEdit(self)
        self.bet_input.setValidator(QIntValidator())
        self.bet_input.resize(100, 22)
        self.bet_input.move(130, 440)

        self.roulette_number = QLabel(str(self.random_value), self)
        self.roulette_number.setFont(QFont('Arial', 50))
        self.roulette_number.move(700, 40)
        self.roulette_number.setFixedSize(200, 60)



    def rouletteColor(self, start, end, shift):
        for i in range(start, end + 1):
            if (i + shift) % 2 == 0:
                self.button_list[i].setStyleSheet("background-color : red")
                self.red_buttons.append(i)
            else:
                self.button_list[i].setStyleSheet("background-color: #333333; color: white;")
                self.black_buttons.append(i)

    def rouletteStart(self):
        button = self.sender()
        button_name = button.text()
        rbutton_func = list([set(range(1, 19)), set(range(2, 37, 2)), set(self.red_buttons), set(self.black_buttons),
                             set(range(1, 37, 2)), set(range(19, 37))])

        if button_name in self.rbutton_names:
            num = rbutton_func[self.rbutton_names.index(button_name)]
        else:
            num = set([int(button_name)])
        bet = self.bet_input.text()

        if not self.bet_input.text().isdigit() or int(bet) <= 0 or self.credit < int(bet):
            self.roulette_number.setText('Error')
            return

        self.random_value = random.randint(0, 36)

        bet = int(bet)
        if self.random_value in num:
            self.credit += bet
        else:
            self.credit -= bet

        self.credit_counter.setText('Credits: ' + str(self.credit) + '\nBet:')
        self.roulette_number.setText(str(self.random_value) + str())


app = QApplication(sys.argv)
win = PyQtLayout()
sys.exit(app.exec_())
