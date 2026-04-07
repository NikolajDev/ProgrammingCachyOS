def test_cele_cislo(retazec):
    for znak in retazec:
        if znak not in '0123456789':
            return False
    return True

def cislo():
    vstup = input('zadaj cislo: ')
    if test_cele_cislo(vstup):
        return int(vstup)
    print('chybne zadane cele cislo')