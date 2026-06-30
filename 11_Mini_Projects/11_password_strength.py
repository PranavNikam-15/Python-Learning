import string

def check_password_strength():

    print("Password Strength Checker")
    password = input("Enter a password to check: ")
    
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    print(f"\nPassword Strength Score: {score}/5")

    if score <= 2:
        print("Weak password. Try adding numbers, uppercase letters, and symbols.")

    elif score in [3, 4]:
        print("Moderate password. Getting there!")

    else:
        print("Strong password! Excellent security.")


check_password_strength()