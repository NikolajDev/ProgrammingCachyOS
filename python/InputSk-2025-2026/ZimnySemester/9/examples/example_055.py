import turtle

def trojuholniky(n, a):
    if n > 0:
        for i in range(3):
            t.fd(a)
            t.lt(120)
            trojuholniky(n - 1, a / 2)

turtle.delay(0)
t = turtle.Turtle()
#t.speed(0)
trojuholniky(6, 300)