def sum(a, b):
    c = a + b          # Local variable: stores sum of a and b
    z = 100            # Local variable: different from global z

    # Local variables have higher priority than global variables
    # Variables created inside a function are destroyed after the function finishes

    return c


def greet():
    global z           # Refers to the global variable 'z'
    z = 15             # Modifies the global variable
    print("hello")


z = 1  # Global variable

print(z)               # Output: 1 (initial global value)
print(sum(15, 22))     # Output: 37 (returned by sum function)
print(z)               # Output: 1 (unchanged by sum function)

greet()                # Calls greet(), modifies global 'z'
print(z)               # Output: 15 (updated by greet function)