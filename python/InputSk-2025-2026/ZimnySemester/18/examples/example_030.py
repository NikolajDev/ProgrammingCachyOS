def vymen(zoz, i, j):
    zoz[i], zoz[j] = zoz[j], zoz[i]

def insert_sort(zoz):
    print(zoz[0], '|', *zoz[1:])
    for i in range(1, len(zoz)):
        j = i
        while j > 0 and zoz[j-1] > zoz[j]:
            vymen(zoz, j-1, j)
            j -= 1
        print(*zoz[:i+1], '|', *zoz[i+1:])

zz = [7, 16, 3, 7, 9, 5, 10]
insert_sort(zz)
print('výsledok =', zz)