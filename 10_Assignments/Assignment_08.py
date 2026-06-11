# Use nested for loops to print a right-angled triangle 
# pattern of asterisks (*) with a height of 5.

for i in range(1, 6):
    for j in range(i):
        print("* ", end="")
    print()