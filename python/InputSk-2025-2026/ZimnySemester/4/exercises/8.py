'''Nasledovná funkcia vykresľuje farebné krúžky v štvorcovej sieti 
n
 x 
n
 a zafarbuje ich podľa podmienky v príkaze 
if
:


import
 
tkinter



def
 
stvorcova_siet
(
n
):

    
canvas
 
=
 
tkinter
.
Canvas
()

    
canvas
.
pack
()


    
for
 
i
 
in
 
range
(
n
):

        
for
 
j
 
in
 
range
(
n
):

            
x
 
=
 
j
 
*
 
20
 
+
 
100

            
y
 
=
 
i
 
*
 
20
 
+
 
12


            
if
 
i
 
==
 
5
:


                
farba
 
=
 
'red'

            
else
:

                
farba
 
=
 
'white'

            
canvas
.
create_oval
(
x
 
-
 
8
,
 
y
 
-
 
8
,
 
x
 
+
 
8
,
 
y
 
+
 
8
,
 
fill
=
farba
)


    
tkinter
.
mainloop
()



stvorcova_siet
(
13
)






A.
 Zmeň 
iba túto podmienku
 tak, aby sa nakreslil obrázok, v ktorom sa zafarbí stredný rad a stredný stĺpec (v programe nemeň iné príkazy, nepridávaj ďalšie):






B.
 Zmeň 
iba túto podmienku
 tak, aby sa nakreslil obrázok, v ktorom sa zafarbia obe uhlopriečky:






Obe verzie programu by mali fungovať správne aj pri zmenenom rozmere 
n
. Vyskúšaj napríklad 
n=10
. Pre párne 
n
 si môžeš zvoliť ľubovoľnú inerpretáciu križovania radov a stĺpcov farebných bodiek.
'''