def sort1(zoz):
    for i in range(1, len(zoz)):
        t, j = zoz[i], i - 1
        while j >= 0 and zoz[j] > t:
            zoz[j + 1] = zoz[j]
            j -= 1
        zoz[j + 1] = t