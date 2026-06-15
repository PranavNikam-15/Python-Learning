# Write a function describe_pet(name, animal="dog") that prints 
# "I have a [animal] named [name]". Test it with default and custom animal types.


def describe_pet(name, animal="dog"):
    print(f"I have a {animal} named {name}")

describe_pet("Bruno")
describe_pet("Whiskers", "cat")