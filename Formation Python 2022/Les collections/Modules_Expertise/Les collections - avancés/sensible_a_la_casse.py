def element_dans_liste(e, l):
    """ for el in l:
        if e.lower() in l.lower():
            return True
    return False """
    l_lower = [el.lower() for el in l]
    return e.lower() in l_lower

noms = ["Jean", "Sophie", "Martin", "Christophe", "Martin"]

if element_dans_liste("Jean", noms):
    print("Jean est là")
else:
    print("Jean n'est pas là")