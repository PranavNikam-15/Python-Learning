# Write a program to create a text file named note.txt
# and write "Hello, File IO!" into it using a with statement.

with open("note.txt", "w") as f:
    f.write("Hello, File IO!\n")
print("File written successfully.")


# Open note.txt in read mode, read its contents, 
# and print them to the console.

with open("note.txt", "r") as f:
    content = f.read()
print("File Content:", content)