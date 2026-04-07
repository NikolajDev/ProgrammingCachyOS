>>> def cs(n):                     # cs() vypočíta ciferný súčet
...     return sum([int(znak) for znak in str(n)])
>>> [i for i in range(100) if cs(i) == 5]
    [5, 14, 23, 32, 41, 50]