# Getter  : Used to access private data
# Setter  : Used to modify private data


class BankAccount:
    def __init__(self, name, balance):
        self.name = name           # Public variable
        self.__balance = balance   # Private variable

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def set_balance(self, new_balance):
        if new_balance > 0:
            self.__balance = new_balance
        else:
            print("Balance must be positive")



acc1 = BankAccount("Pranav Nikam", 100_000)

# Access public variable
print(acc1.name)

# Set new balance
acc1.set_balance(200_000)

# Get balance
print(acc1.get_balance())