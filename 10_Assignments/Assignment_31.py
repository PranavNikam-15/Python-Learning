# Implement polymorphism by writing a function animal_chorus(animal_list that 
# iterates through a list of mixed animal objects and calls make_sound() on each.

class Animal:
    def make_sound(self): pass

class Dog(Animal):
    def make_sound(self): print("Bark")

class Cat(Animal):
    def make_sound(self): print("Meow")

def animal_chorus(animals):
    for a in animals:
        a.make_sound()

animal_chorus([Dog(), Cat(), Dog()])