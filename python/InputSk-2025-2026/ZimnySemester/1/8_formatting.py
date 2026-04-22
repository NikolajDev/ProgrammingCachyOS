"""
Napíš program, ktorý prečíta dve celé čísla (napríklad 27 a 342) a vypíše ich v tvare takejto rovnosti: 27+342=369, teda bez medzier. Použi na to formátovaciu šablónu f'...{hodnota}...'. Po spustení teda môžeš dostať:

zadaj 1. číslo: 27
zadaj 2. číslo: 342
27+342=369

alebo

zadaj 1. číslo: 8
zadaj 2. číslo: 999997
8+999997=1000005
"""

first_num = int(input("Enter your first number: "))
second_num = int(input("Enter your second number: "))

print(f"{first_num}+{second_num}={first_num + second_num}")