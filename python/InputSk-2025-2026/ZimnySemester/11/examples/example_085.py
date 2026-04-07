>>> pretypuj('str', 3.14)
    '3.14'
>>> pretypuj('set', 'Python')
    {'t', 'y', 'P', 'h', 'o', 'n'}
>>> pretypuj('float', '1e5')
    100000.0
>>> pretypuj('dict', [(1, 'a'), (2, 'b')])
    {1: 'a', 2: 'b'}
>>> pretypuj('novy', 123)
    ...
    KeyError: 'novy'