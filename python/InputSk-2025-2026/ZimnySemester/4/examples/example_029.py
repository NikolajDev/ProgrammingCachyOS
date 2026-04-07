def ma_delitela(cislo):
    ma = False
    for delitel in range(2, cislo):
        if cislo % delitel == 0:
            ma = True
            break
    return ma

def je_prvocislo(cislo):
    return cislo > 1 and not ma_delitela(cislo)