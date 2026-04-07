def otoc(retazec):
    if len(retazec) <= 1:
        return retazec
    return otoc(retazec[1:]) + retazec[0]

print(otoc('Bratislava'))
print(otoc('Bratislava' * 110))