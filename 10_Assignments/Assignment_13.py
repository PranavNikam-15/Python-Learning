# Create a formatted multi-line summary receipt using 
# triple quotes (`"""`) and variables for item name, quantity, and unit price.


item = "Wireless Mouse"
qty = 2
price = 24.99

receipt = f"""
--- INVOICE ---
Item: {item}
Qty:  {qty}
Total: ${qty * price:.2f}
---------------
"""


print(receipt)