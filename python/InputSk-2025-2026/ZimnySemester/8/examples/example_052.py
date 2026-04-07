import turtle
t = turtle.Turtle()
t.speed(0)
t.fd(100)
for repc in range(1, 11):
    t.pencolor('red')
    for repc in range(1, repc+1):
        pass
    t.lt(30)
    t.fd(repc*10)
t.pu()
turtle.done()