class AsocPole:
    ...
    def vypis(self):
        for i, bucket in enumerate(self.tab):
            if bucket:
                print(i, *bucket)

a = AsocPole()
for i in range(1, 31):
    a[str(i)] = i ** 2
a.vypis()