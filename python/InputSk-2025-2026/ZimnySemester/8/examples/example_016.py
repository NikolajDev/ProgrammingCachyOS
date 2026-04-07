import turtle

def obluk(d):
    for i in range(9):
        t.fd(d)
        t.rt(10)

def lupen(d):
    for i in 1, 2:
        obluk(d)
        t.rt(90)

def kvet(d, farby):
    for f in farby:
        t.fillcolor(f)
        t.begin_fill()
        lupen(d)
        t.end_fill()
        t.rt(360 / len(farby))

turtle.delay(0)
t = turtle.Turtle()
kvet(20, ['red', 'blue', 'yellow', 'magenta', 'green', 'orange', 'cyan])
turtle.done()