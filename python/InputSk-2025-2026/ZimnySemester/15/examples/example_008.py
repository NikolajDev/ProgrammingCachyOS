def palindrom(post):

    # vnorená definícia tried EmptyError a Stack

    class EmptyError(Exception): pass

    class Stack:

        def __init__(self):
            self._prvky = []

        def push(self, data):
            self._prvky.append(data)

        def pop(self):
            if self.is_empty():
                raise EmptyError('prazdny zasobnik')
            return self._prvky.pop()

        def top(self):
            if self.is_empty():
                raise EmptyError('prazdny zasobnik')
            return self._prvky[-1]

        def is_empty(self):
            return self._prvky == []

    # koniec vnorenej definície

    # tu pokračuje funkcia palindrom

    stack = Stack()           # používanie vnorenej definície
    for prvok in post:
        stack.push(prvok)
    for prvok in post:
        if prvok != stack.pop():
            return False
    return True