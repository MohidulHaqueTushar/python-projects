# import module
import random

wordlist = []
special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

with open("wikipedia-text.txt", "r") as file:
    data = file.readlines()

    for line in data:
        words = line.split()

        for item in words:
            if len(item) > 5:
                wordlist.append(item.capitalize())

# generate password: one word + 1 special characters + 2 numbers
password = (
    "".join(random.choice(wordlist))
    + random.choice(special_characters)
    + str(random.randint(10, 99))
)

print(password)
