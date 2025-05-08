class Account:
    def __init__(self):
        self.__balance = 1000000000
        self.__password = '1234'

    def change_password(self, password):
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def get_cash(self, amount) -> bool:
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

