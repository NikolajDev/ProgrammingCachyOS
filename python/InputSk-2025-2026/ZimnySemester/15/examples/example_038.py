from struktury import Queue

queue = Queue()
for slovo in 'Anicka dusicka kde si bola'.split():
    queue.enqueue(slovo)
print('prvy v rade:', queue.front())
while not queue.is_empty():
    print(queue.dequeue())
print('rad je prazdny:', queue.is_empty())
print('vyberame:', queue.dequeue())