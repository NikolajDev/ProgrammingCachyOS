from math import sin, radians

for uhol in range(0, 361, 10):
    print(' ' * int(sin(radians(uhol)) * 35 + 40) + 'SIN')