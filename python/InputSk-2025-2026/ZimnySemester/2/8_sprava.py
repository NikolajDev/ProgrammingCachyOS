"""
Dostali sme správu od mimozemšťanov, ktorá je zložená zo znakov 'O' a '-'. Správa obsahuje istý počet riadkov a stĺpcov takýchto znakov. Napíš funkciu sprava(pr, ps), ktorým náhodne vygeneruješ podobnú správu, parameter ps označuje počet riadkov a ps počet stĺpcov. Môžeš dostať takýto výstup:

>>> sprava(5, 28)
    O-OOO----OO-OOO---O---OOOO-O
    OOO-OOOO----OO----O-OOOOO-O-
    O-OO-OO-OOO--O-OOO--O----OOO
    ---OO--OO-O-O--OO----OOOO--O
    -O-----O--OOOO-OO-OOO-OO---O
"""

from random import choice

def sprava(pr, ps):
    choices = 'O-'
    for _ in range(pr):
        for _ in range(ps):
            print(f"{choice(choices)}", end="")
        print()

sprava(5, 28)