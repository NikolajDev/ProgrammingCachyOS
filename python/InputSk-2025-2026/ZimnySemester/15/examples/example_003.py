s = Stack()
for slovo in 'Anicka dusicka kde si bola'.split():
    s.push(slovo)
print('na vrchu zasobnika:', s.top())
while not s.is_empty():
    print(s.pop())
print('zasobnik je prazdny:', s.is_empty())
print('vyberame:', s.pop())