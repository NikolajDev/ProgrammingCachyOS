>>> m = '  Guido\n   van  Rossum  \n'
>>> print(m)
      Guido
       van  Rossum

>>> a, b, c = m.split()
>>> a
    'Guido'
>>> b
    'van'
>>> c
    'Rossum'
>>> ' '.join(m.split())
    'Guido van Rossum'