'''-
 Stláčaním malých a veľkých písmen abecedy (bez diakritiky) sa tieto vypisujú nejakým väčším fontom vedľa seba (Napríklad 
'arial
 
30'
). Využi jeden grafický objekt pre text (
create_text
) a tomuto budeš pri stláčaní písmen pridávať vypisovaný text (pomocou 
canvas.itemconfig()
). Program by mal akceptovať aj stláčanie medzery a 
Enter
 (do textu vloží 
'\n'
 alebo 
'\r'
). Použi metódu 
bind_all('<KeyPress>',
 
...)
 pričom vo viazanej funkcii pracuj s hodnotou 
event.char
.
'''