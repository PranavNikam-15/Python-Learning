# with is a context manager in Python. It automatically manages resource

with open('08_File_Input_Output/Sample.txt', 'r') as file:
    data = file.read()
    print(data)

# `with` ensures file is closed automatically