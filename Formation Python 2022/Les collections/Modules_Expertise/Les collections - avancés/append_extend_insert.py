#LES COLLECTIONS : LISTES / TUPLES
#Append / Extend / += / Insert

noms = ["Jean", "Moussa", "Samba"]
noms_supplementaires = ["Christophe", "Zoé"]

noms.append("Toto")
noms.append(noms_supplementaires) #retourne ["Jean", "Moussa", "Samba", ["Christophe", "Zoé"]]

for e in noms_supplementaires:
    noms.append(e) #retourne ["Jean", "Moussa", "Samba", "Christophe", "Zoé"]

#En plus court avec la mèthode extend
noms.extend(noms_supplementaires) #retourne ["Jean", "Moussa", "Samba", "Christophe", "Zoé"]
noms += noms_supplementaires #retourne ["Jean", "Moussa", "Samba", "Christophe", "Zoé"]

#insert pour faire des rajouts suivant l'index
noms.insert(0, "Toto") #retourne ["Toto", "Jean", "Moussa", "Samba", "Toto"]

noms = "Toto" + noms #retourne error car on ne peut pas concaténer une chaine de caractères et une liste
noms = ["Toto"] + noms #retourne ["Toto", "Jean", "Moussa", "Samba", "Toto"]



print(noms)