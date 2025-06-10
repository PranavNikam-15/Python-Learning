# 'break' : The break statement is used to exit a loop immediately, even if the loop’s condition is still True.
print("Break statement:")

for i in range(1, 10):
    if i == 5:
        print(f"Loop stopped at {i} using break.\n")
        break  # Exit the loop when i is 5
    print(i)



# 'continue' : The continue statement is used to skip the current iteration and move to the next iteration of the loop.
print("Continue statement:")

for i in range(1, 6):
    if i == 3:
        print(f"Skipping {i} using continue.\n")
        continue  # Skip when i is 3
    print(i)
    

# 'pass' : The pass statement does nothing. It is a placeholder when you need a syntactically correct block of code but don’t want it to perform any action.
print("Pass statement:")

for i in range(1, 6):
    if i == 3:
        print(f"Nothing happens at {i} using pass.\n")
        pass  # Does nothing
    print(i)