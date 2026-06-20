# Create a base class Animal with a method make_sound().
# Create a subclass Dog that inherits from Animal and prints "Bark".

class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

d = Dog()
d.make_sound()