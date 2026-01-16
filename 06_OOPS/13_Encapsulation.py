# Encapsulation :
# - Encapsulation means binding data (variables) and methods together in a single unit (class) and controlling access to data

class BankAccount:
    def __init__(self, name, balance, atm_pin):
        self.name = name           # Public variable
        # Accessible from anywhere (inside & outside the class)

        self._balance = balance    # Protected variable
        # Should be accessed only inside the class or subclasses

        self.__atm_pin = atm_pin   # Private variable
        # Cannot be accessed directly outside the class

    def show_details(self):
        # Instance method can access all variables (public, protected, and private)
        print("Name:", self.name)
        print("Balance:", self._balance)
        print("ATM PIN:", self.__atm_pin)


acc = BankAccount("Pranav Nikam", 100000, 1234)

print("------ Accessing Variables ------")

# Public variable
print(acc.name)

# Protected variable
print(acc._balance)

# Private variable
# print(acc.__atm_pin)

print("\n------ Accessing inside class ------")
acc.show_details()
