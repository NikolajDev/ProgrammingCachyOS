def fibonacci(n):
    global pocet
    pocet += 1
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

pocet = 0
print('fibonacci(15) =', fibonacci(15))
print('pocet volani funkcie =', pocet)
pocet = 0
print('fibonacci(16) =', fibonacci(16))
print('pocet volani funkcie =', pocet)