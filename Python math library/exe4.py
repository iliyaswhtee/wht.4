def superman(base, height):
    area = base * height
    return area

base = float(input("Enter the length: "))
height = float(input("Enter the height: "))

print("The area of parallelogram is: ", superman(base, height))