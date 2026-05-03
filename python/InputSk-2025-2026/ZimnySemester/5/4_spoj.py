"""
Napíš funkciu spoj(zoznam, retazec=''), ktorá z daného zoznamu hodnôt (čísel alebo reťazcov) vyrobí jeden reťazec, ktorý obsahuje všetky prvky zoznamu, pričom medzi tieto hodnoty vloží zadaný retazec (podobne ako reťazcová metóda join()). Napríklad:
"""


def spoj(zoznam, retazec=''):
    result = ""
    for i in range(len(zoznam)):
        if i == len(zoznam) - 1:
            result += f"{zoznam[i]}"
        else:
            result += f"{zoznam[i]}{retazec}"
    return result

print(spoj(['12', 3, '456', 7], ' <=> '))