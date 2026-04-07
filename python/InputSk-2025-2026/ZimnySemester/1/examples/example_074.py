n = int(input('zadaj n: '))
sucet = 0
for i in range(n):
    sucet = sucet + i * i       # môžeme zapísať aj  sucet += i ** 2
print('súčet =', sucet)