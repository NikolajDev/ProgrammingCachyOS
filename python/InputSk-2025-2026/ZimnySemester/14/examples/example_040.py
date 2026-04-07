if existuje('x.txt'):
    with open('x.txt') as t:
        obsah = t.read()
else:
    obsah = ''