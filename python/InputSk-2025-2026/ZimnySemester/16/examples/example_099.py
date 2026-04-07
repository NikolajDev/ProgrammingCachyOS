>>> zoznam = [i for i in range(20) if i%7 in [2,3,5]]
>>> zoznam
    [2, 3, 5, 9, 10, 12, 16, 17, 19]
>>> mn = {i for i in range(20) if i%7 in [2,3,5]}
>>> mn
    {2, 3, 5, 9, 10, 12, 16, 17, 19}
>>> ntica = tuple(i for i in range(20) if i%7 in [2,3,5])
>>> ntica
    (2, 3, 5, 9, 10, 12, 16, 17, 19)