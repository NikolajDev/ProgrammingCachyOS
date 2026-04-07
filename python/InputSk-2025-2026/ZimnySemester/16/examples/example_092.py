def test(n):
     yield from range(n+1)
     yield from range(n-1, -1, -1)       # alebo reversed(range(n))