def pocty_vyskytov(postupnost):
    vysl = {}
    for prvok in postupnost:
        vysl[prvok] = vysl.get(prvok, 0) + 1
    return vysl

pocet = pocty_vyskytov('anicka dusicka nekasli, aby ma pri tebe nenasli.')
for kluc, hodnota in pocet.items():
    print(repr(kluc), hodnota)