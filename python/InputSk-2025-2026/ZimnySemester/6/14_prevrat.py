"""
Napíš funkciu prevrat(meno_suboru), ktorá prevráti poradie riadkov v danom textovom súbore. Funkcia nič nevypisuje ani nevracia, len zmení obsah zadaného textového súboru. Napríklad:

print('prvy\n druhy\n  treti\nstvrty', file=open('text.txt', 'w'))
prevrat('text.txt')
print(open('text.txt').read(), end='')
    stvrty
      treti
     druhy
    prvy

"""


def prevrat(meno_suboru):
    with open(meno_suboru) as file:
        lines = file.readlines()
    
    lines = lines[::-1]
    with open(meno_suboru, 'w') as file:
        file.writelines(lines)


if __name__ == "__main__":
    prevrat('text.txt')
    print(open('text.txt').read(), end='')
