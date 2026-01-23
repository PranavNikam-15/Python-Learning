"""

File objects have attributes that provide useful information:
- name   : Name/Path of the file as passed to open()
- mode   : Mode in which the file was opened
- closed : True if the file is closed, otherwise False

"""

file = ""

with open('08_File_Input_Output/Sample.txt', 'r') as f:
    
    # Name/Path of the file
    print("File Name/Path:", f.name)
    
    # Mode in which the file was opened
    print("File Mode:", f.mode)

    # Whether the file is closed or not
    print("File Closed? :", f.closed)
    
    # Store file object in 'file' variable
    file = f

# After 'with', the file is automatically closed
print("File Closed after 'with' block? : ", file.closed)