def strom(n, d):
    stack = Stack()
    stack.push((1, n, d))
    while not stack.is_empty():
        adresa, n, d = stack.pop()
    # prvá časť
        if adresa == 1:
            t.fd(d)
            if n <= 0:
                t.bk(d)         # triviálny prípad
            else:
                t.lt(40)
                #strom(n - 1, d * 0.7)
                stack.push((2, n, d))
                stack.push((1, n - 1, d * 0.7))

    # druhá časť
        elif adresa == 2:
            t.rt(75)
            #strom(n - 1, d * 0.6)
            stack.push((3, n, d))
            stack.push((1, n - 1, d * 0.6))

    # tretia časť
        elif adresa == 3:
            t.lt(35)
            t.bk(d)