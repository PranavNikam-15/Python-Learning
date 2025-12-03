"""

- A function is a reusable block of code that performs a specific task.
- Instead of writing the same code again and again, you write a function
  once and use it whenever needed.

"""

def greet():
    print("Hello, Python!")

# 'def' keyword is used to define a function
# function name should be menaingful


# ----------------------------------------------

'''

- A parameter is a variable inside the function definition.
  Parameters are placeholders for actual values (Arguments).

- Arguments are the actual values passed to the function when calling it.

- 'return' sends a value from the function back to the caller.

'''

def add(a, b):   # a and b are parameters
    sum = a + b
    return sum   # sends calculated result back to caller

sum = add(15, 5)   # 15 and 5 are arguments
print(sum)


# ----------------------------------------------

# Without `return` keyword :

def mul(a, b):
    print(a + b)

x = mul(22, 11)
print(x)   # Output: None