# Class : A Class is a bluprint/template which defines data (attributes) & behavior (methods) for objects.
#  e.g : Form for an exam which contains fields like name, age, birthdate, electives, etc.

# Object : An Object is a  specific intance created from class.
#  e.g :  Form that contains data of a particular student

class Employee:
    company = "HP"

    def get_salary(self): # self is way to reference the object of a class being created
        return 50000

e1 = Employee() # object of class Employee is created 
print(e1.get_salary())

e2 = Employee()
print(e2.get_salary())
print(e2.company)