def je_prvocislo(cislo):
    for delitel in range(2, cislo):
        if cislo % delitel == 0:
            return False
    return cislo > 1