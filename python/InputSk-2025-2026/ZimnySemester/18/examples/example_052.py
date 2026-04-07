>>> def vzd(x, y):
        return (x**2 + y**2)**.5
>>> import random
>>> body = [(random.randint(-5, 5), random.randint(-5, 5)) for i in range(10)]
>>> body
    [(-1, 5), (2, 3), (-1, 0), (-1, -2), (0, 1), (-4, 4), (-4, 4), (5, -1), (5, -2), (-5, 0)]
>>> sorted(body, key=lambda b: vzd(*b))
    [(-1, 0), (0, 1), (-1, -2), (2, 3), (-5, 0), (-1, 5), (5, -1), (5, -2), (-4, 4), (-4, 4)]