>>> abc = 'Monty Python'
>>> abc[3]
   't'
>>> abc[9]
   'h'
>>> abc[12]
    ...
    IndexError: string index out of range
>>> abc[len(abc) - 1]
    'n'