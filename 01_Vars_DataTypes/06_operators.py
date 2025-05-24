# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division (float)
print("a // b =", a // b) # Floor Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation
print()


# Comparison Operators
print("Comparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print()


# Logical Operators
x = True
y = False
print("Logical Operators:")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)   # Logical NOT
print()


# Membership Operators
fruits = ["apple", "banana", "cherry"]
print("Membership Operators:")
print("'banana' in fruits:", 'banana' in fruits)
print("'mango' not in fruits:", 'mango' not in fruits)
print()


# Identity Operators
m = [1, 2, 3]
n = [1, 2, 3]
z = m
print("Identity Operators:")
print("m is z:", m is z)         # True, both point to the same object
print("m is n:", m is n)         # False, different objects with same content
print("m == n:", m == n)         # True, content is equal
print("m is not n:", m is not n) # True, different identities
print()


# Assignment Operators
print("Assignment Operators:")
num = 5
num += 3
print("num += 3:", num)
num *= 2
print("num *= 2:", num)
print()


# Bitwise Operators
a = 10   # 1010 in binary
b = 4    # 0100 in binary
print("Bitwise Operators:")
print("a & b =", a & b)   # AND → 1010 & 0100 = 0000  (0)
print("a | b =", a | b)   # OR  → 1010 | 0100 = 1110  (14)
print("a ^ b =", a ^ b)   # XOR → 1010 ^ 0100 = 1110  (14)
print("~a =", ~a)         # NOT → ~1010 = -(1010+1) = -11
print("a << 1 =", a << 1) # Left shift → 10100 = 20
print("a >> 1 =", a >> 1) # Right shift → 0101 = 5