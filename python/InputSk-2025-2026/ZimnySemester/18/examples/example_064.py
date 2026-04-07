zoz0 = [random.randrange(1000) for i in range(5000)]

for sort in bubble_sort, min_sort, insert_sort, quick_sort:
    zoz = list(zoz0)
    start = time.time()
    pp, pv = sort(zoz)
    cas = time.time() - start
    print(pp, pv, cas)