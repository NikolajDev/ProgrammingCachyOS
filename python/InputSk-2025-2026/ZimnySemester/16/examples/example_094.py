def urob(n):
    if n < 1:
        yield 0
    else:
        yield n
        yield from urob(n-1)
        yield n