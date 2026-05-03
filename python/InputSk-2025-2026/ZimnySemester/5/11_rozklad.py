"""
odovzdaj Napíš funkciu rozklad(cislo), ktorá rozloží dané celé číslo cislo na prvočinitele (súčin prvočísel). Výsledkom funkcie bude n-tica (tuple) týchto prvočísel (prvočiniteľov). Funkcia nič nevypisuje. Napríklad:

r = rozklad(478632)
r
    (2, 2, 2, 3, 7, 7, 11, 37)
rozklad(43)
    (43,)
"""

def rozklad(cislo: int) -> tuple[int]:
    result = []
    delitel = 2
    while cislo > 1:
        if cislo % delitel == 0:
            result.append(delitel)
            cislo //= delitel
        else:
            delitel += 1
    return tuple(result)

print(rozklad(43))
