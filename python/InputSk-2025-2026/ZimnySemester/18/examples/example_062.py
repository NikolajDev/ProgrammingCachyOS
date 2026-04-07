zoz = [random.randrange(1000) for i in range(5000)]
zoz1 = zoz[:]
start = time.time()
insert_sort(zoz)
prvy_cas = ...
start = time.time()
insert_sort2(zoz1)
druhy_cas = ...
print(zoz == zoz1, prvy_cas, druhy_cas)