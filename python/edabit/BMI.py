# 1. Úroveň: Začiatočník (Základy a podmienky)

# Úloha: Kalkulačka indexu telesnej hmotnosti (BMI)

#     Zadanie: Napíš program, ktorý od používateľa vypýta jeho výšku v metroch (napr. 1.75) a váhu v kilogramoch (napr. 70). Program vypočíta BMI podľa vzorca: BMI=vyˊ​sˇka2vaˊha​.

#     Výstup: Program vypíše výsledné BMI zaokrúhlené na jedno desatinné miesto a pridá textové hodnotenie:

#         BMI < 18.5 → "Podváha"

#         BMI od 18.5 do 24.9 → "Normálna váha"

#         BMI ≥ 25 → "Nadváha"



weight = float(input("Zadajte svoju váhu v kilogramoch: "))
height = float(input("Zadajte svoju výšku v metroch: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Podváha"
elif 18.5 <= bmi < 25:
    category = "Normálna váha"
else:
    category = "Nadváha"

print(f"Vaše BMI je: {bmi:.1f}")
print(f"Hodnotenie: {category}")