# Type casting refers to converting one data type to another. 
# In Python, this is commonly done using built-in functions like int(), float(), str().

number = 15
print(number, type(number)) 

string_age = "22"
print(string_age, type(string_age)) 

# Convert the string to an integer
age = int(string_age)  # Converting string to integer
print(age, type(age))

# Integer to Float 
temperature = float(number)  # Convert the integer to float
print(temperature, type(temperature))

# Invalid Conversion: String with Letters to Integer
name = "Pranav"  # A string that cannot be converted to an integer
# print(int(name))  # Uncommenting this will raise an error because 'name' cannot be converted to an integer
