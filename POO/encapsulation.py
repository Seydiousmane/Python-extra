#Encapsulation: Tout attribut appartenant à la classe ou à un objet de la classe ne peut être modifier à l'extérieur de la classe
#Convention: Les dev ont tendance à mettre devant les attributs inaccessibles à l'extérieur un _

class Humain:

    def __init__(self, nom, age):
        self.nom = nom
        self._age = age


    def _getage(self):
        try:
            if self._age <=1:
                return str(self._age) + " an"
            else:
                return str(self._age) + " ans"
        except AttributeError:
            print("L'âge n'existe pas")


    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self._age = 0
        else:
            self._age = nouvel_age

    
    def _delage(self):
        del self._age

    age = property(_getage, _setage, _delage, "Je suis l'âge d'un humain")

h1 = Humain("Jason", 1)

print(h1.age)
del h1.age

print(h1.age)
help(Humain.age)

h1._setage(12)
print(h1.age)


        