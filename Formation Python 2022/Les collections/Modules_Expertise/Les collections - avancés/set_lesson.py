#La fonction set
""" Le set fait partie des collections et utilise des ‘tables de hachage’. Il permet de rendre uniques les 
éléments en supprimant les doublons. 
Attention : Le set est énumérable (on peut récupérer tous les éléments) mais pas indexable (il n’y 
a pas de notion d’ordre dans le set)  """

""" On utilise la syntaxe avec les accolades comme pour un dictionnaire. Mais ici il n’y a pas 
d’association avec une valeur. Les valeurs sont en réalité des clefs.  """

noms = ["Jean", "Moussa", "Samba", "Christophe", "Zoé", "Moussa"]
set_noms = set(noms)
print(set_noms)#{"Jean", "Moussa", "Samba", "Christophe", "Zoé"}
print(set_noms[0])#Erreur
""" Indexation 
Il n’est pas possible d’indexer in set. Par exemple ‘print(set_noms[0])’ va créer une exception. 
Pour contourner ce problème, il est possible de convertir le set en une liste : """
noms_sans_doublons = list(set(noms))
print(noms_sans_doublons[0])#Jean