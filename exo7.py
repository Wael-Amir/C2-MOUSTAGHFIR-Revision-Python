def compter_mots(fichier_texte):
    with open(fichier_texte, 'r') as fichier:
        contenu = fichier.read()
        mots = contenu.split()
        nombre_mots = len(mots)
    return nombre_mots

fichier_entree = 'fichier_texte.txt'

fichier_sortie = 'resultat.txt'

nombre_mots = compter_mots(fichier_entree)

with open(fichier_sortie, 'w') as fichier:
    fichier.write(f'Le nombre de mots dans le fichier est : {nombre_mots}')

print(f'Le résultat a été écrit dans {fichier_sortie}')
