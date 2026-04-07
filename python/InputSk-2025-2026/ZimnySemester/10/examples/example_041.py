def pocet(tab, hodnota):
    vysl = 0
    for riadok in tab:
        for prvok in riadok:
            if prvok == hodnota:
                vysl += 1
    return vysl