for n in range(1000, 10001, 1000):
    zoz = [random.randrange(n) for i in range(n)]
    tim = time.time()
    pocet = 0
    for i in range(n):
        for j in range(i + 1, n):
            if zoz[i] == zoz[j]:
                pocet += 1
    tim = time.time() - tim
    print(n, round(tim, 3))