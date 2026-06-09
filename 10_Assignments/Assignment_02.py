# Calculate the total bill for a restaurant meal 
# where the food cost is 85.50, the tax is 8%, and the tip is 15% 
# (calculated on the original cost). Print the final total rounded to 2 decimal places.

food_cost = 85.50
tax = food_cost * 0.08
tip = food_cost * 0.15

total_bill = food_cost + tax + tip

print(f"Total Bill: {round(total_bill, 2)}")



# Q: Write a program that converts a temperature given in 
# Fahrenheit to Celsius using the formula C = (F - 32)5/9, and print the result.

fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5 / 9
print(f"Celsius: {celsius:.2f}")