def test3(p):
    i = 1
    while i < len(p):
        sorted(p)
        i += i
    return p

def test4(p):
    i, n = 1, len(p)
    while i < n:
        if 2 * i >= n:
            sorted(p)
        i += i
    return p