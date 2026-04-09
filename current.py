from account import Account

class CurrentAccount(Account):
    def withdraw(self, amount):
        overdraft_limit = 5000
        if amount <= self.balance + overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn from Current. Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")