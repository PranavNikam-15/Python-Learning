# A constructor is a special method in a class that automatically runs when an object is created.
# Its main job is to initialize the object’s attributes with values.

class Employee :

    def __init__(self, name, salary, bond):
        self.name = name
        self.salary = salary
        self.bond = bond
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"Employee name is {self.name} \nSalary is {self.salary}\nBond is for {self.bond} years")


e1 = Employee("Pranav Nikam", 50000, 5)
# print(e1.get_salary())
e1.get_info()