>>> abc[6] = 'K'
    ...
    TypeError: 'str' object does not support item assignment
>>> novy = abc[:6] + 'K' + abc[7:]
>>> novy
    'Monty Kython'
>>> abc
    'Monty Python'