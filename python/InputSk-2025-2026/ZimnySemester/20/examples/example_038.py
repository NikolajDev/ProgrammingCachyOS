import random

for i in range(500):
    xy = random.randrange(200, 300), random.randrange(50, 150)
    farba = (255, 0, 0)
    obr1.putpixel(xy, farba)