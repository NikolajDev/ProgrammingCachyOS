canvas = tkinter.Canvas()
canvas.pack()

n = 11
t = vyrob(n, n)
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            t[i][j] = 2
    t[i][i] = t[i][n - 1 - i] = 3
kresli(t)

tkinter.mainloop()