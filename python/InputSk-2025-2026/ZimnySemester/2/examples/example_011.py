import math

for uhol in range(0, 361, 10):
    print(' ' * int(math.sin(math.radians(uhol)) * 35 + 40) + 'SIN')