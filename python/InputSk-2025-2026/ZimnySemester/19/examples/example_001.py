zoz = [2, 6, 7, 5, 4, 7, 8, 3, 1, 5, 9]
n = len(zoz)
pocet = 0
for i in range(n):
    for j in range(i + 1, n):
        if zoz[i] == zoz[j]:
            pocet += 1
print(pocet)