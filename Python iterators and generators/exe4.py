def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input("first num: "))
b = int(input("second num: "))

for square in squares(a, b):
    print(square)