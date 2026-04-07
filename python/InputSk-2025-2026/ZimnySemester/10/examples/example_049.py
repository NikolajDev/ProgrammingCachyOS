def index(tab, hodnota):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == hodnota:
                return i, j