import random

with open('cisla.txt', 'w') as file:
    for i in range(100):
        file.write(f'{random.randint(0, 1000)} ')