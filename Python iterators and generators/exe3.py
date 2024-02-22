def divisible_by_3_and_4(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("your num: "))
for num in divisible_by_3_and_4(n):
    print(num)