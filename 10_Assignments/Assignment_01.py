# Declare two integer variables x = 25 and y = 4. 
# Print their addition, subtraction, multiplication, and division results.

x = 25
y = 4

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)


# Q: Write a program that asks the user for their first name and last name, 
# then greets them with their full name.

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(f"Hello, {first_name} {last_name}!")



# Q: Ask the user for their birth year, calculate their age assuming the current year 
# is 2026, and print whether they are an adult (age >= 18) using a boolean check.

birth_year = int(input("Enter your birth year: "))

age = 2026 - birth_year
is_adult = age >= 18

print(f"Age: {age}, Is Adult: {is_adult}")