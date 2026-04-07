def vypis(n):
    if n >= 1:
        vypis(n-1)
        print(n, end=', ')