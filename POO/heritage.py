#Classe Mère
class Vehicule:
    def __init__(self, nom_vehicule, qt_essence):
        self.nom = nom_vehicule
        self.essence = qt_essence

    def montrer_vehicule(self):
        return self.nom
    
    def se_deplacer(self):
        print("Le véhicule {} se déplace".format(self.nom))


class Voiture(Vehicule):
    def __init__(self, nom_voiture, essence, puissance):
        Vehicule.__init__(self, nom_voiture, essence)
        self.puissance = puissance
        


#Programme principal
v1 = Vehicule("F2 Raptor", 2250)
v2 = Vehicule("Toyota Supra", 250)
print(v1.nom)

v3 = Voiture("Toyota Sup", 250, 800)
v3.se_deplacer()