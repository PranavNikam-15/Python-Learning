'''

File operations allow a program to create, read, write and modify files stored on disk

Types of Files :
    1. Text Files : .txt, .csv
    2. Binary Files : .jpg, .png, .pdf, .exe

Steps to Work with a File :
    1. Open the file
    2. Perform operation (read/write/append)
    3. Close the file

'''

# Opening a File
# Syntax: file_object = open("filename", "mode")
f = open('08_File_Input_Output/Sample.txt', 'r')
data = f.read()
print(data)
f.close()


# Reading from a File

# read() : entire file
# read(n) : first n characters
# readline() : reads one line at a time
# readlines() : reads all lines into a list

f = open("08_File_Input_Output/Sample.txt", "r")
print(f.readline())

lines = f.readlines()
print(lines)
f.close()