from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, \
    setheading, done, speed


# Nakreslete rovnoramenný lichoběžník s délkami základen
# ‹base_length› a ‹top_length› a výškou ‹height› (lichoběžník je
# čtyřúhelník s jednou dvojicí rovnoběžných stran – základen –
# spojených rameny, které jsou obecně různoběžné).

def trapezoid(base_length, top_length, height):
    pass


def main():
    speed(4)
    trapezoid(100, 70, 70)

    penup()
    setheading(0)
    forward(150)
    pendown()

    trapezoid(120, 30, 35)

    done()


if __name__ == "__main__":
    main()
