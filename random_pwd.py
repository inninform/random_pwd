import random

pwd = "inform"
word = ""
letters = ["i", "n", "f", "o", "r", "m"]
bool = True
j = 0
while bool:
    i = 0
    while i < 6:
        rnd = random.choice(letters)
        word += rnd
        i += 1
    print(word)
    word = ""
    if word == pwd:
        bool = False
    else:
        continue

print("inninform")



