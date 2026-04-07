def hladaj(zoznam, hodnota):
    for r, riadok in enumerate(zoznam):
        for s, prvok in enumerate(riadok):
            if prvok == hodnota:
                return r, s
    raise ValueError(f'{hodnota!r} is not in list')