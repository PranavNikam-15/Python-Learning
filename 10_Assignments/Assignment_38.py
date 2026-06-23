# Import the csv module and write a list of lists representing 
# user scores into a CSV file named scores.csv.

import csv

data = [["Name", "Score"], ["Alice", 95], ["Bob", 88]]

with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
print("CSV file created.")


# ----------------------------------------------------


# Q: Write a program that reads the `scores.csv` file created previously and calculates the average score of all entries.

with open("scores.csv", "r") as f:

    reader = csv.reader(f)
    next(reader)
    scores = [int(row[1]) for row in reader]

avg = sum(scores) / len(scores)
print("Average Score:", avg)