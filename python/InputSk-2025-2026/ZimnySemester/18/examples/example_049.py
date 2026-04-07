>>> m = {'Janko Hrasko', 'Eugen Suchon', 'Ludovit Stur', 'Andrej Sladkovic', 'Janko Stur'}
>>> sorted(m)
    ['Andrej Sladkovic', 'Eugen Suchon', 'Janko Hrasko', 'Janko Stur', 'Ludovit Stur']
>>> sorted(m, key=lambda x: x.split()[::-1])
    ['Janko Hrasko', 'Andrej Sladkovic', 'Janko Stur', 'Ludovit Stur', 'Eugen Suchon']