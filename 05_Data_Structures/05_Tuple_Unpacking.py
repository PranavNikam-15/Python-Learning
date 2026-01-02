# Tuple unpacking allows assigning multiple values from a tuple

tu = (10, 20, 30, 40, 50)

a, b, c, d, e = tu 
print(a, b, c, d, e)

a, *b, c = tu
print(a)  # 10
print(b)  # [20, 30, 40]
print(c)  # 50