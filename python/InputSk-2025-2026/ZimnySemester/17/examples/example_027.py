def koduj(kluc):
    vysl = 0
    for znak in str(kluc):
        vysl = 32 * vysl + ord(znak)
    return vysl