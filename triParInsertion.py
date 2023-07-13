from random import randint


def genererNombre(n):
    s = [0]*n
    for i in range(n):
        s[i] = randint(1, 1000)
    return s

def triParInsertion(tableau):
    for i in range(0, len(tableau)):
        j = i
        while j > 0 and tableau[j] < tableau[j-1]:
            tableau[j], tableau[j-1] = tableau[j-1], tableau[j]
            j -= 1
        



tab1 = genererNombre(100)
triInsert = triParInsertion(tab1)
print(tab1)


""" Plutôt que de déplacer les éléments d’une position, on
peut prendre un élément après l’autre dans l’ordre initial,
et le placer correctement dans les éléments précédents
déjà triés, comme on le fait lorsque l’on classe ses carte à
jouer après la donne.
Le tri par insertion peut être intéressant pour des tableaux
ayant déjà été triés, mais où l’on doit rajouter quelques
nouveaux éléments. """

#Ak lou niit ki meunti waax, ak lou niit ki meunti deif diamou Yalla reik lay neik mou neex ko wala mou naxxari ko