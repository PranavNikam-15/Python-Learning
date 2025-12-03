def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

'''

Factorial of 4 :

→ 4 * factorial(3)
    → 3 * factorial(2)
            → 2 * factorial(1)
                    → 1 (base case)

Then it returns back:

factorial(1) = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24

'''