# Create a BankAccount class with owner and balance attributes. 
# Include methods to deposit(amount) and withdraw(amount) with a check for insufficient funds.

class BankAccount:

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount


acc = BankAccount("Alice", 100.0)
acc.deposit(50.0)
acc.withdraw(30.0)
print("Final Balance:", acc.balance)