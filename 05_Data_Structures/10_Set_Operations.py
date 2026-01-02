a = {1, 2, 3}
b = {3, 4, 5}


# union(): Returns a new set containing all unique elements from both sets
union_set = a.union(b)
print("Union:", union_set) 


# intersection(): Returns a new set containing elements common to both sets
intersection_set = a.intersection(b)
print("Intersection:", intersection_set) 


# difference(): Returns a new set containing elements in the first set but not in the second
difference_set = a.difference(b)
print("Difference (a - b):", difference_set)  