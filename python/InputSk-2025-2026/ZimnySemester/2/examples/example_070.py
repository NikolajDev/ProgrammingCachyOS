import random

def r():
    return random.randint(1, 6)

def t():
    suc = 0
    for i in range(r()):
        suc += r()
    return suc