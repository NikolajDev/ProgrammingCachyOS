def min_max(zoznam):
    minz = maxz = zoznam[0]
    for p in zoznam[1:]:
        if p < minz:
            minz = p
        if p > maxz:
            maxz = p
    return minz, maxz