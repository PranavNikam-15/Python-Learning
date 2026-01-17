# map() : Applies a function to each element of an iterable and returns a new iterable
# - map(function, iterable)

numbers = [1, 2, 3, 4, 5]

# def sqaure(x):
#     return x*x

squares = list(map(lambda x: x*x, numbers))
print(squares)