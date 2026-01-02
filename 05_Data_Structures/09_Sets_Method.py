new_set = {15, 11, 22, 5, 25}
print(new_set)


# add(value): Adds a value to the set if it doesn't already exist
new_set.add(30)
print(new_set)


# remove(value): Removes the specified element from the set
# throws error if the element is not found
new_set.remove(30)
print(new_set)
# new_set.remove(1234567)  # throws error


# discard(value): Removes the specified element from the set
# Doesn't throw an error if the element is not found
new_set.discard(1234)


# pop(): Removes and returns a random element from the set
new_set.pop()
print(new_set)


# copy(): Returns a shallow copy of the set
copy_set = new_set.copy()
print(copy_set)


# clear(): Removes all elements from the set, making it empty
new_set.clear()
print(new_set)