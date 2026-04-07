>>> deli = delitele(24)
>>> print(deli)
    (1, 2, 3, 4, 6, 8, 12, 24)
>>> if 2 in deli:
...     print('parne')
    parne
>>> print('sucet delitelov =', sum(deli))
    sucet delitelov = 60
>>> print('je prvocislo =', len(delitele(int(input('zadaj cislo: '))))==2)
    zadaj cislo: 11213
    je prvocislo = True
>>> print('je prvocislo =', len(delitele(int(input('zadaj cislo: '))))==2)
    zadaj cislo: 1001
    je prvocislo = False