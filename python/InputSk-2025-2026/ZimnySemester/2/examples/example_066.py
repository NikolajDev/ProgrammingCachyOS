def kombinacne_cislo(n, k):
    vysl = 1
    for i in range(n + 1 - k, n + 1):
        vysl *= i
    return vysl // faktorial(k)