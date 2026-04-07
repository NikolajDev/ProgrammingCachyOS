import random

zoz = [random.randrange(10000) for i in range(5000)]
zoz1 = sorted(zoz)
zoz2 = quick_sort(zoz)
print(zoz1 == zoz2)