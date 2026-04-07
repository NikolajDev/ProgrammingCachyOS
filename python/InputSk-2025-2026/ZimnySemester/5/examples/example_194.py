>>> prvo = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
>>> prvo[5]
    13
>>> prvo = prvo[:5] + ('fuj',) + prvo[5:]
>>> prvo
    (2, 3, 5, 7, 11, 'fuj', 13, 17, 19, 23, 29)
>>> prvo[2] = 'haha'
    ...
    TypeError: 'tuple' object does not support item assignment