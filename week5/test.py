import unittest

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    
    def get_balance(self):
        return self.balance


class BankAccountTests(unittest.TestCase):
    def test_initial_balance(self):
        account = BankAccount()
        self.assertEqual(account.get_balance(), 0)
    
    def test_deposit(self):
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)
    
    def test_withdraw_sufficient_funds(self):
        account = BankAccount(200)
        account.withdraw(100)
        self.assertEqual(account.get_balance(), 100)
    
    def test_withdraw_insufficient_funds(self):
        account = BankAccount(50)
        with self.assertRaises(ValueError):
            account.withdraw(100)
    
    def test_multiple_operations(self):
        account = BankAccount(500)
        account.deposit(200)
        account.withdraw(100)
        self.assertEqual(account.get_balance(), 600)


if __name__ == '__main__':
    unittest.main()