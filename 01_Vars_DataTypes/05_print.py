# Quoting in strings
print('Hello " World')       # double quotes inside single quotes - works fine
# print('Hello ' World')     # invalid syntax due to conflicting quotes
print('Hello \' World')      # escaping single quote with backslash

# Print with multiple arguments
print('Hello_World', "Pranav_Nikam", 15)  # default: space separator
# Output: Hello_World Pranav_Nikam 15

# Custom separator with sep=
print('Hello_World', "Pranav_Nikam", 15, sep=',')   # no space after comma
# Output: Hello_World,Pranav_Nikam,15

print('Hello_World', "Pranav_Nikam", 15, sep=', ')  # space after comma
# Output: Hello_World, Pranav_Nikam, 15

# Using end= to control line ending
print("Hello", end=" ")
print("World")
# Output: Hello World

print("Python", end=" --> ")
print("Rocks")
# Output: Python --> Rocks