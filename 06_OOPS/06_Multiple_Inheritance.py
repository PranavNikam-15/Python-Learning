# Multiple Inheritance: A child class inherits from more than one class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Academics:
    def __init__(self, marks):
        self.marks = marks
        self.result = "Pass" if marks > 40 else "Fail"  

    def display_details(self):
        print(f"Marks  : {self.marks}")
        print(f"Result : {self.result}")


class Student(Person, Academics):
    def __init__(self, name, age, roll_no, marks):
        Person.__init__(self, name, age)
        Academics.__init__(self, marks)
        self.roll_no = roll_no

    def display_details(self):
        print("\n------ Student Details ------")
        Person.display_details(self)
        print(f"Roll No : {self.roll_no}")
        Academics.display_details(self)


S1 = Student("Pranav", 22, 65, 81)
S1.display_details()