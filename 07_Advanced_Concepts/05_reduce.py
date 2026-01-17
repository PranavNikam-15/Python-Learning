# reduce() : Reduces an iterable to a single value by repeatedly applying a function
# - reduce(function, iterable)

from functools import reduce

numbers = [1, 2, 3, 4, 5]
#         [3, 3, 4, 5]
#         [6, 4, 5]
#         [10, 5]
#         [15]

sum = reduce(lambda x, y: x + y, numbers)
print(sum)