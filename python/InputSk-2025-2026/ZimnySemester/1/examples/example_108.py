pocet = int(input('zadaj počet riadkov: '))
for riadok in range(1, pocet + 1):
    for cislo in range(1, riadok + 1):
        print(cislo, end=' ')
    print()