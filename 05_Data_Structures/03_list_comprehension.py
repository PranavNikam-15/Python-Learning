# List comprehension is a concise way to create lists in a single line of code.

# List of squares
numbers = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in numbers]  # Square each number in the list
print(squares)

# Filtering with list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]  # Keep only even numbers
print(even_numbers)

# Conditional expressions inside list comprehension
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]  
print(labels)

# Applying a function to each element
words = ["python", "java", "c++"]
upper_words = [word.upper() for word in words]
print(upper_words)