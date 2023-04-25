""" Le principe du tri à bulles est de parcourir un tableau, 
procéder à l'échange des éléments adjacents en les
échangeant sur le bon ordre  """
""" Répeter le process jusqu'à ce que plus aucun échange ne soit nécessaire """

from random import randrange


def genererTableauAleatoire(n):
    s = [0]*n
    for i in range(n):
        s[i] = randrange(1, 1000)
    return s


def triABulles(tableau):
    permut = True
    n = len(tableau)
    while (permut == True):
        permut = False
        for i in range(0, n-1):
            if tableau[i] > tableau[i+1]:
                tableau[i], tableau[i+1] = tableau[i+1], tableau[i]
                permut = True

tab1 = genererTableauAleatoire(100) 
triABulles(tab1)
print(tab1)

""" Le principe consiste à balayer tout le tableau, en
comparant les éléments adjacents et en les échangeant
s’ils ne sont pas dans le bon ordre. """

