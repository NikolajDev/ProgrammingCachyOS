"""
odovzdaj Napíš funkciu cifry(cislo, sustava=10), ktorá vráti (return) zoznam cifier daného čísla v zadanej číselnej sústave. Napríklad:
"""

def cifry(cislo, sustava=10):
    result = []
    while cislo > 0:
        result.append(cislo%sustava)
        cislo //= sustava
    return result[::-1]

print(cifry(11213, 2))