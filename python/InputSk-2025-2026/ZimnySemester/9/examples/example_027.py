def faktorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return faktorial(n - 1) * n