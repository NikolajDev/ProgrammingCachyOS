def vypis(n):
    if n < 1:
        return      # nerob nič, len skonči
    vypis(n-1)
    print(n, end=', ')