>>> max(3, 7, 11, 4)
    11
>>> max(3, 7, 11, 4, key=lambda x: -x)
    3
>>> max([3, 7, 11, 4], key=str)
    7