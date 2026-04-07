import time

def odmoc(cislo):
    x = pocet = 0
    while x * x < cislo:
       x += 0.001
       pocet += 1
    return x, pocet

start = time.time()
x, pocet = odmoc(150000000)
print(round(x, 3), pocet, round(time.time() - start, 3))