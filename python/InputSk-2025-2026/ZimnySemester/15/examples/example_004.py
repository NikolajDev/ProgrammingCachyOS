def palindrom(post):
    stack = Stack()
    for prvok in post:
        stack.push(prvok)
    for prvok in post:
        if prvok != stack.pop():
            return False
    return True