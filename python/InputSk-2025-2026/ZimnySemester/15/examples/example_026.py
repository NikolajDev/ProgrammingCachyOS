def rekurzia(n):
    if n == 0:
        print('.', end=' ')    # triviálny prípad
    else:
        rekurzia(n - 1)
        print(n, end=' ')
        rekurzia(n - 1)

rekurzia(3)
print('koniec')