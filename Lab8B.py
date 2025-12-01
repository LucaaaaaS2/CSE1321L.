friend_list = []

print("[Friend List]")

while True:
    print("1 - Add friend")
    print("2 - List friends")
    print("3 - Quit")
    choice = int(input("Make your selection: "))

    if choice == 1:
        name = input("Enter your friend's name: ")
        age = input("Enter your friend's age: ")
        friend_list.append((name, age))
        print("Friend added")

    elif choice == 2:
        for x in friend_list:
            print(f"Name: {x[0]}, Age: {x[1]}")

    elif choice == 3:
        print("Shutting down...")
        break