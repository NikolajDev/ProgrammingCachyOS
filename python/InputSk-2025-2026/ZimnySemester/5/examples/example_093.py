>>> abc = ['raz', 'dva', 'tri', 'styri']
>>> abc.pop(7)
    ...
    IndexError: pop index out of range
>>> abc.pop(-1)                      # to isté ako abc.pop()
    'styri'
>>> abc.pop(0)                       # vyhadzuje prvý prvok
    'raz'
>>> abc
    ['dva', 'tri']
>>> abc.pop(1)
    'tri'
>>> abc.pop(0)
    'dva'
>>> abc.pop(0)
    ...
    IndexError: pop from empty list
>>> abc
    []