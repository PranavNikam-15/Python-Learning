# Add a class attribute wheels = 4 to the Car class and a method start() 
# that prints "[brand] engine started!". Test it with an object.

class Car:

    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} engine started!")
        

c = Car("Honda", "Civic")
print("Wheels:", c.wheels)
c.start()