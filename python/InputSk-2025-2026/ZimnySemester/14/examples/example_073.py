>>> daj_cislo('cvicenie.py', 17, IndexError)
    ...
    IndexError: chybne zadany index
>>> daj_cislo('cvicenie.txt', 17, IndexError)
    ...
    IndexError: neexistujuci subor
>>> daj_cislo('data.txt', 3, IndexError)
    ...
    IndexError: chybne cislo v zadanom riadku
>>> daj_cislo('data.txt', 1, IndexError)
    2020
>>> print(daj_cislo('data.txt', '1'))
    None