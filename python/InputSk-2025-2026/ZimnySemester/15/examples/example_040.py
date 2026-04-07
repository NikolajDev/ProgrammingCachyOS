from struktury import Queue

def pocet(rad):
    pom = Queue()
    vysl = 0
    while not rad.is_empty():
        pom.enqueue(rad.dequeue())
        vysl += 1
    while not pom.is_empty():
        rad.enqueue(pom.dequeue())
    return vysl