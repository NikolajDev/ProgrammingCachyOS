with open('dobs.txt') as subor:
    pocet = pocty_vyskytov(subor.read())
for kluc, hodnota in pocet.items():
    print(repr(kluc), hodnota)