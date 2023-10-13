# Romain Cavalieri-Bélanger
# jeux_de_devinette, sept/2023

import random

# fonction qui demande a l'utilisateur de défénir des bornes
# bornes -> int: valeur borne
def bornes():
    borne = int(input('borne: '))
    return borne

jouer = True
guess = None

# boucle tant que l'utilisateur veut jouer
while jouer:
    nb_essai = 0
    x = random.randint(bornes(), bornes())

    # boucle tant que nombre est pas trouver
    while guess != x:
        guess = int(input("guess:"))
        nb_essai += 1

        if guess == x:
            print()
        elif guess > x:
            print("-")
        else:
            print("+")

    print('bravo! vous avez gagné')
    print('vous avez réussi en ', nb_essai, ' essais')

    if str(input('voulez vous rejouer, y or n')) == 'n':
        jouer = False

