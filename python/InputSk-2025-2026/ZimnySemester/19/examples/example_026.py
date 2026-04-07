import time

class Odmeraj():
    def __enter__(self):
        self.t = time.time()
    def __exit__(self, *p):
        print('odmerany cas', round(time.time()-self.t, 4))

def sucet(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

for n in range(1000000, 10000001, 1000000):
    print('pre n =', n, '***', end=' ')
    with Odmeraj():
        sucet(n)