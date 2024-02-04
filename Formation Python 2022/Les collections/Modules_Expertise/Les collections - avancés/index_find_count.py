noms = ["Jean", "Sophie", "Maty", "Assane"]
noms.index("Sophie") #Retourne 1

element_cherche = "Sophie"
nb_occurences = noms.count(element_cherche)
print('Nbre occurences', nb_occurences)

if element_cherche in noms:
    print(noms.index(element_cherche))
else:
    print("L'élément n'est pas dans la collection")



noms = ["Jean", "Sophie", "Maty", "Assane", "Sophie"]
if nb_occurences > 0:
    index_occurence = 0
    for i in range(nb_occurences):
        index_occurence = noms.index(element_cherche, index_occurence)
        print(element_cherche, "trouvé à", index_occurence)
        index_occurence += 1
else:
    print("L'élément n'est pas dans la collection")


a = "Jean-Martin-Toto"
i = a.find("Martin")
print(i) #Retourne 5
#On ne peut pas utiliser find dans une liste

a = "Jean-Martin-Toto"
i = a.find("martin")
print(i) #Retourne -1