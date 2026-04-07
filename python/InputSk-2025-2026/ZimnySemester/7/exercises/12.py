'''Gumená úsečka: kliknutie naštartuje vytváranie úsečky (program si bude pamätať dva vrcholy úsečky - na začiatku prvý aj druhý bod úsečky bude samotný kliknutý bod, teda veľkosť nakreslenej úsečky je 0). Ťahaním sa aktualizuje jej druhý bod (na zmenu doteraz nakreslenej úsečky použi metódu 
canvas.coords()
). Každé ďalšie kliknutie a ťahanie vytvára ďalšiu úsečku.


Teraz pridaj widget posúvač 
Scale
, napríklad takto:


hrubka
 
=
 
tkinter
.
Scale
(
orient
=
'horizontal'
,
 
from_
=
1
,
 
to
=
20
)


hrubka
.
pack
()






pomocou ktorého sa bude dať nastavovať hrúbka kreslených úsečiek. Pri vytváraní novej úsečky zistíš momentálne nastavenú hrúbku pomocou 
hrubka.get()
.
'''