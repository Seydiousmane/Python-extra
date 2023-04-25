""" liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]
resultat = [i*(i+1%(i*5)) for i in sorted(list(set(liste)))]
print(resultat) """

""" mot = "Python"
for i in range(len(mot)):
    print(i) """

""" 
nombre = 7

for i in range(11):
    print("{i} x {nombre} = {resultat}".format(i=i, nombre=nombre, resultat=i*nombre)) 
"""

"""
mot = "Python"
for i in range(len(mot)):
    print(i)
"""


""" 
nombre = 222
somme = 0
for i in str(nombre):
    somme += int(i)

print(somme)

#OU

somme = sum[int(i) for in str(nombre)] 
"""

""" employes = {}

liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]

i = 1

for element in liste:
    if not str(element).isdigit():
        employes["id-{:02d}".format(i)] = element
        i += 1

print(employes) """


symbole = "$"

taille = 10

for i in range(1, taille + 1):
    espaces = " " * (taille - i)
    print(espaces + (symbole) * i)


