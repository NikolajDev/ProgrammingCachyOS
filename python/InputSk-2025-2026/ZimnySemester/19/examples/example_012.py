def insert_sort(zoz):
    for i in range(1, len(zoz)):                   # O(n**2)
        prvok = zoz[i]                       # O(1)
        j = i-1                              # O(1)
        while j >= 0 and zoz[j] > prvok:           # O(n)
            zoz[j+1] = zoz[j]                # O(1)
            j -= 1                           # O(1)
        zoz[j+1] = prvok                     # O(1)