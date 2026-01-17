# filter() : Filters elements based on a condition (True/False)
# - filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6]

def check_even(n):
    return (n % 2 == 0)

evens = list(filter(check_even, numbers))
print(evens)