>>> urob = (i for i in range(20) if i % 7 in [2, 3, 5])
>>> urob
    <generator object <genexpr> at 0x022A6760>
>>> list(urob)
    [2, 3, 5, 9, 10, 12, 16, 17, 19]