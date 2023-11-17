def obtenir_informations():
    return "Melanie", 18, 1.68


infos = obtenir_informations()

print(infos)
print("nom: "+infos[0])
print("age: "+infos[1])
print("taille: "+infos[2])

#LEs 3 lignes préc. reviennent à faire:
nom, age, taille = obtenir_informations()
print(f"Informations: Nom: {nom}, age: {age}, taille: {taille}")


def afficher_informations(nom, age, taille):
    print(f"Informations: Nom: {nom}, age: {age}, taille: {taille}")

afficher_informations(nom, age, taille)
afficher_informations(*infos) #Ceci renvoie le tuple correspondant aux 3 valeurs retournées dans la variable infos. On unpack le tuple
#Sans le *, on aura une erreur