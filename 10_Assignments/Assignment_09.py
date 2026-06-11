# Use nested for loops to print a right-aligned triangle
# pattern of asterisks (*) with a height of 5.

for i in range(1, 6):
    for j in range(5 - i):
        print("  ", end="")
    for k in range(i):
        print(" *", end="")
    print()


# --------------------------------------


# Use nested for loops to print an inverted right-angled 
# triangle pattern of asterisks (*) with a height of 5.

print("\n")

for i in range(5, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()