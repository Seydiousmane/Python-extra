from random import randint


def genererTableau(n):
    s = [0] * n
    for i in range(n):
        s[i] = randint(1, 1000)
    return s


def triParSelection(tableau):
    for i in range(0, len(tableau)):
        min = tableau[i]
        imin = i
        
        for j in range(i+1, len(tableau)):
            if tableau[j] < min:
                min = tableau[j]
                imin = j
        
        tableau[i], tableau[imin] = tableau[imin], tableau[i]

tab1 = genererTableau(100)
triParSelection(tab1)
print(tab1)

""" Le but est désormais de déplacer chaque élément à sa
position définitive.
On recherche l’élément le plus petit. Il faut donc le placer
en premier, or cette position est déjà occupée, on échange
donc les deux éléments.
Il ne reste plus qu’à répéter l’opération N fois.
Chaque échange met un élément en position définitive,
l’autre par contre est mal placé. Cependant, aucun
échange n’est inutile, car un élément qui a été bien placé,
ne sera plus testé par la suite. """