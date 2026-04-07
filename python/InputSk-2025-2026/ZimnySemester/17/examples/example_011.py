import random
import time

def zisti(zoznam, hodnota):
    for prvok in zoznam:
        if prvok == hodnota:
            return True
    return False

n = 2000
t = [random.randrange(n) for i in range(n)]
start = time.time()
for i in range(n):
    zisti(t, i)
cas = time.time()-start
print(round(cas, 3))