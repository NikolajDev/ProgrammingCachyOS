def ocisluj_po_stlpcoch(tab):
    poc = 0
    for j in range(len(tab[0])):
        for i in range(len(tab)):
            tab[i][j] = poc
            poc += 1