# An infinite loop is a loop that never ends because its condition always remains True and there is no mechanism inside the loop to make it false.
# Infinite loops can crash your program or make it unresponsive

i = 1
while i <= 5:
    print(i)
    # Missing: i += 1