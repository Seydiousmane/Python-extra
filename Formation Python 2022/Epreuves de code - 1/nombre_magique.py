import random
def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        try:
            nombre_int = int(input('Quel est le nombre magique entre {} et {} ? '.format(nb_min, nb_max)))
        except:
            print('Réessayez en rentrant un nombre valide')
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Erreur: le nombre doit être entre {nb_min} et {nb_max}")
                nombre_int = 0    
    return nombre_int

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
nbr_essais = 4
essais = nbr_essais

nombre = 0
while nombre != NOMBRE_MAGIQUE and essais > 0:
    print(f"Il vous reste {essais} essais")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print('Bravo, vous avez gagné')
    elif nombre > NOMBRE_MAGIQUE:
        print('Oups, le nombre magique est plus petit')
        essais -=1
    else:
        print('Oups, le nombre magique est plus grand')
        essais -=1
    
if essais == 0:
    print(f"Vous avez perdu ! le nombre magique était: {NOMBRE_MAGIQUE}")


gagne = False
NB_VIES = 4
for i in range(0, NB_VIES):
    vies = NB_VIES-i
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
        gagne = True
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
    else:
        print("Le nombre magique est plus grand")

if not gagne:
    print(f"Vous avez perdu! Le nombre magique était: {NOMBRE_MAGIQUE}")