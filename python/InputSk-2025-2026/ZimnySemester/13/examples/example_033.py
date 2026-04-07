import turtle

class MojaTurtle(turtle.Turtle):
    def strom(self, d):
        self.fd(d)
        if d > 10:
            self.lt(40)
            self.strom(d * .6)
            self.rt(90)
            self.strom(d * .7)
            self.lt(50)
        self.fd(-d)

t = MojaTurtle()
t.lt(90)
t.strom(100)