import turtle
import random

def fun(pos):
    x, y = pos               # pos je dvojica súradníc
    if abs(x - 60) + abs(y) < 100:
        return False
    return abs(x + 60) + abs(y) > 100

turtle.delay(0)
t = turtle.Turtle()
t.speed(0)
t.pensize(5)
for i in range(10000):
    t.seth(random.randint(0, 359))
    if t.distance(0, 0) < 60:
        t.pencolor('green')
    else:
        t.pencolor('red')
    t.fd(10)
    if fun(t.pos()):       # funkcia fun stráži nejakú oblasť
        t.fd(-10)
turtle.done()