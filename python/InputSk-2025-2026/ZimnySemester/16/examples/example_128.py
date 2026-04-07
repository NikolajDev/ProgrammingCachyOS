>>> g = spoj(iter(range(5)), iter(range(10, 0, -2)))
>>> g
    <generator object spoj at 0x00A823C0>
>>> print(*g)
    0 1 2 3 4 10 8 6 4 2
>>> g = spoj(iter(range(5)), iter('ahoj'), iter(range(10, 0, -2)))
>>> print(*g)
    0 1 2 3 4 a h o j 10 8 6 4 2