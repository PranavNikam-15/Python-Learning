'''

String indexing is a simple way of accessing individual characters of a string using their position (index)
A string is a sequence, so each character has a specific index.

'''

name = "PRANAV"

#   P   R   A   N   A   V
#   0   1   2   3   4   5    <-- Positive Indexing
#  -6  -5  -4  -3  -2  -1    <-- Negative Indexing
 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

print("\n")

n = len(name) # length of string

print(name[-6])  #   name[-6 + n]  = name[0] , n = 6
print(name[-5])
print(name[-4])  #   name[-4 + n]  = name[2]
print(name[-3])
print(name[-2])
print(name[-1])