# Write a function print_user_profile(**kwargs) that accepts arbitrary 
# keyword arguments and prints each key-value pair formatted.


def print_user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_profile(username="Pranav Nikam", email="pranavnikam@gmail.com", role="student")