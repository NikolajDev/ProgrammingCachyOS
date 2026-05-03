"""
odovzdaj Napíš funkciu cifry10(cislo), ktorá vráti cifry zadaného čísla postupným delením desiatimi, teda vo while-cykle do výsledku pridá poslednú cifru (cislo % 10) a pritom ešte samotné číslo vydelí 10. Môžeš dostať takýto výstup:

t = cifry10(4132)
t
    '2 3 1 4'
Všimni si, že cifry čísla sú v opačnom poradí ako sú v zadanom čísle.

Teraz napíš všeobecnejší variant tejto funkcie: cifry(cislo, sustava=10), ktorá vráti cifry dadého čísla, ale teraz už v normálnom poradí, pričom parameter sustava určuje číslenú sústavu (číslo z intervalu <2, 10>), pre ktorú sa vytvárajú tieto cifry. Napríklad:

cifry(4132)
    '4132'
cifry(4132, 8)
    '10044'
cifry(4132, 5)
    '113012'
Pre niektoré číslené sústavy vieme vytvoriť reťazec s ciframi v tejto sústave, napríklad

f'{4132:b} {4132:o} {4132:x}'
    '1000000100100 10044 1024'
Takto dostávame číslo 4132 v dvojkovej, osmičkovej a šestnástkovej sústave (16-ovú sústavu sme v tejto úlohe nevytvárali).

"""

def cifry10(cislo, sustava=10):
    if cislo == 0: return "0"
    result = ""
    
    while cislo > 0:
        cifra = cislo % sustava
        result = str(cifra) + result 
        cislo //= 10    
    return result

def cifry(cislo, sustava=10):
    if cislo == 0: return "0"
    res = ""
    while cislo > 0:
        res = str(cislo % sustava) + res
        cislo //= sustava
    return res

print(cifry(4132))     # '4132'
print(cifry(4132, 8))  # '10044'
print(cifry(4132, 5))  # '113012'
print(cifry(4132, 5))