import turtle
import random

turtle.delay(0)
t = turtle.Turtle()
turtle.bgcolor('navy')
t.pensize(5)
t.pencolor('yellow')
for i in range(10000):
    t.seth(random.randint(0, 359))
    t.fd(10)
    if t.distance(40, 0) > 100 or t.distance(100, 0) < 100:
        t.fd(-10)
turtle.done()