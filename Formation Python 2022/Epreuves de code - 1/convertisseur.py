
CM = 2.54
POUCE = 0.394

def convertir():
    option = int(input('Entre une option: 1 pour la conversion en CM et 2 pour la conversion en pouce'))
    while option != 1 and option !=2:
        option = int(input('Entrer une option valide'))

    if option == 1:
        valeur = float(input('Entrer le nombre de pouces à convertir en cm'))
        resultat = convertisseur_cm_en_pouces(valeur)
        print(resultat)

    if option == 2:
        valeur = float(input('Entrer le nombre de cm à convertir en pouces'))
        resultat = convertisseur_pouces_en_cm(valeur)
        print(resultat)


def convertisseur_pouces_en_cm(valeur):
    return round(valeur * CM, 2)


def convertisseur_cm_en_pouces(valeur):
    return round(valeur * POUCE, 2)

convertir()

