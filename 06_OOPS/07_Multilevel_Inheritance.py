# Multilevel Inheritance : A class inherits from a class which is already inherited from another class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)  # Call Person constructor
        self.roll_no = roll_no

    def display_student(self):
        self.display_person()  # Reuse parent method
        print(f"Roll No : {self.roll_no}")


class Result(Student):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age, roll_no)  # Call Student constructor
        self.marks = marks
        self.result = "Pass" if marks > 40 else "Fail"

    def display_result(self):
        self.display_student()  # Reuse Student method
        print(f"Marks  : {self.marks}")
        print(f"Result : {self.result}")


R1 = Result("Pranav", 22, 65, 81)
R1.display_result()
