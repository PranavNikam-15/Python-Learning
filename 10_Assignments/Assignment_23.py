# Use a list comprehension to generate a 
# list of squares for numbers from 1 to 5.

squares = [x**2 for x in range(1, 6)]
print(squares)

# ----------------------------------------------------

# Use a list comprehension to filter out only
#  even numbers from the list 1 to 8.

evens = [x for x in range(1, 9) if x % 2 == 0]
print(evens)


# ----------------------------------------------------


# Create a 2D list representing a 3x3 identity 
# matrix and print each row on a new line.

identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]

print()
for row in identity:
    print(row)