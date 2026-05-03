"""
odovzdaj Napíš funkciu do_dvojic(postupnost), ktorá danú postupnosť (zoznam, n-ticu, …) párnej dĺžky „rozseká“ na zoznam dvojíc (list s prvkami tuple), dvojice postupne budú (prvý, druhý), (tretí, štvrtý), … Napríklad:

x = do_dvojic(('11', 22, '3', 4))
    [('11', 22), ('3', 4)]
"""

def do_dvojic(postupnost):
    to_list = list(postupnost)
    result = []
    for i in range(1, len(to_list), 2):
        result += (to_list[i-1], to_list[i])
    return result

print(do_dvojic(('11', 22, '3', 4)))