'''Napíš program, ktorý zabezpečí ťahanie myši: pri ťahaní so zatlačeným ľavým tlačidlom sa kreslia vodorovné úsečky (z kliknutej pozície úsečka dĺžky 100). Pravým klikom sa obrazovka zmaže. V programe zabezpeč zviazanie týchto dvoch ovládačov:


canvas
.
bind
(
'<B1-Motion>'
,
 
kresli
)


canvas
.
bind
(
'<ButtonPress-3>'
,
 
zmaz
)






Po spustení a ťahaní môžeš dostať, napríklad:






Na zmazávanie obrazovky teraz nahraď klikanie pravým tlačidlom novým widgetom 
Button
. Uvedom si, že funkcia, ktorá obsluhuje udalosť od tlačidla musí byť bez parametrov. Tlačidlo vytvoríš, napríklad takto:


tkinter
.
Button
(
text
=
'Zmaž'
,
 
command
=
zmaz
)
.
pack
()
'''