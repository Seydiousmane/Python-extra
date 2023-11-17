
noms = []
while True:
    nom = input('Entrer votre nom ')
    if nom == "":
        break
    noms.append(nom)

for nom in noms:
    print(nom)