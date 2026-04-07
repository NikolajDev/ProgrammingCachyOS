n = int(input('zadaj číslo: '))
faktorial = 1
for cislo in range(2, n + 1):
    faktorial = faktorial * cislo
print(n, 'faktoriál =', faktorial)