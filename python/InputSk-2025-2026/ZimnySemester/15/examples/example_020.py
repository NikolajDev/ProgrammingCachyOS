def prefix(vyraz):
    s = Stack()
    for prvok in reversed(vyraz.split()):
        if prvok == '+':
            s.push(s.pop() + s.pop())
        elif prvok == '-':
            s.push(s.pop() - s.pop())
        elif prvok == '*':
            s.push(s.pop() * s.pop())
        elif prvok == '/':
            s.push(s.pop() // s.pop())
        else:
            s.push(int(prvok))
    return s.pop()