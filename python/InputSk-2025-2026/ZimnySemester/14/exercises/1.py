'''Do triedy 
MojaTurtle
 z prednášky (má metódu 
domcek()
) pridaj inicializáciu 
__init__(self)
, ktorá nastaví 
speed(0)
 a náhodnú pozíciu, kde 
x
 aj 
y
 je z 
<-250,
 
250>
. Trieda 
MojaTurtle1
 je odvodená z 
MojaTurtle
 a kresli cikcakové čiary. Teraz vytvor novú triedu 
MojaTurtle2
, ktorá bude odvodená z 
MojaTurtle
. V tejto triede prekryješ 
lt(uhol)
 aj 
rt(uhol)
, v ktorých sa zmení otočenie na 
uhol+randint(-5,5)
. Otestuj:


turtle
.
delay
(
0
)


for
 
i
 
in
 
range
(
10
):

    
MojaTurtle1
()
.
domcek
(
50
)


for
 
i
 
in
 
range
(
10
):

    
MojaTurtle2
()
.
domcek
(
50
)






Teraz zmeň triedu 
MojaTurtle1
 tak, aby bola odvodená z 
MojaTurtle2
. Opäť otestuj kreslenie 20 domčekov.
'''