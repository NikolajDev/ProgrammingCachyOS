zoznam = []

def vypis():
    print(', '.join(repr(prvok) for prvok in zoznam))

def pridaj(prvok):
    if prvok not in zoznam:
        zoznam.append(prvok)

def vyhod(prvok):
    if prvok in zoznam:
        zoznam.remove(prvok)