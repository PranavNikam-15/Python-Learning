# Append a new line "Learning Python is awesome!" to note.txt, 
# then read and print all lines as a list using readlines().

with open("note.txt", "a") as f:
    f.write("Learning Python is awesome!\n")

with open("note.txt", "r") as f:
    lines = f.readlines()
print("All lines:", lines)