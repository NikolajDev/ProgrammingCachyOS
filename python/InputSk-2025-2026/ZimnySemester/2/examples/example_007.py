import math

for uhol in range(0, 91, 5):
    uhol_v_radianoch = math.radians(uhol)
    sin_uhla = math.sin(uhol_v_radianoch)
    cos_uhla = math.cos(uhol_v_radianoch)
    print(uhol, sin_uhla, cos_uhla)