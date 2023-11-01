
import random
def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        try:
            nombre_int = int(input('Entrer le nombre magique ? '))
        except:
            print('Réessayer, entrer un nombre')
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print('Le nombre magique doit être compris entre {} et {}')
                nombre_int == 0
    return nombre_int

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)


nombre = 0
essai = 0

while nombre != NOMBRE_MAGIQUE and essai < 4:
    print(f'Vous êtes à votre {essai+1} essais')
    nombre= demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print('Bravo, vous avez gagné')
        
    elif nombre > NOMBRE_MAGIQUE:
        print(f'Réessayez. Indice: Le nombre magique est inférieur à {nombre}')
        essai +=1
    else:
        print(f'Réessayez. Indice : Le nombre magique est supérieur à {nombre}')
        essai +=1
    
if essai == 4:
    print("Vous avez perdu ! Relancer le jeu")