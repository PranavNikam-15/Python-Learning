class Employee :

    company = "Asus" # class attribute

    def __init__(self, name, salary, bond, company):
        self.name = name
        self.salary = salary
        self.bond = bond
        self.company = company # Instance Variable
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"Employee name is {self.name} \nSalary is {self.salary}\nBond is for {self.bond} years")


e1 = Employee("Pranav Nikam", 50000, 5, "Tesla")
e1.get_info()
print(e1.company) # This will always print instance variable whenever present