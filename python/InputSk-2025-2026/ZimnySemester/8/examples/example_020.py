import turtle

turtle.delay(0)
t = turtle.Turtle()
for uhol in range(1, 2000):
    t.fd(8)
    t.rt(uhol + 0.1)
turtle.done()