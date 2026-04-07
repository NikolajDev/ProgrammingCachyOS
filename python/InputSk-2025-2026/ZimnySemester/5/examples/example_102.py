>>> m = 'Guido van Rossum'
>>> m.split()                    # vytvorí postupnosť reťazcov
    ['Guido', 'van', 'Rossum']
>>> a, b, c = m.split()
>>> a
    'Guido'
>>> b
    'van'
>>> c
    'Rossum'
>>> for slovo in m.split():
...     print('<' + slovo + '>')
    <Guido>
    <van>
    <Rossum>