# String Formatting 


#  format() : It is used to insert values into a string by replacing placeholders { }.

name = "Pranav"
age = 22

print("My name is {} and I am {} years old.".format(name, age))

print("My name is {1} and I am {0} years old.".format(age, name)) # Using Index


# F-String

print(f"My name is {name} and I am {age} years old.")