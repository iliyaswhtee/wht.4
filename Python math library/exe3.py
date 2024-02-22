def polygon(length, sides, radius):
    area = (sides/2) * length * radius
    return area

length = float(input("Enter the length: "))
sides = int(input("Enter the sides: "))
radius = float(input("Enter the radius: "))

print("The area is: ", polygon(length, sides, radius))