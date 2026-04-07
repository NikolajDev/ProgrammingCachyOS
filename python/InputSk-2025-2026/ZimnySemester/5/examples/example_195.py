>>> 5 < 'a'
    ...
    TypeError: unorderable types: int() < str()
>>> (1, 5, 10) < (1, 'a', 10)
    ...
    TypeError: unorderable types: int() < str()
>>> (1, 5, 10) != (1, 'a', 10)
    True