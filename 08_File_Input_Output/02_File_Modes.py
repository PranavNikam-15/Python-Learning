# File modes determine how a file will be opened for reading, writing, or appending.

'''

'r' : Read mode
- Opens a file for reading only. File must exist.

'w' : Write mode
- Opens a file for writing. Creates file if not exists. Overwrites if exists.

'a' : Append mode
- Opens a file for appending data at the end. Creates file if not exists.

'x' : Create mode
- Creates a new file. Raises error if file exists.

'r+' : Read & Write mode
- Opens file for reading and writing. File must exist.


'w+' : Write & Read mode
- Opens file for writing and reading. Creates file if not exists. Overwrites existing content.


Binary Modes :

'rb' : Read binary
'wb' : Write binary
'ab' : Append binary
'xb' : Create binary
'rb+' : Read & write binary
'wb+' : Write & read binary

'''

file = open('08_File_Input_Output/Sample.txt', 'a')
file.write("\nAppending this line\n")
file.close()

# --------------------------------------------------

file = open('08_File_Input_Output/Sample.txt', 'r')
lines = file.readlines()

for line in lines:
    print(line)

file.close()