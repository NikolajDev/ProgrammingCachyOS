import tkinter as tk

win = tk.Tk()
win.title("say yes pls")
win.configure(bg="pink")

canvas = tk.Canvas(win, width=400, height=400, bg="pink", highlightthickness=0)
canvas.create_text(200, 80, text="Will you be\nmy valentine?", font=("Courier New", 20, "bold"), fill="red", justify="center")
canvas.pack()

def anko():
    canvas.after(0, lambda: canvas.create_rectangle(190, 190, 210, 210, fill="red", outline="red"))
    canvas.after(50, lambda: canvas.create_rectangle(210, 170, 230, 190, fill="red", outline="red"))
    canvas.after(100, lambda: canvas.create_rectangle(230, 150, 270, 170, fill="red", outline="red"))
    canvas.after(150, lambda: canvas.create_rectangle(250, 150, 270, 170, fill="red", outline="red"))
    canvas.after(200, lambda: canvas.create_rectangle(270, 170, 290, 190, fill="red", outline="red"))
    canvas.after(250, lambda: canvas.create_rectangle(290, 190, 310, 210, fill="red", outline="red"))
    canvas.after(300, lambda: canvas.create_rectangle(290, 210, 310, 230, fill="red", outline="red"))
    canvas.after(350, lambda: canvas.create_rectangle(290, 230, 310, 250, fill="red", outline="red"))
    canvas.after(400, lambda: canvas.create_rectangle(270, 250, 290, 270, fill="red", outline="red"))
    canvas.after(450, lambda: canvas.create_rectangle(250, 270, 270, 290, fill="red", outline="red"))
    canvas.after(500, lambda: canvas.create_rectangle(230, 290, 250, 310, fill="red", outline="red"))
    canvas.after(550, lambda: canvas.create_rectangle(210, 310, 230, 330, fill="red", outline="red"))
    canvas.after(600, lambda: canvas.create_rectangle(190, 330, 210, 350, fill="red", outline="red"))
    canvas.after(650, lambda: canvas.create_rectangle(170, 310, 190, 330, fill="red", outline="red"))
    canvas.after(700, lambda: canvas.create_rectangle(150, 290, 170, 310, fill="red", outline="red"))
    canvas.after(750, lambda: canvas.create_rectangle(130, 270, 150, 290, fill="red", outline="red"))
    canvas.after(800, lambda: canvas.create_rectangle(110, 250, 130, 270, fill="red", outline="red"))
    canvas.after(850, lambda: canvas.create_rectangle(90, 230, 110, 250, fill="red", outline="red"))
    canvas.after(900, lambda: canvas.create_rectangle(90, 210, 110, 230, fill="red", outline="red"))
    canvas.after(950, lambda: canvas.create_rectangle(90, 190, 110, 210, fill="red", outline="red"))
    canvas.after(1000, lambda: canvas.create_rectangle(110, 170, 130, 190, fill="red", outline="red"))
    canvas.after(1050, lambda: canvas.create_rectangle(130, 150, 150, 170, fill="red", outline="red"))
    canvas.after(1100, lambda: canvas.create_rectangle(150, 150, 170, 170, fill="red", outline="red"))
    canvas.after(1100, lambda: canvas.create_rectangle(170, 170, 190, 190, fill="red", outline="red"))
    canvas.after(1150, lambda: canvas.create_text(200, 370, text="I love you pookie<3!", font=("Courier New", 20, "bold"), fill="red"))
    print("You made the right choice!")

def nienko():
    top = tk.Toplevel(win)
    top.title("Windows error")
    top.geometry("200x80+130+220")
    lta = tk.Label(top, text="Wrong answer!\nLet's try again")
    lta.pack()
    btn_ok = tk.Button(top, text="OK", command=top.destroy)
    btn_ok.pack()
    print("the only correct answear is yes")

def are_you_sure():
    top = tk.Toplevel(win)
    top.title("Think hard")
    top.geometry("200x120+130+220")
    ars = tk.Label(top, text="Are you sure?")
    ars.pack()
    btn_yes = tk.Button(top, text="No, I changed my mind", command=top.destroy)
    btn_yes.pack()
    btn_no = tk.Button(top, text="Yes, close", command=win.destroy)
    btn_no.pack()
    print("the only correct answer is no")

def ty_si_kreten():
    top = tk.Toplevel(win)
    top.title("Think hard")
    top.geometry("200x120+130+220")
    ars = tk.Label(top, text="Si kretén?")
    ars.pack()
    btn_yes = tk.Button(top, text="ano", command=top.destroy)
    btn_yes.pack()
    btn_no = tk.Button(top, text="nie", command=top.destroy)
    btn_no.pack()
    print("the only correct answer is yes")

button_ano = tk.Button(
    win,
    text="Yes",
    command=anko,
    font=("Courier New", 18),
    fg="red",
    bg="pink",
    width=28,
    height=2
)
button_ano.pack(pady=5)

button_nie = tk.Button(
    win,
    text="No",
    command=are_you_sure,
    font=("Courier New", 18),
    fg="red",
    bg="pink",
    width=28,
    height=2
)
button_nie.pack(pady=5)

canvas.delete()

win.mainloop()