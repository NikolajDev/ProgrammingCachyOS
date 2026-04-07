def vypis_dva_zoznamy(zoznam):
    zoz1 = zoz2 = []
    for prvok in zoznam:
        if prvok < 0:
            zoz1.append(prvok)
        else:
            zoz2.append(prvok)
    print('zaporne =', zoz1)
    print('nezaporne =', zoz2)