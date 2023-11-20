def extraire_extension(fichier):
    
    fichier_split = fichier.split('.')
    if len(fichier_split) > 1:
        return fichier_split[-1]
    return None

def obtenir_definitions_extensions(extension, definitions):
    for d in definitions:
        if d[0].lower() == extension.lower():
            return d[1]
    return None
    

fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))


for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        definition = obtenir_definitions_extensions(ext, definition_extensions)
        if not definition:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"
    print(fichier, "{", definition, "}")