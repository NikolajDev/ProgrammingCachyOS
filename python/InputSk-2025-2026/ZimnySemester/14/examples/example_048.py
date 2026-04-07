def hladaj(zoznam, hodnota):
    for r, riadok in enumerate(zoznam):
        try:
            s = riadok.index(hodnota)
            return r, s
        except ValueError:
            pass
    raise ValueError(f'{hodnota!r} is not in list')