def rekurzia(n):

# prvá časť
    if n == 0:
        print('.', end=' ')    # triviálny prípad
    else:
        rekurzia(n - 1)        # <--- volanie funkcie

# druhá časť
        # návratové miesto
        print(n, end=' ')
        rekurzia(n - 1)        # <--- volanie funkcie

# tretia časť
        # návratové miesto