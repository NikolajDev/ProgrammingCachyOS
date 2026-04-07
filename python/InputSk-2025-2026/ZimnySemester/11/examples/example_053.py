>>> mnozina = {'behat', 'ucit sa', 'upratat'}
>>> mnozina
    {'upratat', 'behat', 'ucit sa'}
>>> zoznam = list(mnozina)
>>> zoznam
    ['upratat', 'behat', 'ucit sa']
>>> ntica = tuple(mnozina)
>>> ntica
    ('upratat', 'behat', 'ucit sa')
>>> for prvok in mnozina:
...     print(prvok, end=', ')
    'upratat', 'behat', 'ucit sa',