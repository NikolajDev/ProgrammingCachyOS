def fib(n, pamat={}):
    if n in pamat:
        return pamat[n]
    if n < 2:
        vysl = n
    else:
        vysl = fib(n - 2) + fib(n - 1)
    pamat[n] = vysl
    return vysl