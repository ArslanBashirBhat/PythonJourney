sideA = int(input("Enter Side A of triangle :"))
sideB = int(input("Enter Side B of triangle :"))
sideC = int(input("Enter Side c of triangle :"))
#sum of any two sides of a triangle should be greater than third side
if sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA:
    print("Triangle is Valid")
else :
    print("Triangle is not Valid")