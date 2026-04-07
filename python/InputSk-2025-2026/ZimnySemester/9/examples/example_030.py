def otoc(retazec):
    if len(retazec) <= 1:
        return retazec
    return retazec[-1] + otoc(retazec[1:-1]) + retazec[0]

print(otoc('Bratislava'))
print(otoc('Bratislava' * 110))
print(otoc('Bratislava' * 220))