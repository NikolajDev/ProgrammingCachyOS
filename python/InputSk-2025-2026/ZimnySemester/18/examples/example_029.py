def insert_sort(zoz):
    for i in range(1, len(zoz)):
        j = i
        while j > 0 and zoz[j-1] > zoz[j]:
            vymen(zoz, j-1, j)
            j -= 1