"""
Napíš pythonovský skript s funkciou pyramida(ret1, ret2). Oba parametre sú znakové reťazce a obsahujú informácie pre nakreslenie obrázka pomocou tkinter. Prvý reťazec obsahuje 3 celé čísla oddelené čiarkou , (medzera sa bude ignorovať): n, sirka, vyska. Druhý reťazec obsahuje tri mená farieb tiež oddelené čiarkou ,. Funkcia do grafickej plochy nakreslí pyramídu zloženú z farebných obdĺžnikov veľkosti (sirka, vyska) (pomocou create_rectangle()). Pyramída sa skladá z n poschodí: na vrchu pyramídy je jeden obdĺžnik, pod ním sú dva odsunuté vľavo o polovicu šírky, pod nimi sú tri opäť odsunuté vľavo, atď. Tieto obdĺžniky budú zafarbené tromi farbami tak, že žiadne dva, ktoré sa dotýkajú, nemajú rovnakú farbu. Tieto tri farby obdĺžnikov sú zadefinované v druhom parametri ret2.

Napríklad, pre volanie pyramida('4, 50, 20', 'green, blue, maroon') môžeš dostať takýto obrázok:

V tvojom riešení nepoužívaj žiaden iný modul okrem tkinter. Z Pythonu používaj len príkazy z prvých štyroch prednášok. Do grafického plátna (canvas) kresli len pomocou create_rectangle, do ktorého pošleš 4 čísla ako súradnice dvoch bodov a pomenovaný parameter fill. Je jedno, kde v plátne umiestniš nakreslenú pyramídu, môžeš predpokladať, že testovač má neobmedzené rozmery plochy. Bolo by dobre, keby si vykreslil všetky obdĺžniky v takom poradí, že najprv sú všetky jednej farby, až potom všetky obdĺžniky nejake druhej farby a na záver všetky obdĺžniky zvyšnej farby.

Niektoré testy testovača budú testovať len to, či sú obdĺžniky správne rozmiestnené, ďalšie či sú aj správne zafarbené a niektoré testy budú zisťovať aj to, v akom poradí budú farebné obdĺžniky vykresľované (najprv všetky jednou farbou, potom druhou a na koniec všetky ostatné).

Keďže testovací systém vektor nevie pracovať s grafickými aplikáciami, tvoj skript by mohol mať takúto štruktúru:

# 2. tyzdenny projekt
# student: Janko Hrasko
# datum: 5.10.2025

import tkinter1 as tkinter

def pyramida(ret1, ret2):
    ...
    canvas = tkinter.Canvas(width=1200, height=800)
    canvas.pack()
    ...
    tkinter.mainloop()

if __name__ == '__main__':
    pyramida('4, 50, 20', 'green, blue, maroon')    # testovacie volanie funkcie
Pričom pre testovanie na tvojom počitači môže tkinter1.py vyzerať takto:

from tkinter import Canvas, mainloop
Súbor tkinter1.py by mal byť v tom istom priečinku ako tvoj skript, neposiela sa do testovača, lebo testovač ho aj tak má vo svojej verzii.

"""

# 2. tyzdenny projekt
# student: Janko Hrasko
# datum: 5.10.2025

from tkinter import Canvas, mainloop

canvas = Canvas(width=300, height=1080)
canvas.pack()

def pyramida(ret1, ret2):
    n, sirka, vyska = 0, 0, 0

    help = ''
    for i in ret1:
        if i == ",":
            n = int(help)
            help = ""
            n, sirka = sirka, n
        else:
            help += i
        
    vyska = int(help)

    c1, c2 = '', ''
    help = ""

    for i in ret2:
        if i == ",":
            c1 = help
            help = ""
            c1, c2 = c2, c1
        elif i == " ":
            continue
        else:
            help += i
            
    c3 = help

    x = 300 // 2 - sirka
    y = 10

    for i in range(1 , n+1):
        for j in range(i):
            if (i + j) % 3 == 0:
                canvas.create_rectangle(x, y, x + sirka, y+ vyska, fill=c1)
                x += sirka
            else:
                x+= sirka
        x = 300 // 2 - ((sirka) *(i/2)) - sirka
        y += vyska

    x = 300 // 2 - sirka
    y = 10
    for i in range(1 , n+1):
        for j in range(i):
            if (i + j) % 3 == 1:
                canvas.create_rectangle(x, y, x + sirka, y+ vyska, fill=c2)
                x += sirka
            else:
                x+= sirka
        x = 300 // 2 - ((sirka) *(i/2)) - sirka
        y += vyska

    x = 300 // 2 - sirka
    y = 10
    
    for i in range(1 , n+1):
        for j in range(i):
            if (i + j) % 3 == 2:
                canvas.create_rectangle(x, y, x + sirka, y+ vyska, fill=c3)
                x += sirka
            else:
                x+= sirka
        x = 300 // 2 - ((sirka) *(i/2)) - sirka
        y += vyska
        

pyramida('4, 50, 20', 'green, blue, maroon')

mainloop()