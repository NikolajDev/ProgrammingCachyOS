def faktorial(n):
    vysl = 1
    for i in range(2, n + 1):
        vysl *= i
    return vysl