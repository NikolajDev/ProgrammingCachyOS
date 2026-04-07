>>> sustavy('11')
    [11, None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
>>> sustavy('1a1')
    [None, None, None, None, None, None, None, None, None, None, None, 232, 265, 300, 337, 376, 417]
>>> sustavy('FF')
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 255]
>>> sustavy('x')
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]