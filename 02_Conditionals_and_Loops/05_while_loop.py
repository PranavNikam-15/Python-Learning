# A while loop allows to repeatedly execute a block of code as long as a specified condition is True.
# It is useful when the number of iterations is not known in advance.

# Initialize counter
i = 1

# Loop will continue as long as i <= 5
while i <= 5:
    print(i)
    i += 1  # Increment i

# Output:
# 1
# 2
# 3
# 4
# 5


# Print the first 10 even numbers
print("\n\nEven No :\n")
num = 2  # Starting from the first even number
count = 0  # To keep track of how many even numbers we printed

while count < 10:
    print(num)
    num += 2  # Move to the next even number
    count += 1  # Increment the count