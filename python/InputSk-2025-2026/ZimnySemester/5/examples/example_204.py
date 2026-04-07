def delitele(cislo):
    vysl = ()
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            vysl = vysl + (i,)
    return vysl