from functools import partial

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow, QGridLayout
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt

from Account import Account
from Text import Text


account = Account()
text = Text()


class StartPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        english_layout = QHBoxLayout()

        self.english_button = QPushButton('English')

        english_layout.addWidget(self.english_button)
        english_layout.addWidget(QLabel('Choose Language'))

        persian_layout = QHBoxLayout()

        self.persian_button = QPushButton('فارسی')

        persian_layout.addWidget(QLabel('زبان خود را انتخاب کنید'))
        persian_layout.addWidget(self.persian_button)

        language_layout = QHBoxLayout()
        language_layout.addLayout(english_layout)
        language_layout.addLayout(persian_layout)

        main_layout.addLayout(language_layout)

        self.setLayout(main_layout)

class PasswordPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        password_label = QLabel(self)
        password_label.setText(text('Please enter password:'))
        password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        password_label.setIndent(10)

        self.password_input = QLineEdit(self)
        self.password_input.setMaxLength(4)
        self.password_input.setValidator(QIntValidator())
        self.password_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.submit_button = QPushButton(text('Submit'))

        main_layout.addWidget(password_label)
        main_layout.addWidget(self.password_input)
        main_layout.addWidget(self.submit_button)

        self.setLayout(main_layout)

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        grid_layout = QGridLayout()

        self.buttons = [[QPushButton(text('Get Cash')), QPushButton(text('Change Password'))],
                   [QPushButton(text('Money Transfer')), QPushButton(text('Account Balance'))]]

        for i in range(2):
            for j in range(2):
                self.buttons[i][j].setFixedHeight(45)
                grid_layout.addWidget(self.buttons[i][j], i, j)

        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)

class CashPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        grid_layout = QGridLayout()

        self.buttons = [[QPushButton('500,000'), QPushButton('1,500,000')],
                        [QPushButton('1,000,000'), QPushButton('2,000,000')]]

        for i in range(2):
            for j in range(2):
                self.buttons[i][j].setFixedHeight(45)
                grid_layout.addWidget(self.buttons[i][j], i, j)

        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)

class BalancePage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton(text('Confirm'))

        main_layout.addWidget(QLabel(text('Your bank account balance:') + ' ' + str(account.get_balance())))
        main_layout.addWidget(self.button)

        self.setLayout(main_layout)

class ChangePasswordPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        password_label = QLabel(self)
        password_label.setText(text('Enter New Password:'))
        password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        password_label.setIndent(10)

        self.password_input = QLineEdit(self)
        self.password_input.setMaxLength(4)
        self.password_input.setValidator(QIntValidator())
        self.password_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.submit_button = QPushButton(text('Submit'))

        main_layout.addWidget(password_label)
        main_layout.addWidget(self.password_input)
        main_layout.addWidget(self.submit_button)

        self.setLayout(main_layout)

class GoodMissionPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(QLabel(text('Mission Accomplished Successfully!')))

        horizontal_layout = QHBoxLayout()

        self.new_mission_button = QPushButton(text('New Mission'))
        self.goodbye_button = QPushButton(text('Goodbye'))

        horizontal_layout.addWidget(self.new_mission_button)
        horizontal_layout.addWidget(self.goodbye_button)

        main_layout.addLayout(horizontal_layout)

        self.setLayout(main_layout)

class BadMissionPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(QLabel(text('Mission Failed!')))

        horizontal_layout = QHBoxLayout()

        self.new_mission_button = QPushButton(text('New Mission'))
        self.goodbye_button = QPushButton(text('Goodbye'))

        horizontal_layout.addWidget(self.new_mission_button)
        horizontal_layout.addWidget(self.goodbye_button)

        main_layout.addLayout(horizontal_layout)

        self.setLayout(main_layout)

class MoneyTransferPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(QLabel(text('Enter the desired amount:')))

        self.amount_input = QLineEdit(self)
        #self.amount_input.setValidator(QIntValidator())
        self.amount_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.amount_input)

        main_layout.addWidget(QLabel(text('Enter the destination card number:')))

        self.destination_card_number_input = QLineEdit(self)
        #self.destination_card_number_input.setValidator(QIntValidator())
        self.destination_card_number_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.destination_card_number_input)

        self.confirm_button = QPushButton(text('Confirm'))

        main_layout.addWidget(self.confirm_button)

        self.setLayout(main_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ATM App')
        self.setGeometry(130, 230, 500, 500)

        self.show_page('Start')

    def show_page(self, value: str):
        match value:
            case 'Start':
                start_page = StartPage()

                def english_button_clicked():
                    text.change_to_english()
                    self.show_page('Password')
                def persian_button_clicked():
                    text.change_to_persian()
                    self.show_page('Password')

                start_page.english_button.clicked.connect(english_button_clicked)
                start_page.persian_button.clicked.connect(persian_button_clicked)

                self.setCentralWidget(start_page)

            case 'Password':
                password_page = PasswordPage()

                def submit_button_clicked():
                    if account.check_password(password_page.password_input.text()):
                        self.show_page('Main')
                    else:
                        password_page.submit_button.setStyleSheet('color: red')

                password_page.submit_button.clicked.connect(submit_button_clicked)

                self.setCentralWidget(password_page)

            case 'Main':
                main_page = MainPage()

                main_page.buttons[0][0].clicked.connect(partial(self.show_page, 'Cash'))
                main_page.buttons[0][1].clicked.connect(partial(self.show_page, 'Change Password'))
                main_page.buttons[1][0].clicked.connect(partial(self.show_page, 'Money Transfer'))
                main_page.buttons[1][1].clicked.connect(partial(self.show_page, 'Balance'))

                self.setCentralWidget(main_page)

            case 'Cash':
                cash_page = CashPage()

                moneyStr_to_int = {'500,000': 500000, '1,000,000': 1000000, '1,500,000': 1500000, '2,000,000': 2000000}

                def func(amount):
                    if account.get_cash(moneyStr_to_int[amount]):
                        self.show_page('Good Mission')
                    else:
                        self.show_page('Bad Mission')

                for i in range(2):
                    for j in range(2):
                        cash_page.buttons[i][j].clicked.connect(partial(func, cash_page.buttons[i][j].text()))

                self.setCentralWidget(cash_page)

            case 'Money Transfer':
                money_transfer_page = MoneyTransferPage()

                def func():
                    amount = money_transfer_page.amount_input.text()
                    if account.get_cash(int(amount)):
                        self.show_page('Good Mission')
                    else:
                        self.show_page('Bad Mission')

                money_transfer_page.confirm_button.clicked.connect(func)

                self.setCentralWidget(money_transfer_page)

            case 'Balance':
                balance_page = BalancePage()

                balance_page.button.clicked.connect(partial(self.show_page, 'Main'))

                self.setCentralWidget(balance_page)

            case 'Change Password':
                change_password_page = ChangePasswordPage()

                def button_clicked():
                    account.change_password(change_password_page.password_input.text())
                    self.show_page('Main')

                change_password_page.submit_button.clicked.connect(button_clicked)

                self.setCentralWidget(change_password_page)

            case 'Good Mission':
                mission_page = GoodMissionPage()

                mission_page.new_mission_button.clicked.connect(partial(self.show_page, 'Main'))
                mission_page.goodbye_button.clicked.connect(partial(self.show_page, 'Start'))

                self.setCentralWidget(mission_page)

            case 'Bad Mission':
                mission_page = BadMissionPage()

                mission_page.new_mission_button.clicked.connect(partial(self.show_page, 'Main'))
                mission_page.goodbye_button.clicked.connect(partial(self.show_page, 'Start'))

                self.setCentralWidget(mission_page)

