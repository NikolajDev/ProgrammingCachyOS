>>> [1, 2, 5, 3, 4] > [1, 2, 4, 8, 1000]
    True
>>> [1000, 2000, 3000] < [1000, 2000, 3000, 0, 0]
    True
>>> [1, 'ahoj'] == ['ahoj', 1]
    False
>>> [1, 'ahoj'] < ['ahoj', 1]
    ...
    TypeError: '<' not supported between instances of 'int' and 'str'