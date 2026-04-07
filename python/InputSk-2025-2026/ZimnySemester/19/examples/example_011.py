def generuj(i):
    for j in range(n):
        if not bolo[j]:
            zoz[i] = j
            bolo[j] = True
            if i == n - 1:
                print(zoz)
            else:
                generuj(i + 1)
            bolo[j] = False

n = 3
zoz = [0] * n
bolo = [False] * n
generuj(0)