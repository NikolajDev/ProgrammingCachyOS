def insert_sort(zoz):
    for i in range(1, len(zoz)):
        j = i
        while j > 0 and zoz[j-1] > zoz[j]:
            vymen(zoz, j-1, j)
            j -= 1
        print(*zoz)

z = [13, 7, 11, 3, 5, 2]
insert_sort(z)