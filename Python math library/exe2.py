def trapezoid(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = float(input("Enter the first: "))
base2 = float(input("Enter the second: "))
height = float(input("Enter the height: "))

print("The area of the trapezoid is:", trapezoid(base1, base2, height))