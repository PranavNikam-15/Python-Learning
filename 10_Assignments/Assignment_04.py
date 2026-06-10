# Write a program to check if an integer entered by the user is 
# positive, negative, or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")