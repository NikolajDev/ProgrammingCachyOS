import turtle

def ldrak(n, s):
    if n == 0:
        t.fd(s)
    else:
        ldrak(n - 1, s)
        t.lt(90)
        pdrak(n - 1, s)

def pdrak(n, s):
    if n == 0:
        t.fd(s)
    else:
        ldrak(n - 1, s)
        t.rt(90)
        pdrak(n - 1, s)

turtle.delay(0)
t = turtle.Turtle()
t.speed(0)
t.ht()
ldrak(12, 6)