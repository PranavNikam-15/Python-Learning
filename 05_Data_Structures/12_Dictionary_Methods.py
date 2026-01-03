dic = {"a": 1, "b": 2, "c": 3}
print(dic)

# get(key, default):
# Returns the value of the specified key
# If the key does not exist, it returns the default value
print(dic.get("a", "Not Found"))   # Output: 1

# pop(key): Removes the specified key and returns its value
dic.pop("c")
print(dic)

# Adding a new key–value pair
dic["d"] = 4
print(dic)

# popitem(): Removes and returns the last inserted key–value pair
dic.popitem()
print(dic)

# update(): Updates the dictionary with key–value pairs from another dictionary
dic.update({"d": 5})
print(dic)

# keys(): Returns all keys
print(dic.keys())

# values(): Returns all values
print(dic.values())

# items(): Returns all key–value pairs as tuples
print(dic.items())