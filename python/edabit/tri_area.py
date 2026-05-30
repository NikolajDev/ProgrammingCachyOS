# def tri_area(base, height):
#     return (base * height) / 2

# assert tri_area(3, 2) == 3
# assert tri_area(7, 4) == 14
# assert tri_area(10, 10) == 50


from random import choice

dict_help = {'yes': 0, 'no': 0}

for _ in range(100):
    choice_ = choice(["yes", "no"])
    dict_help[choice_] += 1

print(dict_help)
