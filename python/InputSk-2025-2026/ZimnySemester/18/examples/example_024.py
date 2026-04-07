import random

zoz = [random.randrange(100) for i in range(5000)]
zoz1 = sorted(zoz)          # kontrolne utriedený zoznam
bubble_sort(zoz)            # bublinkové triedenie
print(zoz == zoz1)