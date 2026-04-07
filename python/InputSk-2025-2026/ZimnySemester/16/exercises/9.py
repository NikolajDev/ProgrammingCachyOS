'''-
 Nasledovná funkcia z danej množiny hodnôt vytvorí novú, v ktorej je každý prvok zdvojnásobený:


def
 
zmen
(
mn
):

    
return
 
set
(
i
 
*
 
2
 
for
 
i
 
in
 
mn
)






Môžete otestovať:


>>> 
zmen
({
'a'
,
 
21
,
 
'py'
,
 
-
11
,
 
'123'
})


    {-22, 'pypy', 42, 'aa', '123123'}






Funkcia 
zmen()
 využíva 
for
-cyklus. Prepíš ju tak, aby si namiesto toho použil 
iter()
, 
next()
, 
while
 
True
 a 
try
 
except
 
StopIteration
.
'''