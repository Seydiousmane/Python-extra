#LES COLLECTIONS : LISTES / TUPLES
#TRIS : Sort / Sorted

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

#Tri par ordre alphabétique
noms.sort()
noms.sort(reverse=True) #Du plus grand au plus petit
noms_tries = sorted(noms, reverse=True) #Créer une nouvelle liste

def tri_longueur_caracteres(nom):
    return len(nom)

noms.sort(key=lambda nom: len(nom))#inplace #Afficher les noms par longueur croissant
noms.sort(key=lambda nom: len(nom), reverse=True)

#Même procédé
noms.sort(key=tri_longueur_caracteres, reverse=True) #Ici on fait appel appel à un callback

print(noms)
