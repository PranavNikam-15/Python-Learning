# Create a list of 4 fruits. Append a new fruit to 
# the list and print the updated list.

fruits = ["apple", "banana", "cherry", "mango"]

fruits.append("orange")
print("Updated fruits:", fruits)


# ----------------------------------------------------


# Given a list of numbers [45, 12, 89, 23, 7], 
# sort them in ascending order and print the highest and lowest values.

nums = [45, 12, 89, 23, 7]
nums.sort()

print("Sorted:", nums)
print("Lowest:", nums[0], "Highest:", nums[-1])


# ----------------------------------------------------


# Write a program that removes all duplicate values from the 
# list [1, 2, 2, 3, 4, 4, 5] using list methods or iteration without sets.

original = [1, 2, 2, 3, 4, 4, 5]
unique = []

for item in original:
    if item not in unique:
        unique.append(item)
        
print("Unique list:", unique)