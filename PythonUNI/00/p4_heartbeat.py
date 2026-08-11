from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed


# Implementujte proceduru ‹heartbeat›, která vykreslí stylizovanou
# křivku EKG. Parametr ‹iterations› udává počet tepů, které
# procedura vykreslí. Zbylé parametry zadávají amplitudu základního
# úderu a periodu slabšího úderu. Slabší úder má poloviční
# amplitudu.  Například při periodě 3 bude mít sníženou amplitudu
# každý třetí úder, počínaje prvním.

def heartbeat(amplitude, period, iterations):
    pass


def main():
    speed(4)
    heartbeat(30, 3, 5)
    done()


if __name__ == "__main__":
    main()
