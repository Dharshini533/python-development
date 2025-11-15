class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Account Holder:", self.owner)
        print("Balance:", self.__balance)

acc = BankAccount("Dharshini", 5000)
acc.show_balance()
acc.deposit(2000)
acc.show_balance()