def pocet(zoznam, hodnota):
    vysl = 0
    for prvok in zoznam:
        if prvok == hodnota:
            vysl += 1
    return vysl