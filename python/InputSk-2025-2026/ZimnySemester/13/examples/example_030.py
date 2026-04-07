import turtle

class MojaTurtle(turtle.Turtle):
    def stvorec(self, velkost):
        for i in range(4):
            self.fd(velkost)
            self.rt(90)

t = MojaTurtle()
t.stvorec(100)
t.lt(30)
t.stvorec(200)