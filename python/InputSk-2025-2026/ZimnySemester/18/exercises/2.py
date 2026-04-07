'''-
 Otestuj rôzne triediace algoritmy (
bubble_sort
, 
min_sort
 a 
insert_sort
) ručným zadávaním dvoch prvkov a prípadnou ich výmenou. Použi aplikáciu, v ktorej sa najprv vygeneruje náhodný 
8
-prvkový zoznam čísel. Potom sa očakáva zadávanie dvojíc kartičiek, ktoré môžeš navzájom vymeniť. Program beží v grafickom režime:


import
 
tkinter


import
 
random



class
 
Karta
:

    
def
 
__init__
(
self
,
 
x
,
 
y
,
 
h
):

        
self
.
x
,
 
self
.
y
,
 
self
.
h
 
=
 
x
,
 
y
,
 
h

        
self
.
id1
 
=
 
canvas
.
create_rectangle
(
x
,
 
y
,
 
x
+
sir
,
 
y
+
vys
,
 
fill
=
'lightblue'
)

        
self
.
id2
 
=
 
canvas
.
create_text
(
x
+
sir
//
2
,
 
y
+
vys
//
2
,
 
text
=
h
,
 
font
=
'consolas 30 bold'
,
 
fill
=
'navy'
)

        
self
.
id3
 
=
 
canvas
.
create_rectangle
(
x
,
 
y
,
 
x
+
sir
,
 
y
+
vys
,
 
fill
=
'steelblue'
)

        
self
.
b
 
=
 
True


    
def
 
__repr__
(
self
):

        
return
 
str
(
self
.
h
)


    
def
 
klik
(
self
,
 
x
,
 
y
):

        
return
 
self
.
x
 
<=
 
x
 
<
 
self
.
x
+
sir
 
and
 
self
.
y
 
<=
 
y
 
<
 
self
.
y
+
vys


    
def
 
zmen
(
self
):

        
self
.
b
 
=
 
not
 
self
.
b

        
canvas
.
itemconfig
(
self
.
id3
,
 
fill
=
'steelblue'
 
if
 
self
.
b
 
else
 
''
)



def
 
klik
(
ev
):

    
for
 
k
 
in
 
zoz
:

        
if
 
k
.
klik
(
ev
.
x
,
 
ev
.
y
):

            
k
.
zmen
()

            
if
 
not
 
k
.
b
:

                
sel
.
append
(
k
)

            
else
:

                
sel
.
remove
(
k
)

            
return



def
 
rob
(
ev
):

    
if
 
len
(
sel
)
 
==
 
2
:

        
k1
,
 
k2
 
=
 
sel

        
if
 
k1
.
x
 
>
 
k2
.
x
:

            
k1
,
 
k2
 
=
 
k2
,
 
k1

        
if
 
k1
.
h
 
>
 
k2
.
h
:

            
canvas
.
itemconfig
(
k1
.
id3
,
 
width
=
0
)

            
canvas
.
itemconfig
(
k2
.
id3
,
 
width
=
0
)

            
dx
 
=
 
k2
.
x
-
k1
.
x

            
for
 
i
 
in
 
range
(
10
):

                
canvas
.
update
()

                
canvas
.
after
(
50
)

                
canvas
.
move
(
k1
.
id1
,
 
dx
/
10
,
 
0
)

                
canvas
.
move
(
k1
.
id2
,
 
dx
/
10
,
 
0
)

                
canvas
.
move
(
k2
.
id1
,
 
-
dx
/
10
,
 
0
)

                
canvas
.
move
(
k2
.
id2
,
 
-
dx
/
10
,
 
0
)

            
k1
.
h
,
 
k2
.
h
 
=
 
k2
.
h
,
 
k1
.
h

            
canvas
.
itemconfig
(
k1
.
id2
,
 
text
=
k1
.
h
,
 
fill
=
'navy'
)

            
canvas
.
itemconfig
(
k2
.
id2
,
 
text
=
k2
.
h
,
 
fill
=
'navy'
)

            
canvas
.
move
(
k1
.
id1
,
 
-
dx
,
 
0
)

            
canvas
.
move
(
k1
.
id2
,
 
-
dx
,
 
0
)

            
canvas
.
move
(
k2
.
id1
,
 
dx
,
 
0
)

            
canvas
.
move
(
k2
.
id2
,
 
dx
,
 
0
)

            
canvas
.
itemconfig
(
k1
.
id3
,
 
width
=
1
)

            
canvas
.
itemconfig
(
k2
.
id3
,
 
width
=
1
)

            
canvas
.
update
()

            
canvas
.
after
(
500
)

    
for
 
k
 
in
 
sel
:

        
k
.
zmen
()

    
sel
.
clear
()



def
 
vsetky
(
ev
):

    
for
 
k
 
in
 
zoz
:

        
if
 
k
.
b
:

            
k
.
zmen
()

            
sel
.
append
(
k
)



def
 
nahodne
(
ev
):

    
for
 
k
 
in
 
zoz
:

        
k
.
h
 
=
 
random
.
randint
(
10
,
 
99
)

        
canvas
.
itemconfig
(
k
.
id2
,
 
text
=
k
.
h
)



canvas
 
=
 
tkinter
.
Canvas
(
width
=
500
,
 
height
=
120
)


canvas
.
pack
()


sir
,
 
vys
 
=
 
50
,
 
70


zoz
,
 
sel
 
=
 
[],
 
[]


y
 
=
 
10


for
 
x
 
in
 
range
(
10
,
 
490
-
sir
,
 
sir
+
10
):

    
canvas
.
create_rectangle
(
x
-
2
,
 
y
-
2
,
 
x
+
sir
+
4
,
 
y
+
vys
+
4
,
 
outline
=
'lightgray'
,
 
fill
=
'white'
)


for
 
x
 
in
 
range
(
10
,
 
490
-
sir
,
 
sir
+
10
):

    
zoz
.
append
(
Karta
(
x
,
 
y
,
 
random
.
randint
(
10
,
 
99
)))


canvas
.
bind
(
'<ButtonPress-1>'
,
 
klik
)


canvas
.
bind
(
'<ButtonPress-3>'
,
 
rob
)


canvas
.
bind_all
(
'a'
,
 
vsetky
)


canvas
.
bind_all
(
'n'
,
 
nahodne
)


tkinter
.
mainloop
()






Tento program ti namieša 
8
 kartičiek s náhodnými číslami. Klikaním ich otáčaš, pravým klikom 2 otočené navzájom vymeníš (len ak je prvá väčšia ako druhá). Kláves 
n
 pripraví novú sadu náhodných čísel.
'''