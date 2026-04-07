>>> for x, y in (30, 50), (60, 100), (70, 120):
...     print(f'x = {x}, y = {y}')
    x = 30, y = 50
    x = 60, y = 100
    x = 70, y = 120
>>> for x, y, farba in (30, 50, 'red'), (60, 100, 'blue'), (70, 120, 'pink'):
...     print(f'x = {x}, y = {y}, farba = {farba!r}')
    x = 30, y = 50, farba = 'red'
    x = 60, y = 100, farba = 'blue'
    x = 70, y = 120, farba = 'pink'