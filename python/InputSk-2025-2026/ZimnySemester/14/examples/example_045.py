def nahrad(zoznam, h1, h2):
    try:
        i = zoznam.index(h1)
        zoznam[i] = h2
    except ValueError:
        pass