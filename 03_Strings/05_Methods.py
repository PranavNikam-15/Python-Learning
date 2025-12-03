name = "pranav NIKAM NIKAM"

print(name.swapcase())     # Converts uppercase → lowercase and lowercase → uppercase

print(name.find('NIKAM'))  # Returns index of first occurrence, or -1
print(name.rfind('NIKAM')) # Returns index of last occurrence, or -1
print(name.index('NIKAM')) # Same as find() but gives error if not found


print(name.startswith("pranav"))  # Checks if string starts with given text
print(name.endswith("NIKAM"))     # Checks if string ends with given text


print(name.startswith(("pra", "nav")))  # True if string starts with any prefix in tuple
print(name.endswith(("kam", "raj")))    # True if string ends with any suffix in tuple


print(name.count('a'))      # Counts how many times 'a' appears in string


str = "Python"
digits = "12520304"
alnum = "abc123"

print(str.isalpha())   # Checks if all characters are alphabets
print(digits.isdigit()) # Checks if all characters are digits
print(alnum.isalnum())  # Checks if characters are alphabets or digits


# Checking for spaces
spaces = "     "
print(spaces.isspace())   # True → only spaces

spaces = "  P  "
print(spaces.isspace())   # False → contains non-space character


# Removing spaces
text = "   Hello World   "

print(text.strip())   # Removes spaces from both sides
print(text.lstrip())  # Removes spaces from left side
print(text.rstrip())  # Removes spaces from right side