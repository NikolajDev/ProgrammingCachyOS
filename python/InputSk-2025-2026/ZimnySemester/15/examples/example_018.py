def postfix(vyraz):
    s = Stack()
    for prvok in vyraz.split():
        if prvok == '+':
            s.push(s.pop() + s.pop())
        elif prvok == '-':
            s.push(-s.pop() + s.pop())
        elif prvok == '*':
            s.push(s.pop() * s.pop())
        elif prvok == '/':
            op2 = s.pop()             # môžeme zapísať aj: op2, op1 = s.pop(), s.pop()
            op1 = s.pop()
            s.push(op1 // op2)
        else:
            s.push(int(prvok))
    return s.pop()