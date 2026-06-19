# Create a class Car with an __init__ method that sets brand and model. 
# Instantiate one object and print its attributes.


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand, my_car.model)