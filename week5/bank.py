class BankAccount:
    def __init__(self) :
        self.__balance = 0
    def deposit(self, amount):
        self.__balance+=amount
        print(f"your balance is {self.__balance} now")
    def withdraw(self, amount):
        if amount>0:
            self.__balance-=amount
            print(f"withdraw {self.__balance}")
        else:
            print("insufficient balance")
    def display(self):
        print(f"current balance = {self.__balance}")
account = BankAccount()
account.deposit(100)
account.withdraw(50)
account.display()
    