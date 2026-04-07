def pocet(tab, hodnota):
    vysl = 0
    for riadok in tab:
        vysl += riadok.count(hodnota)
    return vysl