'''Zadefinuj triedu 
MojaTurtle
 odvodenú od 
turtle.Turtle
, v ktorej bude definova metóda 
trojuholník
. Metóda nakreslí rovnostranný trojuholník s danou veľkosťou strany, pričom sa bude otáčať vpravo. Otestuj, napríklad:


t
 
=
 
MojaTurtle
()


for
 
i
 
in
 
range
(
5
):

    
t
.
trojuholnik
(
150
)

    
t
.
lt
(
72
)






Teraz zadefinuj 
MojaTurtle2
, ktorá je odvodenú od 
MojaTurtle
. V nej predefinuješ metódu 
trojuholnik
. Táto nová verzia metódy najprv nastaví náhodnú farbu výplne (
self.fillcolor(...)
), naštartuje vypĺňanie (
self.begin_fill()
), zavolá metódu 
trojuholník
 z rodičovskej triedy (super triedy) a ukončí vypĺňanie (
self.end_fill()
). Otestuj, napríklad:


t
 
=
 
MojaTurtle2
()


for
 
i
 
in
 
range
(
5
):

    
t
.
trojuholnik
(
150
)

    
t
.
lt
(
72
)






Teraz v prvej triede 
MojaTurtle
 zadefinuj metódu 
rt(uhol)
 tak, že sa korytnačka najprv otočí o len polovičný uhol, prejde dopredu dĺžku 
10
 a nakoniec sa otočí o druhú polovicu uhla. Otestuj nielen nakreslenie trojuholníka, ale nakresli aj nejaký štvorec.


Po spustení testu s trojuholníkmi môžeš dostať takýto obrázok:
'''