import random

liste_de_nombres = [random.randint(1, 100) for _ in range(10)]

maximum = max(liste_de_nombres)
minimum = min(liste_de_nombres)
somme = sum(liste_de_nombres)

moyenne = somme / len(liste_de_nombres)

print("Liste de nombres :", liste_de_nombres)
print("Maximum :", maximum)
print("Minimum :", minimum)
print("Moyenne :", moyenne)
