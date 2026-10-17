def is_prime(num: int) -> bool:
    if num == 1:
        return False
    else:
        for i in range(2, (num//2 + 1)):
            if (num % i == 0):
                return False
    return True


def primes(start: int, stop: int) -> list(int):
    prime_nums = []
    for i in range(start, stop+1):
        if is_prime(i):
            prime_nums.append(i)
    return prime_nums


many = int(input("How many times you want to input the range of nums: "))
for i in range(many):
    start, stop = int(input("From: ")), int(input("To: "))
    for val in (primes(start, stop)):
        print(val)

