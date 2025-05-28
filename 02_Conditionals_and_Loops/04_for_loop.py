# A 'for' loop allows to repeat a block of code for a specific number of times.
# It's most commonly used with the 'range()' function.

# Print numbers from 1 to 5
for i in range(1, 6):  # range(start, end) goes from start to end-1
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# Print the first 10 even numbers
print("\n\nEven No :\n")
for num in range(2, 21, 2):  # start=2, stop=21, step=2
    print(num)