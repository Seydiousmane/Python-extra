import os
import random
import time

NIVEAUX_DIFFICULTE = (
    {
        "titre": "Facile",
        "longueur_seq": 2,
        "sequence_inc": 1,
        "duree_memo": 3,
        "nombre_essais": 3
    },
    {
        "titre": "Normal",
        "longueur_seq": 3,
        "sequence_inc": 2,
        "duree_memo": 3,
        "nombre_essais": 2
    },
    {
        "titre": "Difficile",
        "longueur_seq": 4,
        "sequence_inc": 3,
        "duree_memo": 2,
        "nombre_essais": 2
    }
)

def clear_screen():
    if(os.name == "posix"):
        os.system('clear')
    else:
        os.system('cls')


def entrer_valeur_numerique_min_max(min, max):
    valeur = input(f"Rentrez une valeur entre {min} et {max}: ")
    try:
        valeur_int = int(valeur)
    except:
        print('Erreur: Vous devez rentrer une valeur numérique valide')
        return entrer_valeur_numerique_min_max(min, max)
    
    if not(min <= valeur_int <= max):
        print(f"ERREUR : Vous devez rentrer une valeur numérique entre {min} et {max}")
        return entrer_valeur_numerique_min_max(min, max)
    return valeur_int


def choix_niveaux_difficulte(niveaux):
    print('Choisissez votre niveau')
    index = 1
    for niveau in niveaux:
        print(f"{index} - {niveau['titre']}")
        index += 1
    choix = entrer_valeur_numerique_min_max(1, len(niveaux))
    return niveaux[choix-1]


def generer_sequence(n):
    sequence = ""
    for i in range(n):
        chiffre = random.randint(0, 9)
        sequence += str(chiffre)
    return sequence


choix_dict = choix_niveaux_difficulte(NIVEAUX_DIFFICULTE)
sequence = generer_sequence(choix_dict['longueur_seq'])
longueur_sec = choix_dict['longueur_seq']

clear_screen()

score = 0
vies = choix_dict['nombre_essais']
print(f"Début jeu - niveau {choix_dict['titre']}")

while True:
    print("Retenez la sequence")
    time.sleep(1)
    print(sequence)
    time.sleep(choix_dict['duree_memo'])
    clear_screen()
    sequence_retenue = input('Entrer la séquence retenue')

    if sequence == sequence_retenue:
        score += 1
        sequence += generer_sequence(choix_dict['sequence_inc'])
    else:
        vies -= 1
        if vies <= 0:
            break
        print('Mauvaise réponse, réessayez ')
    time.sleep(1)
    clear_screen()

print("Mauvaise réponse")
print(f"La séquence était {sequence}")
print(f"Votre score final est : {score}")