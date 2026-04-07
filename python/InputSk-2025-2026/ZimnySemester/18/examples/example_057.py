def min_sort(zoz):
    for i in range(len(zoz)-1):
        for j in range(i+1, len(zoz)):
            if zoz[i] > zoz[j]:
                vymen(zoz, i, j)
        print(*zoz)

z = [13, 7, 11, 3, 5, 2]
min_sort(z)