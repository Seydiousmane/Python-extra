#LISTES - ALGO : VALEUR LA PLUS PETITE

noms_chauffeurs = ["Patrick", "MOussa", "Alex", "Mathurin", "Ossam", "Alice"]
distance_chauffeur = [1.5, 2.2, 0.9, 0.4, 7.5, 10]

distance_min = distance_chauffeur[0]
for distance in distance_chauffeur:
    if distance < distance_min:
        distance_min=distance

print("Distance minimale: ", distance_min, "km")


#Récupérer l'index de la distance min et de son chauffeur
index_min = 0
distance_min = distance_chauffeur[0]
for i in range(len(distance_chauffeur)):
    distance = distance_chauffeur[0]
    if distance < distance_min:
        distance_min=distance
        index_min = i

print("Distance minimale: ", distance_min, "km")
print("Index de la distance minimale ", index_min)
print("Chauffeur avec la distance minimale", noms_chauffeurs[index_min])

#La solution avec sort() marchera pour la distance mais on ne pourrait pas avoir l'index du chauffeur
#Optimisons la liste des distances et des noms de chauffeurs
noms_et_distances = [("Patrick", 1.5), ("MOussa", 2.2), ("Alex", 0.9), ("Mathurin", 0.4), ("Ossam", 7.5), ("Alice", 10)]