>>> t1 = do_dvojrozmernej(range(10), 3)
>>> vypis(t1)
       0    1    2
       3    4    5
       6    7    8
       9
>>> t2 = do_dvojrozmernej(do_radu(t1), 5)
>>> vypis(t2)
       0    1    2    3    4
       5    6    7    8    9
>>> vypis(do_dvojrozmernej('programovanie', 5))
     'p'  'r'  'o'  'g'  'r'
     'a'  'm'  'o'  'v'  'a'
     'n'  'i'  'e'