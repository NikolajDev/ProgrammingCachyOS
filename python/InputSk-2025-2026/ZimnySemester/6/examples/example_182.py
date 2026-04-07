>>> print('prvy\n druhy\n  treti\nstvrty', file=open('text.txt', 'w'))
>>> prevrat('text.txt')
>>> print(open('text.txt').read(), end='')
    stvrty
      treti
     druhy
    prvy
>>>