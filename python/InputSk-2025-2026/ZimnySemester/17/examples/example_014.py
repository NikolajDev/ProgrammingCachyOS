def zisti(zoznam, hodnota):
    zac = 0                            # zaciatok intervalu
    kon = len(zoznam) - 1              # koniec intervalu
    while zac <= kon:
        stred = (zac + kon) // 2       # stred intervalu
        if zoznam[stred] < hodnota:
            zac = stred + 1
        elif zoznam[stred] > hodnota:
            kon = stred - 1
        else:
            return True
    return False