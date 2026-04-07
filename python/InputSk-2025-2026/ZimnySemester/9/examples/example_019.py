def vypis(n):
    if n < 1:
        pass                 # skonči
    else:
        print(n, end=', ')
        vypis(n - 1)
        print(n, end=', ')

vypis(10)