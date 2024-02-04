#LES COLLECTIONS : LITES / TUPLES
# join et split

#
noms = ["Jean", "Sophie", "Maty", "Assane"]

#join : Rejoindre --> coller
noms_join = (", ").join(noms)
print(noms_join) # Jean, Sophie, Maty, Assane

#split : Séparer
a = "Jean, Sophie, Maty, Assane"
a_split = a.split(", ")
print(a_split) #["Jean", "Sophie", "Maty", "Assane"]