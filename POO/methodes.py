class Humain:
    lieu_habitation = "Terre"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self, mesage):
        print('{} a dit {}'.format(self.nom, mesage))
    
    def changer_planete(cls, nouvelle_planete):
        Humain.lieu_habitation = nouvelle_planete

    changer_planete = classmethod(changer_planete)
    
    def definition():
        print("L'humain est classé comme étant...")

    definition = staticmethod(definition)

h1 = Humain("Jason",24)
h1.parler('Waxx waxxet')

print('Planéte actuelle {}'.format(Humain.lieu_habitation))    
Humain.changer_planete("Mars")
print('Planéte actuelle {}'.format(Humain.lieu_habitation))

Humain.definition()
        