nums = '4, 50, 20'
x, y, z = 0, 0, 0
colors = 'green, blue, maroon'
c1, c2, c3 = "", "", ""


help = ""

for i in nums:
    if i == ",":
        x = int(help)
        help = ""
        x, y = y, x
    else:
        help += i
        
z = int(help)

print(type(x), type(y), type(z))
print(x, y, z)


help = ""

for i in colors:
    if i == ",":
        c1 = help
        help = ""
        c1, c2 = c2, c1
    elif i == " ":
        continue
    else:
        help += i
        
c3 = help

print(type(c1), type(c2), type(c3))
print(c1, c2, c3)