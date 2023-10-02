# Romain Cavalieri-Bélanger
# jeux_de_devinette, sept/2023

import random


#
def jeux_devinette(a, z):
    nb_essai = 0
    jouer = True

    # boucle tant que l'utilisateur veut jouer
    while jouer:
        x = random.randint(a, z)
        guess = int(input("guess:"))

        # boucle tant que nombre est pas trouver
        while guess != x:
            nb_essai += 1

            if guess > x:
                print("-")
            else:
                print("+")

            guess = int(input("guess:"))

        print('bravo! vous avez gagné')
        print('vous avez réussi en ', nb_essai, ' essais')

        if str(input('voulez vous rejouer, y or n')) == 'n':
            jouer = False



jeux_devinette(int(input('a: ')), int(input('z: ')))