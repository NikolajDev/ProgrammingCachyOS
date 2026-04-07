n = len(zoz)
pocet = 0
for i in range(n):
    for j in range(i + 1, n):
        if zoz[i] == zoz[j]:
            pocet += 1