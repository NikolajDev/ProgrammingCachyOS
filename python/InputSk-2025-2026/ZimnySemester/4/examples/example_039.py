def je_prvocislo(cislo):
    delitel = 2
    while delitel < cislo and cislo % delitel != 0:
        delitel = delitel + 1
    return delitel == cislo