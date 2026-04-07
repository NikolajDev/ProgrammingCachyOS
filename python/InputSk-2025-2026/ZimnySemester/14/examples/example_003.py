import turtle

class MojaTurtle(turtle.Turtle):
    def domcek(self, dlzka):
        for uhol in 90, 90, 90, 30, 120, -60:
            self.fd(dlzka)       # fd z triedy ??? Turtle
            self.rt(uhol)        # rt z triedy Turtle

class MojaTurtle1(MojaTurtle):
    def fd(self, dlzka):
        while dlzka >= 5:
            self.lt(60)
            super().fd(5)        # fd z triedy Turtle
            self.rt(120)
            super().fd(5)        # fd z triedy Turtle
            self.lt(60)
            dlzka -= 5
        super().fd(dlzka)        # fd z triedy Turtle

t = MojaTurtle1()
t.domcek(100)