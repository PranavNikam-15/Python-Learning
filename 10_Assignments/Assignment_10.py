# Use a for loop to calculate the sum of all even numbers between 1 and 20.

even_sum = 0

for i in range(2, 21, 2):
    even_sum += i
print("Sum of evens:", even_sum)