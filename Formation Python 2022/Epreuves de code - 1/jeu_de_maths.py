import random

NBRE_MIN = 1
NBRE_MAX = 100

def poser_question():
    a = random.randint(NBRE_MIN, NBRE_MAX)
    b = random.randint(NBRE_MIN, NBRE_MAX)
    option = random.randint(0,1)
    operation = "+"
    if option == 0:
        operation = operation
        resultat = int(a+b)
    else:
        operation = '*'
        resultat = int(a*b)
    
    solution = ""
    
    while solution == "":
        try:
            solution = int(input(f'Entrer le résultat de {a} {operation} {b} '))
        except:
            print('Entrer un nombre')
    

    if resultat != solution:
        
        return False
    else:
        print('Vrai')
        return True


NB_QUESTIONS = 4
nb_points = 0

for i in range(0, NB_QUESTIONS):
    print(f"Question N° {i+1} sur {NB_QUESTIONS}")
    if poser_question():
        print('Réponse correct')
        nb_points += 1
        print(f'Vous avez {nb_points} points')
    else:
        print ('Réponse incorrecte')
        print(f'Vous avez {nb_points} points')

moyenne = nb_points / NB_QUESTIONS * 100
try:
    moyenne = int(moyenne)
except:
    moyenne = 0
    

if moyenne <=25:
    print(f'Vous avez {moyenne}%. Votre score est faible')
elif moyenne == 50:
    print(f'Vous avez {moyenne}%. Votre score est jugé passable')
elif moyenne == 75:
    print(f'Vous avez {moyenne}%. Votre score est bien')
else:
    print(f'Vous avez {moyenne}%. Votre score est excellent')