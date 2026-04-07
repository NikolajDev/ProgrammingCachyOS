>>> a = 'ahoj   \naj "apostrof" \' v texte  \n'
>>> print(a)
    ahoj
    aj "apostrof" ' v texte

>>> print(repr(a))
    'ahoj   \naj "apostrof" \' v texte  \n'
>>> print(f'{a!r}')                       # urobí _repr so zadanou hodnotou
    'ahoj   \naj "apostrof" \' v texte  \n'