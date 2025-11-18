# String slicing is used to extract a portion (substring) from a string

# string[start : end : step]

# start → index from where slicing begins (inclusive)
# end → index where slicing stops (exclusive)
# step → jump value (default = 1)


str = "Python" 
# length = 6

print(str[0 : 6])        # Goes from index 0 to 5
# output: Python

print(str[1 : -1])       # Same as: str[1 : 5]
# output: ytho

print(str[:6])           # start = 0 (default)
# output: Python

print(str[2:])           # end = length of string (default)
# output: thon

print(str[:])            # start=0, end=len, step=1
print(str[::])           # same as above
# output: Python


str2 = "Pyhton_Programming"
# length = 18

# str2[0 : 18 : n ] --> step n means skip (n-1) characters in between

print(str2[0 : 18 : 1])  # step = 1 → skip 0 chars
print(str2[0 : 18 : 2])  # step = 2 → skip 1 char