def vypis(zoz):
    pom = zoz[:]
    while len(pom) != 0:
        print(pom[0], end=' ')
        pom = pom[1:]
    print()