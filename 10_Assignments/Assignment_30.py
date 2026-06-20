# Create two subclasses Cat and Cow inheriting from Animal, each overriding make_sound(). 
# Instantiate them and call their sounds.

class Animal:
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Cow(Animal):
    def make_sound(self):
        print("Moo")

Cat().make_sound()
Cow().make_sound()