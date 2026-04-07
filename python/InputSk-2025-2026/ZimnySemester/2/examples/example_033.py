def vypis_sucet(n):
    sucet = 1
    print(1, end=' ')
    for i in range(2, n + 1):
        sucet = sucet + i
        print('+', i, end=' ')
    print('=', sucet)