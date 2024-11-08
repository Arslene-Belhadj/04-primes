"""
importation pour pouvoir utiliser la fonction sqrt
"""
from math import sqrt

#### Fonction secondaire

def isprime(p):
    """
    Vérifie si un nombre entier p est un nombre premier.
    """
    if p == 1:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main ():

    # vos appels à la fonction secondaire ici
    """
    Fonction principale qui demande à l'utilisateur d'entrer un nombre 
    et affiche si ce nombre est premier ou non.
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
