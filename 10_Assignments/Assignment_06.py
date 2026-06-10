# Write a ticket pricing program based on age: 
# under 5 years old is free, 5 to 17 is 50, 18 to 60 is 60, and over 60 is 40. 
# Include a check for invalid negative ages.

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age!")

elif age < 5:
    print("Ticket is Free")

elif age <= 17:
    print("Ticket Price: 50")

elif age <= 60:
    print("Ticket Price: 60")
    
else:
    print("Ticket Price: 40")