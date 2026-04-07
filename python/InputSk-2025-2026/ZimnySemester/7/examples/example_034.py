import tkinter

def test_vlavo(event):
    print('šípka vľavo')

def test_a(event):
    print('stlačil si kláves a')

def test_F1(event):
    print('F1')

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind_all('a', test_a)
canvas.bind_all('<Left>', test_vlavo)
canvas.bind_all('<KeyPress-F1>', test_F1)

tkinter.mainloop()