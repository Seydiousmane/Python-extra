from random import randint
def genererNombre(n):
    s = [0] * n
    for i in range(n):
        s[i] = randint(1, 1000)
    return s

def triShell(tableau):
    n=0
    while n<len(tableau):
        n=3*n+1
        print(n)

    print("N divisé par trois")
    while n!=0:
        n=int(n/3)
        print(n)
        for i in range(n, len(tableau)):
            valeur = tableau[i]
            j=i
            while j > n-1 and tableau[j-n] > valeur:
                print(tableau[j-n])
                tableau[j] = tableau[j-n]
                j = j-n
            tableau[j]=valeur
            print(tableau[j])
            print('A laP')

nombres = genererNombre(20)
print(nombres)
triShell(nombres)
print(nombres)
