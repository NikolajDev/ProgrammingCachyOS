def vzostupne(zoznam):
    for i in range(len(zoznam) - 1):
        if zoznam[i] > zoznam[i + 1]:
            return False
    return True