# String Methods

name = "pranav NIKAM"   # Strings in Python are immutable

# name[4] = 'p'
#  This will throw a runtime error because strings cannot be modified in-place.

a = len(name)   # len() returns number of characters in the string
print(a)        # Output: 12


print(name.upper())        # Converts all letters to UPPERCASE
print(name.lower())        # Converts all letters to lowercase
print(name.title())        # Capitalizes first letter of each word
print(name.capitalize())   # Capitalizes only the first character


print(name.strip())        # Removes leading and trailing spaces
print(name.replace("a", "@"))   # Replaces all 'a' with '@'


print(name.find("nikam"))      # Returns starting index of substring OR -1
print(name.startswith("pra"))  # Checks if string starts with "pra", returns True/False
print(name.endswith("kam"))    # Checks if string ends with "kam", returns True/False


print(name.split())        # Splits string into list of words (default on spaces)