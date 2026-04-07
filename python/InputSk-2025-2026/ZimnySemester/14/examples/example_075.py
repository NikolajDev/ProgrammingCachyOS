>>> int('1101')
    1101
>>> int('1101', 2)      # dvojkova sustava
    13
>>> int('1101', 3)
    37
>>> int('1101', 16)
    4353
>>> int('3a')
    ...
    ValueError: invalid literal for int() with base 10: '3a'
>>> int('3a', 11)
    43
>>> int('3a', 16)
    58