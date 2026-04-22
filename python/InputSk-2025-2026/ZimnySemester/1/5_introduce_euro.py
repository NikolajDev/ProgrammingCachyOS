"Euro je zavedené na Slovensku od 1. januára 2009. Zisti, koľko približne dní od vtedy uplynulo (do dnes uplynulo 16 rokov, 8 mesiacov a 22 dní). Predpokladaj, že každý rok má 365 dní a každý mesiac má 30 dní. Potom vypočítaj koľko je to hodín a aj sekúnd. Po spustení môžeš dostať:"

year = 365
month = 30

days_euro_in_sk = (16 * year) + (8 * month) + 22

hours_euro_in_sk = days_euro_in_sk * 24
seconds_euro_in_sk = hours_euro_in_sk * 3600

print(f"Number of days since the Euro was introduced in Slovakia: {days_euro_in_sk}")
print(f"Total hours since the Euro's introduction: {hours_euro_in_sk}")
print(f"Total seconds since the Euro's introduction: {seconds_euro_in_sk}")