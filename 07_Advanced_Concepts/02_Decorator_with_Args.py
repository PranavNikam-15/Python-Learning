# decorator factory
def repeat(n):
    # It will repeat the decorated function 'n' times.

    # Actual decorator
    def decorator(func):
        # This is the actual decorator that wraps the target function.
        
        # wrapper function
        def wrapper(val):
            # This wrapper executes the original function multiple times.
            for _ in range(n):
                func(val)
      
        return wrapper
    
    return decorator


@repeat(5)
def say_hello(val):
    print(f"Hello, {val}!")


say_hello("Pranav")