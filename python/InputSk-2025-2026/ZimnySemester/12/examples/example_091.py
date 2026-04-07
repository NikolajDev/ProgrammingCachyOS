class Test:
    z = 300

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f'Test({self.x}, {self.y}, {self.z})'