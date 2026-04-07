import turtle

def stvorce(n, a):
    if n == 0:
        pass
    else:
        for i in range(4):
            t.fd(a)
            t.rt(90)
            stvorce(n - 1, a / 3)
            # skúste: stvorce(n - 1, a * 0.45)

turtle.delay(0)
t = turtle.Turtle()
stvorce(4, 300)