# Write a program that divides two numbers. 
# Use a try-except block to handle division by zero gracefully.

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


# ----------------------------------------------------


# Write a complete try-except-else-finally block that 
# opens a simulated resource, handles potential errors, prints 
# a success message in else, and cleans up in finally.

try:
    num = int("100")

except ValueError:
    print("Conversion failed.")

else:
    print("Conversion successful:", num)

finally:
    print("Execution completed, cleaning up resources.")