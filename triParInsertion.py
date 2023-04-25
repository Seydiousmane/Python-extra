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


#Ak lou niit ki meunti waax, ak lou niit ki meunti deif diamou Yalla reik lay neik mou neex ko wala mou naxxari ko