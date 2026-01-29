# re is Regular Expression module
# It is used to search, match, find, extract, and replace patterns in strings

import re
text = "The quick brown fox jumps over the lazy dog"


# Search for a pattern
match = re.search("fox", text)

if match:
    print("Match Found!")
    print("Start Index : ", match.start())
    print("End Index : ", match.end())

print("----------------------------")

# find all occurrences of a pattern
match = re.findall("the", text, re.IGNORECASE)
print("Matches : ", match)

for m in re.finditer("the", text, re.IGNORECASE):
    print(m.group(), "->", m.start(), m.end())

print("----------------------------")


new_text = re.sub("fox", "cat", text)
print(new_text)