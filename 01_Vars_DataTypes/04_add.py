# First input and type casting to int

a = input("Enter first number: ")
# Initially input type is STRING, need to type cast to int
b = int(a)


# Second input and type casting to int

c = input("Enter second number: ")   
d = int(c)
# c = int(input("Enter second number: ")) 

# Adding both numbers
print("The sum is:" , b + d)

# a = int(input("Enter first number: ")) 
# c = int(input("Enter second number: ")) 
# print("Sum is :", a + c)


# Taking user input for first and last name, and performing string concatenation
name = input("Enter First Name: ")
surname = input("Enter Last Name: ")

# Concatenating first name and last name, and printing the result
print("Hello! I'm", name + " " + surname)  # if all inputs are strings, it concatenates them