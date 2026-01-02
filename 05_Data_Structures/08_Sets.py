# A set is an unordered collection of unique elements
s = {15, "Pranav", True, 2, False}

print(s, type(s))  

# print(s[0]) -> This will throw error: 'set' object is not subscriptable
# Sets are unordered, so elements have no index

# Accessing elements using a loop (iteration)
for element in s:
    print(element)

# Converting set to a list
my_list = list(s)
print(my_list)