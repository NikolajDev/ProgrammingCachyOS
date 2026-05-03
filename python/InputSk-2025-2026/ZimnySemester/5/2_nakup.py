"""
Napíš funkciu nakup(zoznam), ktorá spracuje nákupný zoznam a vráti jeho celkovú cenu. Vstupný zoznam obsahuje dvojice čísel v tvare [koľko, cena, koľko, cena, ...], ktorý pre každý nakúpený tovar označuje jeho množstvo (koľko) a jednotkovú cenu (cena). Napríklad:

cena = nakup([3, 2.5, 0.5, 10, 1.2, 1.2])
cena
13.94
    
"""

def nakup(zoznam):
    result = 0
    for i in range(1, len(zoznam), 2):
        result += zoznam[i-1] * zoznam[i]
    return result

print(nakup([3, 2.5, 0.5, 10, 1.2, 1.2]))