def insert_sort2(zoz):
    for i in range(1, len(zoz)):
        prvok = zoz.pop(i)
        j = i-1
        while j >= 0 and zoz[j] > prvok:
            j -= 1
        zoz.insert(j+1, prvok)