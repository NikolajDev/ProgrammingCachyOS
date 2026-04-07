import turtle

def strom(n, d):
    t.fd(d)
    if n > 0:
        t.lt(40)
        strom(n - 1, d * 0.7)
        t.rt(75)
        strom(n - 1, d * 0.6)
        t.lt(35)
    t.bk(d)

t = turtle.Turtle()
t.lt(90)
strom(5, 80)