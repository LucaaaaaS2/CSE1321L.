while True:
    print("Multiplication and Exponent Calculator")
    print("Choose option 1 for Multiplication")
    print("Choose option 2 for Exponentiation")
    print("Choose option 3 to Exit")
    choice = int(input())
    if choice == 1:
        x = int(input("Enter an operand: "))
        y = int(input("Enter the other operand: "))
        result = 0
        for i in range(y):
            result = result + x
        print(f"{x} x {y} = {result}")
    elif choice == 2:
        base = int(input("Enter the base: "))
        exp = int(input("Enter the exponent: "))
        result = 1
        for i in range(exp):
            temp = 0
            for j in range(base):
                temp = temp + result
            result = temp
        print(f"{base}^({exp}) = {result}")
    elif choice == 3:
        print("Closing the Calculator...")
        break
    else:
        print("Invalid Choice")




