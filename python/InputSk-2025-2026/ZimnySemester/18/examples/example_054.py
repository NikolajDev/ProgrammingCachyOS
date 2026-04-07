>>> zoz = ['abc', 3.14, 'def', 2.71, 'ghi', 333, 'jkl', 22]
>>> sorted(zoz)
    TypeError: unorderable types: float() < str()
>>> sorted(zoz, key=str)
    [2.71, 22, 3.14, 333, 'abc', 'def', 'ghi', 'jkl']