# What is a Variable ?
# A variable is like a container used to store data in a program.
# You give it a name, and assign it a value using the '=' operator.
# Example: age = 25  -  Here, 'age' is the variable name and 25 is the value.

#  Rules to define a variable :
#  - Must start with a letter (a-z, A-Z) or an underscore (_)
#  - Cannot start with a digit
#  - Cannot contain spaces or tabs
#  - Can only contain letters, digits, and underscores
#  - Case-sensitive: 'Name' and 'name' are different
#  - Should not be a Python keyword (like if, for, while)

# Example variable declarations :
name = "Pranav Nikam"    # String
age = 22                 # Integer
cgpa = 8.2               # Float
is_pass = True           # Boolean

#  Built-in data types :
#     int       - Whole numbers (e.g., 10, -5)
#     float     - Decimal numbers (e.g., 3.14, -0.001)
#     str       - Text data (e.g., "Pranav Nikam")
#     bool      - True or False
#     list      - Ordered, changeable collection (e.g., [1, 2, 3])
#     tuple     - Ordered, unchangeable collection (e.g., (1, 2, 3))
#     set       - Unordered, unique elements (e.g., {1, 2, 3})
#     dict      - Key-value pairs (e.g., {"name": "Pranav", "age": 22})

# Printing values and their types
print(name)
print(type(name))   # <class 'str'>    - The type() function is a built-in Python function that returns the data type of any value or variable.

print(age)
print(type(age))    # <class 'int'>

print(cgpa)
print(type(cgpa))   # <class 'float'>

print(is_pass)
print(type(is_pass))  # <class 'bool'>