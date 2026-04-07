def nsd(a, b):
    if a == b:
        return a
    if a > b:
        return nsd(b, a)
    return nsd(a, b - a)