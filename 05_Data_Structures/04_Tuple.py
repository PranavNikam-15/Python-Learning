# A tuple is an ordered, immutable collection that can store elements of different data types.

new_tuple = (15, 11.05, "Python", True)
print(new_tuple)

print(new_tuple[2])  # Access element at index 2

# Tuples are immutable (elements cannot be changed after creation)
# new_tuple[2] = "Java"  -> throws error


# Creating a tuple with a single element

tu = (15)   # This is not a tuple
print(tu)

_tu = (15,) # This is a tuple with one element
print(_tu)