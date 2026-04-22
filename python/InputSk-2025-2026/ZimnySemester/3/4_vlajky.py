# """
# Napíš program s funkciou vlajky((), ktorá nakreslí vlajky týchto štátov: Nemecko, Taliansko, Francúzsko a Ukraina. Všetky nech majú rozmery 135 x 90. Volanie vlajky((), nakreslí (všimni si, že medzi farebnými pruhmi nie je čierna čiara):
# """

# from tkinter import Canvas, mainloop

# # Thinking 

# # if we have a constant size of the flag we can split it by 3 if the flag has three color if the colors are in columns we divide the width by the number of color e.g. Italy 3 colors 135 / 3 if the colors are in row we divide the height by the number of color e.g. Germany 90 / 3. Then as we can see there is not a line between the colors so we use outline="0"

# def vlajky():
#     canvas = Canvas(width=600, height=600)
#     canvas.pack()
#     # Germany
#     x = 50
#     y = 50
#     w = 135
#     h = 90
#     y_copy = y
#     colorh = h / 3
#     color1, color2, color3 = "black", "red", "yellow"
#     for i in range(3):
#         canvas.create_rectangle(x, y_copy, x + w, y_copy + colorh, fill=color1, width=0)
#         color1, color2, color3 = color2, color3, color1
#         y_copy += colorh
#     canvas.create_rectangle(x, y, x + w, y + h)
    
#     # Italy
#     x = 220
#     y = 50
#     w = 135
#     h = 90
#     colorw = w / 3
#     color1, color2, color3 = "green", "white", "red"
#     x_copy = x
#     for i in range(3):
#         canvas.create_rectangle(x_copy, y, x_copy + colorw, y + h, fill=color1, width=0)
#         color1, color2, color3 = color2, color3, color1
#         x_copy += colorw
#     canvas.create_rectangle(x, y, x + w, y + h)

#     # France
#     x = 50
#     y = 180
#     w = 135
#     h = 90
#     colorw = w / 3
#     color1, color2, color3 = "blue", "white", "red"
#     x_copy = x
#     for i in range(3):
#         canvas.create_rectangle(x_copy, y, x_copy + colorw, y + h, fill=color1, width=0)
#         color1, color2, color3 = color2, color3, color1
#         x_copy += colorw
#     canvas.create_rectangle(x, y, x + w, y + h)

#     #Ukraine
#     x = 220
#     y = 180
#     w = 135
#     h = 90
#     y_copy = y
#     colorh = h / 2
#     color1, color2 = "blue", "yellow"
#     for i in range(2):
#         canvas.create_rectangle(x, y_copy, x + w, y_copy + colorh, fill=color1, width=0)
#         color1, color2 = color2, color1
#         y_copy += colorh
#     canvas.create_rectangle(x, y, x + w, y + h)
    

# vlajky()
# mainloop()


# # If you are Advanced here is also how it can looks like, but with the knowledge you have from the course this should not be a solution:

"""
You can try this solution if you don't understand it, don't be sad we will cover this later and maybe we will look back at it
"""

"""
from tkinter import Canvas, mainloop
def vlajky():
    canvas = Canvas(width=600, height=600)
    canvas.pack()
    for x, y, colors, sw, sh, dx, dy in (
        (50, 50, ("black", "red", "yellow"), 135, 30, 0, 30),
        (220, 50, ("green", "white", "red"), 45, 90, 45, 0),
        (50, 180, ("blue", "white", "red"), 45, 90, 45, 0),
        (220, 180, ("blue", "yellow"), 135, 45, 0, 45)
    ):
        for i in range(len(colors)):
            canvas.create_rectangle(x + i*dx, y + i*dy, x + i*dx + sw, y + i*dy + sh, fill=colors[i], width=0)
        canvas.create_rectangle(x, y, x + 135, y + 90)

vlajky()
mainloop()
"""