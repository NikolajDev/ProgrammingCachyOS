import turtle

class MojaTurtle(turtle.Turtle):
    def domcek(self, dlzka):
        for uhol in 90, 90, 90, 30, 120, -60:
            self.fd(dlzka)       # fd z triedy Turtle
            self.rt(uhol)        # rt z triedy Turtle

t = MojaTurtle()
t.domcek(100)