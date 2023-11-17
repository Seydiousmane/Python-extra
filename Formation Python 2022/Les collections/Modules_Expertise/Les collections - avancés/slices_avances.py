#LES COLLECTIONS : LISTES / TUPLES
#Slices

noms = ["Jean", "Sophie", "Martin", "Chritophe", "Zoé"]

slices_noms = noms[:] #Ici on fait une copie de noms

noms[0] = "Toto"

print(slices_noms) #["Jean", "Sophie", "Martin", "Chritophe", "Zoé"]
print(noms) #["Toto", "Sophie", "Martin", "Chritophe", "Zoé"]
