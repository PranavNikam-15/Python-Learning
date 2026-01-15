# Hierarchical Inheritance : Multiple child classes inherits from one parent class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks
        self.result = "Pass" if marks > 40 else "Fail"

    def display_student(self):
        print("------- Student Details -------")
        self.display_person()
        print(f"Roll No : {self.roll_no}")
        print(f"Marks  : {self.marks}")
        print(f"Result : {self.result}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        print("------- Teacher Details -------")
        self.display_person()
        print(f"Subject : {self.subject}")



# Objects
S1 = Student("Pranav Nikam", 22, 65, 81)
T1 = Teacher("Mr. Baburao Apte", 40, "Maths")

# Display details
S1.display_student()
print()
T1.display_teacher()
