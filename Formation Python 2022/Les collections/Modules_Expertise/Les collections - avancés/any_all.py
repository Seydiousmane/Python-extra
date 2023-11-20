#Any et all
#Any : quelconque / n'importe quel
#All

noms = ["Jean", "Sophie", "Martin", "Zoé"]

a = [True, False, False, False]
print(any(a)) #Retourne True apr_s avoir trouver au moins un seul élément True
print(all(a)) #Retourne False parce que tous les éléments ne sont pas True


found = False
for nom in noms:
    if "z" in noms.lower():
        found = True
        break

if found:
    print('Trouvé')
else:
    print('Non trouvé')


noms_avec_z = any([True  if "z" in noms.lower() else False for nom in noms])

if noms_avec_z:
    print('Trouvé')
else:
    print("Non trouvé")