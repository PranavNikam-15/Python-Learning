'''

Recursion :
- Recursion is when a function calls itself to solve a small part of the problem
- Base Case → Stops the recursion
- Recursive Case → Function calls itself

'''

def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n-1)

countdown(5)