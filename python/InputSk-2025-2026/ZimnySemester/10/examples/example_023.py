def ocisluj(tab):
    poc = 0
    for riadok in tab:
        for j in range(len(riadok)):
            riadok[j] = poc
            poc += 1