def div_sum(n):
    if n < 2:
        return 0
    sum_ = 0
    for i in range(2, n//2 + 1):
        if n % i == 0:
            sum_ += i
    return sum_ + 1


count = int(input())
list_nums = []
for _ in range(count):
    num = int(input())
    list_nums.append(num)

for i in list_nums:
    print(div_sum(i))