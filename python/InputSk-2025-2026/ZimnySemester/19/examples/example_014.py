def fun1(n):
    x = 0
    for i in range(n):
        x += 1
    return x

def fun2(n):
    x = 0
    for i in range(n):
        for j in range(i):
            x += 1
    return x

def fun3(n):
    if n == 0: return 1
    x = 0
    for i in range(n):
        x += fun3(n-1)
    return x

def fun4(n):
    if n == 0: return 0
    return fun4(n//2) + fun1(n) + fun4(n//2)

def fun5(n):
    x, i = 0, n
    while i > 0:
        x += fun1(i)
        i //= 2
    return x

def fun6(n):
    if n == 0: return 1
    return fun6(n-1) + fun6(n-1)

def fun7(n):
    if n == 1: return 0
    return 1 + fun7(n//2)