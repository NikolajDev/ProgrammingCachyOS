'''-
 Napíš funkciu 
druhy(stack)
, ktorá zo zásobníka vyberie a vráti druhý prvok od spodu (dna zásobníka). Všetky ostatné prvky nezmení. Otestuj:


>>> 
z
 
=
 
Stack
(
'python'
)


>>> 
druhy
(
z
)


    'y'


>>> 
z


    Stack(('p', 't', 'h', 'o', 'n'))






ak sa nedá vykonať, vyvolá 
EmptyError
, napríklad:


>>> 
z
 
=
 
Stack
([
'python'
])


>>> 
druhy
(
z
)


    ...


    EmptyError


>>> 
z


    Stack(('python',))
'''