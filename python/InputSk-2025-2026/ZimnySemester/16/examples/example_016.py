>>> cisla = [7, 11, 13]
>>> sucin(cisla)              # zoznam [7, 11, 13] sa násobí 1
    [7, 11, 13]
>>> sucin(*cisla)             # sucin(cisla[0], cisla[1], cisla[2])
    1001
>>> sucin(*range(2, 11))
    3628800