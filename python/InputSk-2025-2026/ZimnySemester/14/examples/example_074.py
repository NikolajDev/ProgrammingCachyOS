>>> rgb(100, 150, 20.0)
    ...
    AssertionError: chybny treti parameter b
>>> rgb(100, 350, 20.0)
    ...
    AssertionError: chybny druhy parameter g
>>> rgb('100', 350, 20.0)
    ...
    AssertionError: chybny prvy parameter r
>>> rgb(100, 150, 200)
    '#6496c8'