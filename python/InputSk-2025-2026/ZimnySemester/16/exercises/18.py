'''Zapíš tri verzie funkcie 
mix(gen1,
 
gen2)
, ktorá generuje prvky na striedačku - ak v jednom skončí skôr, tak už berie len zvyšné druhého




najprv s pomocným zoznamom: prvý generátor najprv presype prvky do zoznamu, a potom počas prechodu druhým generátorom dáva aj prvky z pomocného zoznamu


bez pomocného zoznamu len pomocou štandardnej funkcie 
next()


porozmýšľaj nad verziou 
mix(*gen)
, v ktorej sa mixuje ľubovoľne veľa generátorov




Napríklad:


>>> 
print
(
*
mix
(
iter
(
'PYTHON'
),
 
iter
(
range
(
4
)),
 
iter
(
'ahoj'
)))


    P 0 a Y 1 h T 2 o H 3 j O N
'''