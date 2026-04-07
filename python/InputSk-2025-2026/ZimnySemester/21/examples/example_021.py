class Program:
    def __init__(self):

        def strihaj(meno_suboru, ps, pr=1):
            obr = Image.open(meno_suboru)
            sir, vys = obr.width // ps, obr.height // pr
            return [ImageTk.PhotoImage(obr.crop((x, y, x + sir, y + vys)))
                        for y in range(0, obr.height, vys)
                            for x in range(0, obr.width, sir)]

        win = tkinter.Tk()
        win.title('zvieratka v lese')
        zoz1 = strihaj('vtak.png', 8)
        zoz2 = strihaj('zajo.png', 8)
        zoz3 = strihaj('zemegula.png', 7, 3)
        Plocha('les.png', zoz1, zoz2, zoz3)