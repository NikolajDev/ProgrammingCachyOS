import turtle

def strom(n, d):
    t.fd(d)
    if n == 0:
        t.rt(90)
        t.fd(1)
        t.lt(90)
    else:
        t.lt(40)
        strom(n - 1, d * 0.67)
        t.rt(75)
        strom(n - 1, d * 0.67)
        t.lt(35)
    t.bk(d)

turtle.delay(0)
t = turtle.Turtle()
t.lt(90)
strom(6, 120)