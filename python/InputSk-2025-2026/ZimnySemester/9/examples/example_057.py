import turtle

def vlocka(n, d):
    if n == 0:
        t.fd(d)
    else:
        vlocka(n - 1, d / 3)
        t.lt(60)
        vlocka(n - 1, d / 3)
        t.rt(120)
        vlocka(n - 1, d / 3)
        t.lt(60)
        vlocka(n - 1, d / 3)

def sneh_vlocka(n, d):
    for i in range(3):
        vlocka(n, d)
        t.rt(120)

turtle.delay(0)
t = turtle.Turtle()
#t.speed(0)
t.lt(120)
for i in range(5):
    sneh_vlocka(i, 300)