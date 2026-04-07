>>> zoz = ['prvý', 'druhý', 'tretí']
>>> zoz
    ['prvý', 'druhý', 'tretí']
>>> ''.join(zoz)
    'prvýdruhýtretí'
>>> '...'.join(zoz)
    'prvý...druhý...tretí'
>>> list(str(2021))
    ['2', '0', '2', '1']
>>> '.'.join(list(str(2021)))
    '2.0.2.1'
>>> '.'.join('Python')           # reťazec 'Python' je tu ako postupnosť znakov
    'P.y.t.h.o.n'