>>> def podm(x):               # zistí, či je číslo párne
...     return x % 2 == 0
>>> list(range(1, 20, 3))
    [1, 4, 7, 10, 13, 16, 19]
>>> mapuj(podm, range(1, 20, 3))
    [False, True, False, True, False, True, False]
>>> filtruj(podm, range(1, 20, 3))
    [4, 10, 16]