def bubble_sort(zoz):
    n = len(zoz)-1
    while n > 0:
        m = 0
        for j in range(n):
            if zoz[j] > zoz[j+1]:
                vymen(zoz, j, j+1)
                m = j
        n = m

def min_sort(zoz):
    for i in range(len(zoz)-1):
        m = i
        for j in range(i+1, len(zoz)):
            if zoz[m] > zoz[j]:
                m = j
        vymen(zoz, i, m)

def insert_sort(zoz):
    for i in range(1, len(zoz)):
        j, p = i-1, zoz[i]
        while j >= 0 and zoz[j] > p:
                zoz[j+1] = zoz[j]
                j -= 1
        zoz[j+1] = p