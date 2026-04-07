zoznam = [(hodnota, kluc) for kluc, hodnota in pocet.items()]

zoznam.sort(reverse=True)

print(zoznam[:20])