zz = [random.randrange(1000) for i in range(1000)]
szz = sorted(zz, reverse=True)
min_sort_rev(zz)
print(zz == szz)