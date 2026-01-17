# A decorator is a function that modifies another function
# without changing its source code.

def my_decorator(func):
    def wrapper():
        print("I am about to execute this function...")
        func()
        print("I executed this function.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

say_hello()