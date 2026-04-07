def vyrob(pocet_riadkov, pocet_stlpcov, hodnota=0):
    vysl = [None] * pocet_riadkov         # None alebo ľubovoľná iná hodnota
    for i in range(pocet_riadkov):
        vysl[i] = [hodnota] * pocet_stlpcov
    return vysl