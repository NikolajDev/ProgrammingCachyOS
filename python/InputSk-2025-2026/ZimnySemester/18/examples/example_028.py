import random

zoz = [random.randrange(100) for i in range(5000)]
zoz1 = sorted(zoz)
min_sort(zoz)
print(zoz == zoz1)