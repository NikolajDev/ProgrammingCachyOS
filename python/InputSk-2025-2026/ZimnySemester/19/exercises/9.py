'''Zisti, aká je časová zložitosť týchto algoritmov:


# zisťuje akýsi súčet



i
,
 
j
 
=
 
1
,
 
1


sum
 
=
 
0


while
 
i
 
<
 
n
:

    
sum
 
+=
 
i
 
*
 
j

    
i
 
=
 
10
 
*
 
i

    
j
 
=
 
(
j
 
+
 
1
)
 
%
 
10


print
(
sum
)



# rekurzívny výpočet



def
 
f
(
n
):

    
if
 
n
 
<=
 
1
:

        
return
 
1

    
return
 
f
(
n
 
//
 
2
)
 
+
 
f
(
n
 
//
 
2
)



# rekurzívny výpočet - to isté ako predchádzajúci príklad, ale máličko inak



def
 
f
(
n
):

    
if
 
n
 
<=
 
1
:

        
return
 
1

    
return
 
2
 
*
 
f
(
n
 
//
 
2
)



# ešte jeden cyklus



f
 
=
 
1


while
 
2
 
*
 
f
 
<=
 
n
:

    
f
 
*=
 
2


print
(
f
)



# rozklad čísla na prvočinitele



def
 
rozklad
(
n
):

    
i
 
=
 
2

    
while
 
n
 
>
 
1
:

        
if
 
n
 
%
 
i
 
==
 
0
:

            
n
 
=
 
n
 
//
 
i

        
else
:

            
i
 
+=
 
1
'''