def printMenu():
    print("[Owl About Coffee]")
    print("1. Espresso - $3.00")
    print("2. Latte - $4.00")
    print("3. Cappuccino - $4.00")
    print("4. Tea - $2.00")
    print("5. Exit and checkout")

def getChoice():
    choice = int(input("Enter your choice: "))
    if choice in range(1,6):
        return(choice)
    else:
        return -1

def processOrder(choice):
    if choice == 1:
        cost = 3
        number = int(input("How many Espresso(s) would you like?"))
        subtotal = cost * number
        print(f"Added {number} Espresso(s) - ${subtotal:.2f} ")
        return subtotal
    if choice == 2:
        cost = 4
        number = int(input("How many Latte(s) would you like?"))
        subtotal = cost * number
        print(f"Added {number} Latte(s) - ${subtotal:.2f} ")
        return subtotal
    if choice == 3:
        cost = 4
        number = int(input("How many Cappuccino(s) would you like?"))
        subtotal = cost * number
        print(f"Added {number} Cappuccino(s) - ${subtotal:.2f} ")
        return subtotal
    if choice == 4:
        cost = 2
        number = int(input("How many Tea(s) would you like?"))
        subtotal = cost * number
        print(f"Added {number} Tea(s) - ${subtotal:.2f} ")
        return subtotal
    else:
        return 0

def getTotal(subtotal):
    if subtotal > 0:
        print()
        print(f"Subtotal: ${subtotal:.2f}")
        tax = subtotal * .06
        print(f"Tax (6%): ${tax:.2f}")
        total = subtotal + tax
        print(f"Total: ${total:.2f}")
        print("[Program Terminated]")

subtotal = 0
while True:
    printMenu()
    choice = getChoice()
    if choice == -1:
        print("Invalid choice, please select one of options displayed.")
        continue
    if choice == 5:
        getTotal(subtotal)
        break
    else:
        subtotal += processOrder(choice)
