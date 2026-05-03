"""
Napíš funkciu z_cifier(zoznam, sustava=10), ktorá dostane zoznam cifier v zadanej číselnej sústave (v tvare z predchádzajúcej úlohy). Funkcia vráti celé číslo (return), ktorého cifry v danej sústave zodpovedajú zadanému zoznamu. Napríklad:
"""

def z_cifier(zoznam, sustava=10):
    power_to = len(zoznam) - 1
    result = 0
    for num in zoznam:
        result += num * (sustava ** power_to)
        power_to -= 1
    return result

print(z_cifier([1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1], 2))
