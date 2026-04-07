def koduj(retazec):
    vysl = 0
    for znak in retazec:
        vysl = 100 * vysl + ord(znak)
    return vysl