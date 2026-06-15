# Write a function named say_hello() that prints "Welcome to functions!" and call it.

def say_hello():
    print("Welcome to functions!")

say_hello()



# Write a function add_two_numbers(a, b) that returns the sum of two integers. 
# Call it with 10 and 20 and print the result.

def add_two_numbers(a, b):
    return a + b

print("Sum:", add_two_numbers(10, 20))



# Write a function is_even(num) that returns True if a 
# number is even, and False otherwise. Test it with 4 and 7.

def is_even(num):
    return num % 2 == 0

print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))