# Romain Cavalieri-Bélanger
# Devinette, sept/2023

import random

nb_essaie = 0
x = random.randint(0, 10)
guess = 0
trouver = False

# boucle tant que nombre pas trouver
while trouver:
    nb_essaie += 1
    guess = int(input("guess:"))

    if guess == x:
        print("vous avez trouvé en ", nb_essaie, " essaies")
        trouver = True

    elif guess > x:
        print("-")

    else:
        print("+")


