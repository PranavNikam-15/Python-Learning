# Write a while loop to calculate the sum of all numbers from 1 to 50.

total = 0
n = 1

while n <= 50:
    total += n
    n += 1
print("Sum from 1 to 50:", total)


# Write a program that prints the multiplication 
# table for a given number from 1 to 10.

num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")