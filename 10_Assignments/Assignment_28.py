# Implement a private balance attribute __balance in the BankAccount 
# class and provide a getter method get_balance() to access it securely.

class SecureAccount:

    def __init__(self, balance):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance

acc = SecureAccount(500)
print("Balance:", acc.get_balance())