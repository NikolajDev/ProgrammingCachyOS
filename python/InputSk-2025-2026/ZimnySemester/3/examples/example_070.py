id1 = canvas.create_line(10, 20, 30, 40)
id2 = canvas.create_oval(10, 20, 30, 40)
canvas.create_text(100, 100, text='ahoj', tag='t')
canvas.create_rectangle(80, 90, 120, 110, fill='gray', tag='t')
...
canvas.delete(id1)
canvas.delete('t')