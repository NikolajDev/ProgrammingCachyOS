>>> aplikuj(float, int, str, '-314159e-3')
    '-314'
>>> def rev(x): return x[::-1]
>>> aplikuj(str, rev, int, 1074)
    4701
>>> aplikuj(abs, lambda x: x+7, -17)
    24