# Create a tuple containing 3 primary colors. 
# Print the second color in the tuple.

colors = ("red", "blue", "yellow")
print("Second color:", colors[1])

# ----------------------------------------------------


# Given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}, 
# find and print their union and intersection.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)


# ----------------------------------------------------

# Write a function that takes two lists of student IDs, converts them to sets, 
# and returns the IDs of students who are present in only the first list.

def exclusive_students(list1, list2):
    return list(set(list1) - set(list2))

print(exclusive_students([101, 102, 103], [102, 104]))