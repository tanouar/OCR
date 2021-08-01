def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb
    
    (max >= 0)"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
