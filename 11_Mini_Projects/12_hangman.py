import random

def hangman():

    words = ["python", "developer", "programming", "github", "computer"]
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:

        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"\nWord: {display_word}")
        
        if display_word == word:
            print("Congratulations, you won!")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts remaining: {attempts}")

    print(f"\nGame Over! The word was '{word}'.")


hangman()