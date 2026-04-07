'''-
 Táto verzia triedenia vkladaním v niektorých situáciách vypíše momentálny obsah celého zoznamu. Ručne odtrasuj tento algoritmus a vypíš tieto kontrolné výpisy:


def
 
insert_sort1
(
zoz
):

    
for
 
i
 
in
 
range
(
1
,
 
len
(
zoz
)):

        
j
,
 
t
 
=
 
i
,
 
zoz
[
i
]

        
while
 
j
 
>
 
0
 
and
 
zoz
[
j
-
1
]
 
>
 
t
:

            
zoz
[
j
]
 
=
 
zoz
[
j
-
1
]

            
j
 
-=
 
1

        
if
 
j
 
<
 
i
:

            
zoz
[
j
]
 
=
 
t


            
print
(
*
zoz
)




z
 
=
 
[
5
,
 
9
,
 
4
,
 
3
,
 
6
,
 
10
,
 
1
,
 
8
,
 
2
,
 
7
]


insert_sort1
(
z
)
'''