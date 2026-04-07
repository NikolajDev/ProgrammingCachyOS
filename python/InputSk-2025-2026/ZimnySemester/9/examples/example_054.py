import turtle

def stvorce(n, d):
    if n > 0:
        for i in range(4):
            t.fd(d)
            t.rt(90)
            t.lt(30)
            stvorce(n - 1, d / 3)
            t.rt(30)

turtle.delay(0)
t = turtle.Turtle()
t.speed(0)
stvorce(5, 300)