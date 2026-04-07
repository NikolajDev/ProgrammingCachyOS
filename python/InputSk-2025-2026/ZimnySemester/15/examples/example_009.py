def palindrom(post):
    stack = []                    # Stack()
    for prvok in post:
        stack.append(prvok)       # push(prvok)
    for prvok in post:
        if prvok != stack.pop():  # pop()
            return False
    return True