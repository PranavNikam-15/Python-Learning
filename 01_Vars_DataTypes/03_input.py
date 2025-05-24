# The input() function is used to take input from the user. 
# By default, input() returns the input as a string.

# 1. Taking a number as input from the user
number = input("Enter a number: ")
print(number, type(number))

num = int(number)  # Convert the string input to an integer
print(num, type(number))

# 2. Taking a string as input
name = input("Enter your Name: ")
print("Hello,", name)
