'''Odrekurzívni rekurzívnu krivku 
ckrivka()
 z 9. prednášky v zimnom semestri:


import
 
turtle



def
 
ckrivka
(
n
,
 
s
):

    
if
 
n
 
==
 
0
:

        
t
.
fd
(
s
)

    
else
:

        
ckrivka
(
n
 
-
 
1
,
 
s
)

        
t
.
lt
(
90
)

        
ckrivka
(
n
 
-
 
1
,
 
s
)

        
t
.
rt
(
90
)



t
 
=
 
turtle
.
Turtle
()


ckrivka
(
6
,
 
20
)
'''