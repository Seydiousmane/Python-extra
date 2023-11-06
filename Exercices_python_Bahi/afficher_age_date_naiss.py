from datetime import datetime
print("Ce programme affiche l'âge de l'utilisateur à partir de l'année de naissance")
date_naiss = int(input("Entrer votre date de naissance "))
print(datetime.now().year - date_naiss)