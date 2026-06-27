import random
import string

def generate_password():

    print("Password Generator")

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Length should be at least 4.")
            return
        
        chars = string.ascii_letters + string.digits
        password = "".join(random.choice(chars) for _ in range(length))

        print(f"Generated Password: {password}")

    except ValueError:
        print("Please enter a valid number.")


generate_password()