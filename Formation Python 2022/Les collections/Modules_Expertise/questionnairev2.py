def demander_reponse_numerique(min, max):
    reponse_str = input(f"Entrer votre réponse entre " +str(min) + " et " +str(max) + ": ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print(f"Erreur, vous devez entrer un nombre entre {min} et {max}")
    except:
        print("Erreur, entrer une bonne réponse")
    return demander_reponse_numerique(min, max)

def poser_question(question):
    quest = question[0]
    choix = question[1]
    trouve = False
    solution = question[2]
    for i in range(len(choix)):
        print(" ", i+1, "-", choix[i])

    reponse = demander_reponse_numerique(1, len(choix))

    if choix[reponse-1] == solution:
        print("Bravo")
        trouve =True
    else:
        print('Mauvaise réponse')

    return trouve


def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score", score)

question1 = ("Quelle est la capilatale de la France ?", ("Marseille", "Lyon", "Paris"), "Paris")
question2 = ("Quelle est la capilatale du Sénégal ?", ("Dakar", "Diourbel", "Bignona"), "Dakar")
question3 = ("Quelle est la capilatale de l'Italie ?", ("Milan", "Rome", "Pise"), "Rome")
questionnaire = (question1, question2, question3)
lancer_questionnaire(questionnaire)