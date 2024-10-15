angle1 = int(input("Enter angle 1 of Triangle :"))
angle2 = int(input("Enter angle 2 of Triangle :"))
angle3 = int(input("Enter angle 3 of Triangle :"))
sum_of_angles = 180
sum = angle1 + angle2 + angle3
angles = angle1 > 0 and angle2 > 0 and angle3 > 0
if sum == sum_of_angles and angles:
    print("Triangle is Valid")
else :
    print("Triangle is not valid")