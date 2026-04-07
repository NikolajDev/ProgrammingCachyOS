import turtle
import random

def strom(n, d):
    t.pensize(2 * n + 1)
    t.fd(d)
    if n == 0:
        t.dot(10, 'green')
    else:
        uhol1 = random.randint(20, 40)
        uhol2 = random.randint(20, 60)
        t.lt(uhol1)
        strom(n - 1, d * random.randint(40, 70) / 100)
        t.rt(uhol1 + uhol2)
        strom(n - 1, d * random.randint(40, 70) / 100)
        t.lt(uhol2)
    t.bk(d)

turtle.delay(0)
t = turtle.Turtle()
t.lt(90)
t.pencolor('maroon')
strom(6, 150)