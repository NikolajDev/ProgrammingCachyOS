>>> sucet([2, '3', 4.0, 'päť'])
    9
>>> sucet(['1', 2, 0.3, 'abc'])
    '120.3abc'
>>> sucet([[1,2], 3, '4x'])
    [1, 2, '4', 'x']
>>> sucet([(1, 2), (3, 4), [5]])
    (1, 2, 3, 4, 5)
>>> print(sucet([]))     # pre prázdnu postupnosť
    None