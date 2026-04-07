def vypis(n):
    if n < 1:
        pass               # nerob nič, len skonči
    else:
        print(n, end=', ')
        vypis(n - 1)       # rekurzívne volanie