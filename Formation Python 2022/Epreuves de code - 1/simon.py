import os
import random
import time

print('Bienvenue dans le menu du jeu du Simon')
print('Veuillez mémoriser la séquence de chiffres affichée ci-contre en 3 secondes')

def clear_screen():
    if(os.name == "posix"):
        os.system('clear')
    else:
        os.system('cls')


sequence = ""
for i in range(4):
    chiffre = random.randint(0, 9)
    sequence += str(chiffre)
clear_screen()
score = 0
while True:
    print('Retenez bien le nombre afficher pendant 3 secondes')
    time.sleep(1) 
    print(sequence)
    time.sleep(3)
    clear_screen()
    sequence_retenue = input('Rentrer la séquence retenue: ')
    if sequence == sequence_retenue:
        score += 1
    else:
        break

    chiffre = random.randint(0,9)
    sequence += str(chiffre)
    clear_screen()
        
print("Mauvaise réponse")
print(f"La séquence était {sequence}")
print(f'Votre score est {score}')
