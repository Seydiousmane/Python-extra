#Module pour le joueur


def parler(personnage, message):
    print("{} : {}".format(personnage, message))

def au_revoir():
    print('Au revoir !')


if __name__== "__main__":
    print("Phase de TEST player")
    parler("Pabi", 'Bonjour tout le monde')
    au_revoir()