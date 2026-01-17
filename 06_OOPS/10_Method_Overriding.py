# Method Overriding occurs when a child class provides its own implementation of a method that is already defined in the parent class
# It is a form of runtime polymorphism (decision is made at runtime)

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):  # Overriding parent method
        print("Dog barks")

class Cat(Animal):
    def sound(self):  # Overriding parent method
        print("Cat meows")

a = Animal()
a.sound()

d = Dog()
d.sound()

c = Cat()
c.sound()