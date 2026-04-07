zoznam = [Cas(8, 10)]

for i in range(14):
    zoznam.append(zoznam[-1].sucet(Cas(0, 50)))

for cas in zoznam:
    print(cas, end=' ')