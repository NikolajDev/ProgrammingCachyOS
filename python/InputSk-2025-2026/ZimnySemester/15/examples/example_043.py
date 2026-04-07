s = Stack()
for i in ...:
    s.push(i)
    s.push(i + 1)
while not s.is_empty():
    print(s.pop(), end=' ')