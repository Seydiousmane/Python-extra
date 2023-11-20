# any / isdigit



print("a".isdigit()) # False
print("1".isdigit()) # True ne contient que des chiffres

def chaine_contient_chiffre(chaine):
    for c in chaine:
        if c.isdigit():
            return True
    return False

noms = "toto"
print(chaine_contient_chiffre(noms))



def chaine_contient_chiffre(chaine):
    return any([c.isdigit() for c in chaine])


nom = input("Quel est ton nom ?")
if nom == "":
    print('Le nom est vide')
elif chaine_contient_chiffre(nom):
    print('Ce nom est valide, il ne peut pas contenir de chiffre')
else:
    print("Bonjour ", nom)





