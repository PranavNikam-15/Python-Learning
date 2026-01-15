# Method overloading is compile-time polymorphism where multiple methods in the same class share the same name but differ in number or type of parameters

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3)) 
print(calc.add(2, 3, 4))