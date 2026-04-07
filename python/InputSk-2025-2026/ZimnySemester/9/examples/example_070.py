def sucet(zoznam):
    if len(zoznam) == 0:
        return 0
    return zoznam[0] + sucet(zoznam[1:])