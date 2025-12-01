print("Welcome!")
number = float(input("Please input a number: "))
print("What would you like to do with this number: ")
print("0) Get the additive inverse of the number")
print("1) Get the reciprocal of the number")
print("2) Square the number")
print("3) Cube the number")
print("4) Exit the program")
select = int(input(""))
if select == 0:
    print(f"The additive inverse of {number} is -{number}")
elif select == 1:
    if number == 0:
        print("Cannot divide by 0!")
    else:
        reciprocal = 1 / number
        print(f"The reciprocal of {number} is {reciprocal:.3f}")
elif select == 2:
    square = number * number
    print(f"The square of {number} is {square}")
elif select == 3:
    cube = number * number * number
    print(f"The cube of {number} is {cube}")
elif select == 4:
    print("Thank you, goodbye!")
else:
    print("Invalid option!")
