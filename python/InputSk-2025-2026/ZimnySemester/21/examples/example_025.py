def timer(self):
    for a in self.azoz:
        a.dalsia_faza()
    self.canvas.after(100, self.timer)