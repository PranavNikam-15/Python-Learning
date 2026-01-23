import os

# os.remove() : used to delete a file
# File must exist otherwise it raises FileNotFoundError


try :
    os.remove("08_File_Input_Output/Sample_2.txt")
except FileNotFoundError:
    print("File Not Found !") 