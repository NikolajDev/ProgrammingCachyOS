def min2(a, b):
    if a < b:
        return a
    return b

def min(a, b, c):
    return min2(min2(a, b), c)