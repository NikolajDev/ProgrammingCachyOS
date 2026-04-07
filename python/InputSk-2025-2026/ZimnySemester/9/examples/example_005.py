import turtle

def xy(d):
    t.fd(d)
    t.lt(60)
    xy(d + 0.3)

turtle.delay(0)
t = turtle.Turtle()
t.speed(0)
xy(1)