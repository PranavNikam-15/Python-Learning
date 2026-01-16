# Instance Method :
# - Takes 'self' as the first argument
# - Can access both instance and class attributes

# Class Method :
# - Takes 'cls' as the first argument
# - Uses @classmethod decorator
# - Can access only class attributes

# Static Method :
# - Takes no 'self' or 'cls'
# - Uses @staticmethod decorator
# - Cannot access instance or class data directly


class Student:
    college_name = "VU"  # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def display_data(self):
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"College : {Student.college_name}")

    # Class Method
    @classmethod
    def change_college(cls, new_college):
        cls.college_name = new_college

    # Static Method
    @staticmethod
    def is_adult(age):
        return age >= 18


# Object
s1 = Student("Pranav Nikam", 22)

print("------ Instance Method ------ ")
s1.display_data()

print("\n------ Class Method ------")
Student.change_college("PN")
s1.display_data()

print("\n------ Static Method ------")
print("Is Adult:", Student.is_adult(s1.age))