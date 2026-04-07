from struktury import Queue

def zdvoj_subor(meno_suboru):
    queue = Queue()
    with open(meno_suboru) as subor:
        for riadok in subor:
            queue.enqueue(riadok)
    with open(meno_suboru, 'a') as subor:
        while not queue.is_empty():
            subor.write(queue.dequeue())

zdvoj_subor('text.txt')