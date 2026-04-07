>>> ret = input('zadaj 2 čísla: ')
    zadaj 2 čísla: 15 999
>>> zoz = ret.split()
>>> zoz
    ['15', '999']
>>> a, b = zoz
>>> ai, bi = int(zoz[0]), int(zoz[1])
>>> a, b, ai, bi
    ('15', '999', 15, 999)