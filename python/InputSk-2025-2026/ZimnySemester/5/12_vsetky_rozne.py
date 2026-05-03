"""
odovzdaj Napíš funkciu vsetky_rozne(postupnost), ktorá zistí (vráti True alebo False), či sú všetky prvky postupnosti rôzne (postupnost je reťazec, zoznam alebo ntica). Najprv si vyrob utriedený pomocný zoznam (nepokaz pôvodný) a v ňom zisťuj, či sa nenachádzajú dve rovnaké hodnoty za sebou. Napríklad:

vsetky_rozne([3, 8, 7, 9, 4, 1, 6, 10, 5, 2])
    True
zoz = [3, 8, 7, 9, 4, 1, 6, 3, 10, 5, 2]
vsetky_rozne(zoz)
    False
zoz
    [3, 8, 7, 9, 4, 1, 6, 3, 10, 5, 2]

"""

def vsetky_rozne(zoznam: list[int]) -> bool:
    zoradeny_zoznam = sorted(zoznam)
    for i in range(1, len(zoznam)):
        if zoradeny_zoznam[i-1] == zoradeny_zoznam[i]:
            return False
    return True

print(vsetky_rozne([3, 8, 7, 9, 4, 1, 6, 10, 5, 2]))

zoz = [3, 8, 7, 9, 4, 1, 6, 3, 10, 5, 2]
vsetky_rozne(zoz)
print(zoz)