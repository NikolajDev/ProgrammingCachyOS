zoznam = []

def vypis():
    print('\n'.join(f'{meno!r}: {cislo!r}' for meno, cislo in zoznam))

def pridaj(meno, cislo):
    for i in range(len(zoznam)):
        if zoznam[i][0] == meno:
            zoznam[i] = meno, cislo
            return
    zoznam.append((meno, cislo))

def zisti(hladane_meno):
    for meno, cislo in zoznam:
        if meno == hladane_meno:
            return cislo
    print(f'zadane meno {hladane_meno!r} nie je v zozname')

def zrus(meno):
    for i in range(len(zoznam)):
        if zoznam[i][0] == meno:
            del zoznam[i]
            return
    print(f'zadane meno {hladane_meno!r} nie je v zozname')