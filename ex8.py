notes_des_eleves = {
    "Jean": 14,
    "Paul": 16,
    "Pierre": 12,
    "Jacque": 19,
    "Eva": 15
}

meilleur_eleve = max(notes_des_eleves, key=notes_des_eleves.get)
meilleure_note = notes_des_eleves[meilleur_eleve]

print(f"L'élève avec la meilleure note est {meilleur_eleve} avec une note de {meilleure_note}.")
