def otoc(retazec):
    if len(retazec) <= 1:
        return retazec
    stred = len(retazec) // 2
    prva = otoc(retazec[:stred])
    druha = otoc(retazec[stred:])
    return druha + prva

print(otoc('Bratislava'))
print(otoc('Bratislava' * 110))
print(otoc('Bratislava' * 220))
povodny = 'Bratislava' * 100000
r = otoc(povodny)
print(len(r), r == povodny[::-1])