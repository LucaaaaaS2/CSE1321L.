users = {}

def register():
    print("\n[Register]")
    print("Username:")
    username = input()
    print("Password:")
    password = input()
    users[username] = password
    print("User successfully added!\n")

def login():
    print("\n[Login]")
    print("Username:")
    username = input()
    print("Password:")
    password = input()
    if username in users and users[username] == password:
        print("Success!\n")
        logged_in_menu(username)
    else:
        print("Incorrect username/password!\n")

def logged_in_menu(username):
    while True:
        print("Choose an option")
        print("3 - Change Password")
        print("4 - Logout")
        print("E - Exit")
        choice = input().upper()
        if choice == "3":
            print("\n[Changin password]")  # matches expected typo in lab
            print("Password:")
            new_password = input()
            users[username] = new_password
            print()
        elif choice == "4":
            print("\nLogging Out...\n")
            break
        elif choice == "E":
            print("\nTerminating...")
            exit()
        else:
            print("Invalid option. Try again.\n")

def main_menu():
    while True:
        print("Choose an option")
        print("1 - Login")
        print("2 - Register")
        print("E - Exit\n")
        choice = input().upper()

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "E":
            print("Terminating...")
            break
        else:
            print("Invalid option. Try again.\n")

main_menu()