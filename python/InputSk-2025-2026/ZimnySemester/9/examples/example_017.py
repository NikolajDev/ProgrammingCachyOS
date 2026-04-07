def spir(d):
    if d > 100:
        t.pencolor('red')     # a skonči
    else:
        t.fd(d)
        t.lt(60);
        spir(d + 3)
        t.fd(d)
        t.lt(60)

spir(1)