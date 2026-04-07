def hladaj(zoznam, hodnota):
    for r, riadok in enumerate(zoznam):
        try:
            s = riadok.index(hodnota)
            return r, s
        except ValueError:
            if r == len(zoznam) - 1:     # posledný prechod for-cyklom
                raise