def faktorial(n):
    vysl = 1
    while n > 1:
        vysl *= n
        n -= 1
    return vysl