def priemer(zoznam):
    sucet = 0
    pocet = 1
    for prvok in zoznam:
        sucet += prvok
        pocet += 1
    return sucet / pocet