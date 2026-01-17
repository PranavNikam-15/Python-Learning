# Abstraction : means hiding unnecessary implementation details and showing only the essential features to the user

# Abstract Class : 
# - A class that can not be instantiated
# - A class which can contain normal + abstract methods
# - A class which usually acts as a blueprint for child classes


# Abstract Method :
# It is a method declared but not implemented (Children must override abstract methods)



from abc import ABC, abstractmethod

# Abstract class
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} in Cash")


CreditCardPayment().pay(1500)
UpiPayment().pay(50_000)
CashPayment().pay(100_000)