import turtle

def spir(d):
    if d > 100:
        pass     # nerob nič
    else:
        t.fd(d)
        t.lt(60)
        spir(d + 3)

turtle.delay(0)
t = turtle.Turtle()
t.speed(0)
spir(10)