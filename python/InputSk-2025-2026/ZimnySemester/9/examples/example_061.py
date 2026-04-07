import turtle

def hilbert(n, s, u=90):
    if n > 0:
        t.lt(u)
        hilbert(n - 1, s, -u)
        t.fd(s)
        t.rt(u)
        hilbert(n - 1, s, u)
        t.fd(s)
        hilbert(n - 1, s, u)
        t.rt(u)
        t.fd(s)
        hilbert(n - 1, s, -u)
        t.lt(u)

turtle.delay(0)
t = turtle.Turtle()
t.speed(0)
t.ht()
hilbert(5, 7)          # vyskúšajte: hilbert(7, 2)