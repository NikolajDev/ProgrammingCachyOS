def rekurzia(n):
    stack = Stack()
    stack.push((1, n))
    while not stack.is_empty():
        adresa, n = stack.pop()
        if adresa == 1:
            if n == 0:
                print('.', end=' ')    # triviálny prípad
            else:
                stack.push((2, n))
                stack.push((1, n - 1))
        elif adresa == 2:
                print(n, end=' ')
                #stack.push((3, n))
                stack.push((1, n - 1))

rekurzia(3)
print('koniec')