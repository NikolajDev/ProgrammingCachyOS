def trojuholnik(n, obrys='*', vnutro='-'):
    print(' ' * (n - 1) + obrys)
    for i in range(1, n - 1):
        print(' ' * (n - i - 1) + obrys + vnutro * (2 * i - 1) + obrys)
    print(obrys * (2 * n - 1))