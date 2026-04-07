class Plocha:
    ...

    def timer(self):
        teraz = time.time()
        for a in self.azoz:
            if a.time < teraz:
                a.dalsia_faza()
                a.time = teraz + a.tik
        self.canvas.after(20, self.timer)