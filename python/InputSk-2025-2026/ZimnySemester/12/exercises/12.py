'''-
 Zadefinuj triedu 
MojaGrafika
 s týmito metódami:




metóda 
__init__()
 vytvorí grafickú plochu veľkosti 
400x300
 (atribút 
self.canvas
)


metóda 
kruh(r,
 
x,
 
y,
 
farba=None)
 nakreslí kruh s polomerom 
r
 so stredom 
(x,
 
y)
 s danou výplňou (
None
 označuje náhodnú farbu)


metóda 
stvorec(a,
 
x,
 
y,
 
farba=None)
 nakreslí štvorec so stranou 
a
 so stredom 
(x,
 
y)
 s danou výplňou (
None
 označuje náhodnú farbu)


metóda 
text(text,
 
x,
 
y,
 
farba=None)
 vypíše daný text na súradnice 
(x,
 
y)
 s danou farbou (
None
 označuje náhodnú farbu)


metóda 
zapis(meno_suboru)
 zapíše všetky nakreslené útvary do textového súboru: každý do samostatného riadka v tvare, napríklad 
kruh
 
40
 
100
 
150
 
red
 alebo 
text
 
Python
 
100
 
50
 
#12ff3a
, …


metóda 
citaj(meno_suboru)
 zruší všetky nakreslené objekty (
self.canvas.delete('all')
), prečíta súbor a nakreslí všetky v ňom zapísané útvary




Napríklad:


g
 
=
 
MojaGrafika
()


g
.
stvorec
(
280
,
 
200
,
 
150
,
 
'yellow'
)


for
 
x
 
in
 
range
(
20
,
 
400
,
 
40
):

    
g
.
kruh
(
20
,
 
x
,
 
100
)
               
# náhodné farby


g
.
text
(
'Python'
,
 
200
,
 
150
,
 
'red'
)


g
.
zapis
(
'grafika.txt'
)
               
# vytvorí súbor






g
 
=
 
MojaGrafika
()


g
.
citaj
(
'grafika.txt'
)
               
# znovu ho prečíta a vykreslí
'''