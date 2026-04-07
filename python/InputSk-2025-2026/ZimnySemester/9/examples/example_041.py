def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

for i in range(15):
    print(fibonacci(i), end=', ')

print('\nfibonacci(100) =', fibonacci(100))