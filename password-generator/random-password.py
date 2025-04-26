# import the module
import random

# password characters
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

# password characters
password_characters = upper_case + lower_case + numbers + special_characters


# function to generate password
def generate_password(length):
    return "".join(random.sample(password_characters, length))


# generate password: 12 characters
random_password = generate_password(length=12)

# print the password
print("Password: ", random_password)
