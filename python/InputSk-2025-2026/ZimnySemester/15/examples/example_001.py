class EmptyError(Exception): pass

class Stack:

    def __init__(self):
        '''inicializuje zoznam'''
        self._prvky = []

    def push(self, data):
        '''na vrch zásobníka vloží novú hodnotu'''
        self._prvky.append(data)

    def pop(self):
        '''z vrchu zásobníka vyberie hodnotu, alebo vyvolá EmptyError'''
        if self.is_empty():
            raise EmptyError('prazdny zasobnik')
        return self._prvky.pop()

    def top(self):
        '''z vrchu zásobníka vráti hodnotu, alebo vyvolá EmptyError'''
        if self.is_empty():
            raise EmptyError('prazdny zasobnik')
        return self._prvky[-1]

    def is_empty(self):
        '''zistí, či je zásobník prázdny'''
        return self._prvky == []