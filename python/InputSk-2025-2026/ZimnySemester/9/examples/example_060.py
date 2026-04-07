import turtle

def drak(n, s, u=90):
    if n == 0:
        t.fd(s)
    else:
        drak(n - 1, s, 90)
        t.lt(u)
        drak(n - 1, s, -90)

turtle.delay(0)
t = turtle.Turtle()
t.speed(0)
t.ht()
drak(14, 2)