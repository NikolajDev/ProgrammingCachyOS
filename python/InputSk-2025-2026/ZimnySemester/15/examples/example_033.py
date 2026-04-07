def rekurzia(n):
    stack = Stack()
    adresa = 1
    while True:
        if adresa == 1:
            if n == 0:
                print('.', end=' ')    # triviálny prípad
                if stack.is_empty():
                    break              # alebo return
                adresa, n = stack.pop()
            else:
                stack.push((2, n))
                adresa, n = 1, n - 1
        elif adresa == 2:
                print(n, end=' ')
                # stack.push((3, n))
                adresa, n = 1, n - 1