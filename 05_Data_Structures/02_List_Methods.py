marks = [90, 73, 56, 92, 80]
print(marks)

# append(): Adds a new element to the end of the list
marks.append(48)
print(marks)

# pop(): Removes and returns the element at the given index (default is last element)
marks.pop()
print(marks)

# pop(index): Removes element at the specified index
marks.pop(2)  # Removes element at index 2
# marks.pop(15) -> throws IndexError if index is out of range
# marks.pop(-3) -> removes the third element from the end
print(marks)

# insert(index, element): Inserts element at the specified index
marks.insert(3, 100)
marks.insert(4, 100)
print(marks)

# count(element): Returns the number of times the element occurs in the list
print(marks.count(100))

# index(element): Returns the index of the first occurrence of the element
print(marks.index(100))

# remove(element): Removes the first occurrence of the element from the list
marks.remove(100)
print(marks)

# reverse(): Reverses the order of elements in the list
marks.reverse()
print(marks)

extra_marks = [42, 57, 99, 64]
# extend(iterable): Adds all elements of the given iterable to the end of the list
marks.extend(extra_marks)
print(marks)

# sort(): Sorts the list in ascending order
marks.sort()
print(marks)

# copy(): Returns a copy of the list
list_copy = marks.copy()
print(list_copy)

# clear(): Removes all elements from the list
marks.clear()
print(marks)