>>> zoz = list(range(0, 110, 10))
>>> zoz
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> zoz[3:6] = ['begin', 'end']                  # tri prvky sa nahradili dvomi
>>> zoz
    [0, 10, 20, 'begin', 'end', 60, 70, 80, 90, 100]