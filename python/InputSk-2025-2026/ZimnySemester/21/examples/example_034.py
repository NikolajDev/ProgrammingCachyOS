if x + dx < vel:
    dx = abs(dx)
if x + dx > sirka - vel:
    dx = -abs(dx)
if y + dy < vel:
    dy = abs(dy)
if y + dy > vyska - vel:
    dy = -abs(dy)
x, y = x + dx, y + dy