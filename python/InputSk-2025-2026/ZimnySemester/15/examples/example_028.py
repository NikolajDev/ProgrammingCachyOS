def rekurzia(n):
    if n == 0:
        print('.', end=' ')    # triviálny prípad
    else:
        rekurzia(n - 1)        # <--- volanie funkcie
        # návratové miesto
        print(n, end=' ')
        rekurzia(n - 1)        # <--- volanie funkcie
        # návratové miesto

rekurzia(3)                    # <--- volanie funkcie
# návratové miesto
print('koniec')