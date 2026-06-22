# Q: Write a simple decorator function my_decorator
# that prints a message before and after a target function runs.

def my_decorator(func):
    def wrapper():
        print("--- Before function execution ---")
        func()
        print("--- After function execution ---")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()