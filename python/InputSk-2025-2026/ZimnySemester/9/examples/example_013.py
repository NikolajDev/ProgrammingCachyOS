def vypis(n):
    if n < 1:
        pass      # nerob nič, len skonči
    else:
        vypis(n-1)
        print(n, end=', ')