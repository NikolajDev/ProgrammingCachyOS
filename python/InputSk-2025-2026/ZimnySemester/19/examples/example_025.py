def test1(n):
    i, j = 1, 0
    while i < n:
        j += i
        i += 1
    return j

def test2(n):
    i, j = 1, 0
    while i < n:
        j += i
        i += i
    return j