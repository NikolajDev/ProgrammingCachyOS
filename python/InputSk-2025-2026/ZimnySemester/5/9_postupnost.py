"""
odovzdaj Napíš funkciu postupnost(start, koniec, krok=1), ktorá vytvorí (vráti) takýto zoznam čísel: jeho prvky sú hodnoty od start do koniec krokom krok (podobne ako range(start, koniec, krok), ale funkcia postupnost by mala fungovať aj pre desatinné čísla). Zrejme nepoužiješ štandardnú funkciu range(). Napríklad:

postupnost(3, 100, 7)
    [3, 10, 17, 24, 31, 38, 45, 52, 59, 66, 73, 80, 87, 94]
postupnost(20, 0, -2)
    [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
postupnost(1, 5, 0)
    []
postupnost(0, 3, 0.5)
    [0, 0.5, 1.0, 1.5, 2.0, 2.5]
"""

def postupnost(start, koniec, krok=1):
    result = []
    while start < koniec:
        result.append(start)
        start += krok
    return result

print(postupnost(0, 3, 0.5))