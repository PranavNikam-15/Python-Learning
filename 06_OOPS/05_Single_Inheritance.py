# Single Inheritance: One child class inherits from one parent class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_details(self):
        print("\n------ Details ------")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        super().display_details()   # reuse parent method
        print(f"Roll No : {self.roll_no}")
        print(f"Marks  : {self.marks}")


S1 = Student("Pranav", 22, 65, 81)
S1.display_details()