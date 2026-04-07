import turtle

def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)

t = turtle.Turtle()
t.pensize(5)
t.fillcolor('red')
t.begin_fill()
stvorec(100)
t.end_fill()
turtle.done()