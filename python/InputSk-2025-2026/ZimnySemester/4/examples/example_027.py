def pocet_delitelov(cislo):
    pocet = 0
    for delitel in range(1, cislo + 1):
        if cislo % delitel == 0:
            pocet += 1
    return pocet

def je_prvocislo(cislo):
    return pocet_delitelov(cislo) == 2