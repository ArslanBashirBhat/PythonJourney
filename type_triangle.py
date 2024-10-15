sideA = int(input("Enter side A of triangle :"))
sideB = int(input("Enter side B of triangle :"))
sideC = int(input("Enter side A of triangle :"))
if sideA == sideB == sideC :
    print("EQUILATERAL TRIANGLE")
elif sideA == sideB or sideA == sideC or sideB == sideC :
    print("ISOSCELES TRIANGLE")
else :
    print("SCALENE TRIANGLE")