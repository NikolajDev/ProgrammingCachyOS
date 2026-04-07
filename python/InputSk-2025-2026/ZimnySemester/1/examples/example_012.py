>>> y = 4.3 * 10 ** 100          # velmi velke desatinne cislo
>>> y
    4.3e+100
>>> y ** 2
    1.849e+201
>>> y ** 3
    7.9507e+301
>>> y ** 4
    Traceback (most recent call last):
      File "<pyshell#7>", line 1, in <module>
        y ** 4
    OverflowError: (34, 'Result too large')