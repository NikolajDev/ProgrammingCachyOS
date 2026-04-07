def vykonaj():
    t = turtle.Turtle()
    p = {'fd': t.fd, 'rt': t.rt, 'lt': t.lt}
    while True:
        prikaz, parameter = input('> ').split()
        p[prikaz](int(parameter))