def koduj(retazec):
    vysl = 0
    for znak in retazec:
        vysl = vysl + ord(znak)
    return vysl