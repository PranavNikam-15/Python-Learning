# Given a string "programming", use a dictionary to count the 
# frequency of each character and print the result.

text = "programming"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1
    
print("Character Frequencies:", freq)