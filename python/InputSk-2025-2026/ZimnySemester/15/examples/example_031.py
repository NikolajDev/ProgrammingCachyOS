def rekurzia(n):

# inicializácia zásobníka
    stack = Stack()
    stack.push((1, n))

    while not stack.is_empty():
        adresa, n = stack.pop()

        # prvá časť
        if adresa == 1:
            if n == 0:
                print('.', end=' ')    # triviálny prípad
            else:
                # rekurzia(n - 1)      # <--- volanie funkcie
                stack.push((2, n))
                stack.push((1, n - 1))

        # druhá časť
        elif adresa == 2:
                # návratové miesto
                print(n, end=' ')
                # rekurzia(n - 1)      # <--- volanie funkcie
                stack.push((3, n))
                stack.push((1, n - 1))

        # tretia časť
        elif adresa == 3:
                # návratové miesto
                pass