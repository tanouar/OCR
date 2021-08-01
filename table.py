table = input("Saisissez un chiffre : ") # On attend que l'utilisateur saisisse un chiffre
table = int(table) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
nb = table

i = 0 # C'est notre variable compteur que nous allons incrémenter dans la boucle

while i < 10: # Tant que i est strictement inférieure à 10
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1 # On incrémente i de 1 à chaque tour de boucle
