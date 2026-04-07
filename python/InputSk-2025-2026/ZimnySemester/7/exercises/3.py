'''Program zabezpečí klikanie myšou: prvé kliknutie si zapamätá súradnice, druhé kliknutie nakreslí obdĺžnik (
create_rectangle
), v ktorom jeden vrchol je zapamätaný a druhý vrchol je práve kliknutý. Obdĺžnik je zafarbený náhodnou farbou. Toto sa opakuje pri ďalších klikaniach.


canvas
.
bind
(
'<ButtonPress-1>'
,
 
klik
)






Napríklad:
'''