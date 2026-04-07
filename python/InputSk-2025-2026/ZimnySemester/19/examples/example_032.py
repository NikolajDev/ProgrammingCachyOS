class Robot:
    def __init__(self, meno_suboru):
        ...

    def __repr__(self):
        return ''

    def daj_robot(self):
        return ...

    def zmen_robot(self, poloha):
        ...

    robot = property(daj_robot, zmen_robot)

    def poloz(self, *poloha):
        ...

    def pohyb(self, prikazy):
        return ...