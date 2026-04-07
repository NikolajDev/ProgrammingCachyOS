zoznam = []
for i in range(30):
    hodnota = str(2 ** i)
    if '7' in hodnota:
        zoznam.append(hodnota)
print(zoznam)