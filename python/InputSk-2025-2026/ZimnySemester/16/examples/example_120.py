>>> def f(x, y): return x * y
>>> map2(f, 'python', range(1, 6))
    ['p', 'yy', 'ttt', 'hhhh', 'ooooo']
>>> map2(f, ('a', 4, (1, 2)), [3, 5, 2])
    ['aaa', 20, (1, 2, 1, 2)]