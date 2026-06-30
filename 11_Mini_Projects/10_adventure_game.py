def adventure_game():

    print("Welcome to the Text Adventure Game!")
    print("You find yourself at the edge of a dark forest.")

    choice1 = input("Do you want to 'enter' the forest or 'walk' along the edge? ").lower()

    if choice1 == "enter":

        print("\nYou walk deep into the trees and find a mysterious glowing chest.")
        choice2 = input("Do you want to 'open' it or 'leave' it? ").lower()

        if choice2 == "open":
            print("It's full of treasure! You win!")
        else:
            print("You walk away safely, but miss an adventure. Game over.")

    elif choice1 == "walk":
        print("\nYou follow the edge and discover a hidden village. You are safe! You win!")

    else:
        print("Confused by your indecision, a wild animal appears. Game over!")

adventure_game()