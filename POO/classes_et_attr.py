class Humain:
    humain_cree = 0
    def __init__(self, prenom, nom, age):
        print('A', self)
        self.prenom = prenom
        self.nom = nom
        self.age = age

        Humain.humain_cree +=1

print("Lancement du programme")
h1 = Humain("Jojo", "Mbaye", 34)
h1.prenom = "Thomas"
print("Prénom de h1 -> {}".format(h1.prenom))

h2 = Humain("Moussa", "Fall", 17)
print("Prénom de h2 -> {}".format(h2.prenom))

print('Humains existants {}'.format(Humain.humain_cree))