if __name__ == '__main__':
    r = Robot('subor1.txt')
    print(r)
    r.robot = 1, 2
    print(f'{r.pohyb('3p2dl3h1p') = }')
    print(r)
    print('pozicia robota =', r.robot)
    print(f'{r.pohyb('dl2dp2hhp') = }')
    print(r)
    print(f'{r.poloz(1, 4, 1, 3) = }')
    print(f'{r.poloz(0, 5) = }')
    print(r)
    print(f'{r.pohyb('1d3l3l') = }')
    print(r)