# An exception is an error that occurs during program execution
# If not handled, it stops the program

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b

except ValueError:
    print("Invalid input! Enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Division result:", result)

finally:
    print("Execution completed.")
    

# try: Code that may raise an exception
# except: Handle specific exceptions
# else: Executes if no exception occurs
# finally: Always executes (cleanup code)