def ocisluj(tab):
    poc = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] = poc
            poc += 1