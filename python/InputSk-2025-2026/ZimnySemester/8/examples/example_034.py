import turtle

turtle.delay(0)
zoznam = []
for i in range(60):
    zoznam.append(turtle.Turtle())
    zoznam[-1].seth(i * 6)

for t in zoznam:
    t.fd(200)
turtle.done()