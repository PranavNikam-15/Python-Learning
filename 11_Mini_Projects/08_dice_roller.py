import random

def roll_dice():

    print("Dice Rolling Simulator")

    try:
        num_dice = int(input("How many dice to roll? "))
        sides = int(input("How many sides per die? "))
        rolls = [random.randint(1, sides) for _ in range(num_dice)]

        print(f"Roll results: {rolls}")
        print(f"Total sum: {sum(rolls)}")

    except ValueError:
        print("Please enter valid integers.")


roll_dice()