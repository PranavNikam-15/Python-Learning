# A list is an ordered, mutable collection of elements that can store items of different data types.
my_list = [15, 2.2, "Python", True]

# Creating a list using the list() constructor
new_list = list((15, 2.2, "Python", True))

print(my_list)
print(new_list)

# Accessing list elements
print(my_list[0])   # Access first element
print(my_list[-1])  # Access last element using negative index

# Modifying list elements
my_list[1] = 11.05  # Change element at index 1
print(my_list)

# Slicing lists
print(my_list[1:3])   # Elements from index 1 to 2 (end index is exclusive)
print(my_list[:4:2])  # Elements from start to index 3 with step 2