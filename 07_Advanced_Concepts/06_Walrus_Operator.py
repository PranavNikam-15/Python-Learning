# The walrus operator (:=) is called the assignment expression
# It allows you to assign a value to a variable and use it in the same expression


if (data := input("Enter something: ")) and len(data) > 5:
    print(data)


while (line := input("Enter text: ")) != "exit":
    print(line)