def fib(n):
    a, b = -1, 1
    while n > 0:
        a, b = b, a+b
        yield b
        n -= 1