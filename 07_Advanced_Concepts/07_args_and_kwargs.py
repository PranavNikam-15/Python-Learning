# *args allows a function to accept any number of positional arguments
#  All positional arguments passed to the function are automatically packed into a tuple

def add_numbers(*args):
    total = 0
    for item in args:
        total += item
    return total

sum = add_numbers(15, 5, 15)
print(f"Sum : {sum}")

print()


# **kwargs allows a function to accept a variable number of keyword arguments
# Inside the function, kwargs is a dictionary

def student_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
        print(f"{key} :  {val}")

student_info(Name="Pranav Nikam", Age=22, Branch="CSE")