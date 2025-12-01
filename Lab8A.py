email_list = []

print("[Mailing List]")
print()
while True:
    print("1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")
    choice = int(input("Make your selection: "))
    print()
    if choice == 1:
        email_list.append(input("Enter the email to be added: "))
        print("Email added to mailing list.")
        print()
    elif choice == 2:
        remove = input("Enter the email to be removed: ")
        if remove in email_list:
            email_list.remove(remove)
            print(f"{remove} has been removed from the mailing list.")
            print()
        else:
            print(f"No such email in mailing list: {remove}")
            print()
    elif choice == 3:
        for x in email_list:
            print(x)
            print()
    elif choice == 4:
        print("Shutting down...")
        break




