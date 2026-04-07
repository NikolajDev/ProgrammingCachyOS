for n in 2000, 4000, 8000, 16000, 32000, 64000:
    t = [random.randrange(n) for i in range(n)]
    start = time.time()
    for i in range(n):
        zisti(t, i)
    cas = time.time()-start
    print(n, round(cas, 3))