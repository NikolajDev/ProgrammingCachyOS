import turtle

def strom(d):
    t.fd(d)
    if d > 5:
        t.lt(40)
        strom(d * 0.7)
        t.rt(75)
        strom(d * 0.6)
        t.lt(35)
    t.bk(d)

turtle.delay(0)
t = turtle.Turtle()
t.lt(90)
strom(80)