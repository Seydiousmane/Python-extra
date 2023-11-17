#Les slices s'appliquent aux listes ou aux tuples
personnes = ("Mélanie", "Paul", "Moussa", "Alice")

for i in personnes:
    print(i)

#Afficher les 3 premières personnes
for i in personnes[0:3]:
    print(i)
#Afficher Mélanie

#slice ---> [index_depart:index_fin:step:optionnel]

#[:] => Renvoie l'ensemble
#[::2] ==> Renvoie les données avec un pas de 2

