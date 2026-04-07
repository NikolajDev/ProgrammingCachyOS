>>> a = 10
>>> b = 7
>>> a < b
    False
>>> a >= b + 3
    True
>>> b < a < 2 * b
    True
>>> a != 7 and b == a - 3
    True
>>> a == 7 or b == 10
    False
>>> not a == b          # to isté ako  a != b
    True
>>> 1 == '1'
    False
>>> 1 < '2'             # nemôžeme takto porovnaváť čísla a znaky
    ...
    TypeError: unorderable types: int() < str()