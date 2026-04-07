def bubble_sort(zoz):
    for i in range(len(zoz)):
        for j in range(len(zoz)-1-i):         # skracujeme vnútorný cyklus zakaždým o 1
            print(*zoz[:j], (zoz[j], zoz[j+1]), *zoz[j+2:])   # pridali sme výpis
            if zoz[j] > zoz[j+1]:
                vymen(zoz, j, j+1)