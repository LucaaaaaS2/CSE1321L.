side1= float(input("Enter the first side of the triangle: "))
side2=float(input("Enter the second side of the triangle: "))
side3=float(input("Enter the third side of the triangle: "))
if side1> 0 and side2> 0 and side3> 0:
    if(side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1):
        if side1==side2 and side2==side3:
            print("The triangle is an equilateral triangle.")
        else:
            if side1 == side2 or side1 == side3 or side2==side3:
                print("The triangle is an isosceles triangle.")
            else:
                print("The triangle is a scalene triangle.")
    else:
        print("The sides do not form a valid triangle.")
else:
    print("Invalid input. All sides must be greater than 0.")
    