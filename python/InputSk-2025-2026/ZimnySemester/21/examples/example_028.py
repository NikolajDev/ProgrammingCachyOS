def klik(self, event):
    self.azoz.append(Anim(event.x, event.y, random.choice(self.zoz),
                          random.randint(50, 300)))