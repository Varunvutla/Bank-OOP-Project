from account import Account

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn from Savings. Balance: {self.balance}")
        else:
            print("Insufficient balance in Savings Account")