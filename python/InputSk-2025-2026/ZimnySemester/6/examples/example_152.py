with open('subor.txt', 'r') as r:
    with open('subor2.txt', 'w') as w:
        w.write(r.read())