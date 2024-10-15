physics = int(input("Enter Marks Scored in Physics :"))
chemistry = int(input("Enter Marks Scored in Chemistry :"))
biology = int(input("Enter Marks Scored in Biology :"))
maths = int(input("Enter Marks Scored in Maths :"))
computer = int(input("Enter Marks Scored in Computer :"))
total = physics + chemistry + biology + maths + computer
percentage = total/500 * 100
if percentage >= 90 :
    print(f"You scored {percentage}% with Grade A")
elif percentage >= 80 :
    print(f"You scored {percentage}% with Grade B")
elif percentage >= 70 :
    print(f"You scored {percentage}% with Grade C")
elif percentage >= 60 :
    print(f"You scored {percentage}% with Grade D")
elif percentage >= 40 :
    print(f"You scored {percentage}% with Grade E")
elif percentage >= 35 :
    print(f"You scored {percentage}% with Grade F")
elif percentage < 35 :
    print(f"You Failed with {percentage}%")



