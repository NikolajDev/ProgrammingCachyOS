>>> def delitele(n):
...     return tuple(i for i in range(1, n + 1) if n % i == 0)
>>> delitele(60)
    (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60)