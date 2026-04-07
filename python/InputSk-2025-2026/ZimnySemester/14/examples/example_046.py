def hladaj(zoznam, hodnota):
    for r in range(len(zoznam)):
        for s in range(len(zoznam[r])):
            if zoznam[r][s] == hodnota:
                return r, s
    raise ValueError(f'{hodnota!r} is not in list')