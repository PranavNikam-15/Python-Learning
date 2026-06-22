# Write a generator function countdown(n) that yields 
# numbers counting down from n to 1.

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num, end=" ")


# ----------------------------------------------------


# Write a generator function that yields even numbers 
# up to a limit max_val. Iterate through it using a for loop.


def generate_evens(max_val):
    for i in range(2, max_val + 1, 2):
        yield i

for val in generate_evens(10):
    print(val, end=" ")