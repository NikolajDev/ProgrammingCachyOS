>>> c = Cas(8, 35, 40)
>>> print(c.hodiny, c.minuty, c.sekundy)
    8 35 40
>>> c.minuty = 53
>>> print(c)
    8:53:40
>>> c.hodiny = 12
>>> print(c)
    12:53:40
>>> c.sekundy = 27
>>> print(c)
    12:53:27