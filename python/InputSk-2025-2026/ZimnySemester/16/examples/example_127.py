>>> g = zdvoj(i**2 for i in range(1, 5))
>>> g
    <generator object zdvoj at 0x022A6828>
>>> list(g)
    [1, 1, 4, 4, 9, 9, 16, 16]
>>> zdvoj('Python')
    ...
>>> zdvoj([2, 3, 5])
    ...