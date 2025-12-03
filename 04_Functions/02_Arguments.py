'''

Default Arguments : 

- Functions can have default values for parameters.
- If no value is provided, the default is used.

'''
def greet(name="Guest"):
    print(f'Hello, {name}')

greet()
greet("Pranav")

# ----------------------------------------

'''

Keyword Arguments : 

- Arguments can be passed in any order by specifying the parameter name.

'''

def intro(name, age):
    print(name, age)

intro(age=22, name="Pranav")

# ----------------------------------------

# *args → multiple positional arguments

def total(*number):
    return sum(number)

sum = total(1, 2, 3, 4)
print(sum)

# ----------------------------------------

# **kwargs → multiple keyword arguments

def info(**details):
    print(details)

info(name="Pranav", age=22)  
# {'name': 'Pranav', 'age': 21}