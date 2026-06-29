import time

def countdown():

    print("Countdown Timer")

    try:
        seconds = int(input("Enter time in seconds: "))

        for i in range(seconds, 0, -1):
            mins, secs = divmod(i, 60)
            print(f"{mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)

        print("Time's up!")

    except ValueError:
        print("Please enter a valid number of seconds.")


countdown()