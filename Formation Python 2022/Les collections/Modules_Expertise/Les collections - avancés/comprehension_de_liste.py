noms = ["Jean", "Sophie", "Maty", "Hassanette", "Sophie"]

longueur_noms = [len(nom) for nom in noms if len(nom)<10]
noms_avec_e = [nom for nom in noms if "e" in nom]
longueur_noms = [len(nom) if len(nom)<10 else 0 for nom in noms] #Le if à gauche conditionne la valeur elle même [4, 5, 4, 0, 5]

a = [i for i in range(5) if i%2==0]
a = [i for i in range(5) if (i//2)*2 == i]#Afficher que les nombres paires
a = [True if (i//2)*2 == i  else False for i in range(11)]
a = [(i, True if (i//2)*2 == i  else False) for i in range(11)] #[(0, True), ...., (9, False), (10, True)]
print(a)
