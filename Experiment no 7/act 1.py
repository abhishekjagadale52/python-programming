# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:22:46 2026

@author: abhishek jagadale
"""
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
            print(f"New Balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            print(f"Current Balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            print(f"Remaining Balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

# --- Example Usage ---
# 1. Create an account
my_account = BankAccount("Abhishek", 1000.0)

# 2. Deposit money
my_account.deposit(500.0)

# 3. Withdraw money
my_account.withdraw(200.0)

# 4. Attempt to withdraw more than the balance
my_account.withdraw(2000.0)
