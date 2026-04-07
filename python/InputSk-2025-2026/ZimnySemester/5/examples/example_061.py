>>> abc = list('Python')
>>> abc
    ['P', 'y', 't', 'h', 'o', 'n']
>>> abc[2:2]                                     # rez dĺžky 0
    []
>>> abc[2:2] = ['dve', 'slova']                  # rez dĺžky 0 sa nahradí dvomi prvkami
>>> abc
    ['P', 'y', 'dve', 'slova', 't', 'h', 'o', 'n']