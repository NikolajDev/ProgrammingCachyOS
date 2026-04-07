import turtle
import random

turtle.delay(0)
t = turtle.Turtle()
t.pensize(5)
t.pencolor('blue')
for i in range(10000):
    t.seth(random.randint(0, 359))
    t.fd(10)
    if t.xcor()**2 + t.ycor()**2 > 50**2:
        t.fd(-10)
turtle.done()