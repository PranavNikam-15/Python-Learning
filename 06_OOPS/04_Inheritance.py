# Inheritance : Inheritance allows class (child class, base class) to acquire the properties & methods from another class   (Parent class, Super class)

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! I am {self.name}")


# super() function: Used to call methods from the parent class

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show_age(self):
        print(f"I am {self.age} years old")


obj = Child("Pranav", 22)

obj.greet()
obj.show_age()