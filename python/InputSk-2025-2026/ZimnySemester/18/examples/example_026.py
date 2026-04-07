def vymen(zoz, i, j):
    zoz[i], zoz[j] = zoz[j], zoz[i]

def min_sort(zoz):
    for i in range(len(zoz)-1):
        for j in range(i+1, len(zoz)):
            if zoz[i] > zoz[j]:
                vymen(zoz, i, j)
        print(*zoz[:i], [zoz[i]], *zoz[i+1:])

zz = [7, 16, 3, 7, 9, 5, 10]
print(*zz)
print('-----------------')
min_sort(zz)
print('výsledok =', zz)