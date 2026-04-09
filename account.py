class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. Balance: {self.balance}")

    def withdraw(self, amount):
        print("Withdraw method should be implemented by subclasses")