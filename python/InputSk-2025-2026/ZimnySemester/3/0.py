# Starter Code
import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=300, height=300)
canvas.pack()

# here we will put the code
# What objects are inside tkinter:
'''
canvas.create_text(...)           # write text we enter
canvas.create_rectangle(...)      # draws rectangle
canvas.create_oval(...)           # draws oval
canvas.create_line(...)           # draws line to point
canvas.create_polygon(...)        # draws polygon
canvas.create_image(...)          # draws png image
'''

canvas.create_text(150, 150, text='Programming in python')

root.mainloop()