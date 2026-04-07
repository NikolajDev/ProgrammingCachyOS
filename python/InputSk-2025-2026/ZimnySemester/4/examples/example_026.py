def sucet_delitelov(cislo):
    sucet = 0
    for delitel in range(1, cislo):
        if cislo % delitel == 0:
            sucet += delitel
    return sucet

def najdi_dokonale(do):
    print(f'dokonalé čísla do {do} sú', end=' ')
    for cislo in range(1, 10001):
        if sucet_delitelov(cislo) == cislo:
            print(cislo, end=', ')
    print()
    print('=== viac ich už nie je ===')