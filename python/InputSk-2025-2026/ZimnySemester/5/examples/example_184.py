>>> for i in 10 * (1,):
...     print(i, end=' ')
    1 1 1 1 1 1 1 1 1 1
>>> for i in 10 * (1, 2):
...      print(i, end=' ')
    1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
>>> for i in 10 * tuple(range(10)):
...      print(i, end=' ')
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
    1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2
    3 4 5 6 7 8 9
>>> for z in 'Python':
...     print(z, end=' ')
    P y t h o n
>>> for z in 'Python',:
...     print(z, end=' ')
    Python
>>> for i in 123,:
...     print(i, end=' ')
    123
>>> for i in 123:
...     print(i, end=' ')
    ...
    TypeError: 'int' object is not iterable