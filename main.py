from savings import SavingsAccount
from current import CurrentAccount

accounts = [
    SavingsAccount("Varun", 10000),
    CurrentAccount("Sai", 2000)
]

for acc in accounts:
    acc.withdraw(3000)