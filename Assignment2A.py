print("[Welcome to OwlBanking]")

balance = 0.00
history = ""

while True:
    print("Select an option:")
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Check Balance")
    print("4 - Check Transaction History")
    print("Q - Quit")

    option = input()

    if option == "1":
        amount = float(input("How much do you want to deposit: $"))
        old_balance = balance
        balance += amount
        history += f"${amount:.2f} was deposited, balance went from ${old_balance:.2f} to ${balance:.2f}"

    elif option == "2":
        if balance == 0:
            print("Error: Cannot Withdraw with balance of zero")
        else:
            amount = float(input("How much do you want to withdraw: $"))
            if amount > balance:
                print("Error: Cannot Withdraw a larger amount than balance")
            else:
                old_balance = balance
                balance -= amount
                history += f"${amount:.2f} was withdrawn, balance went from ${old_balance:.2f} to ${balance:.2f}"

    elif option == "3":
        print(f"Balance: ${balance:.2f}")

    elif option == "4":
        if history == "":
            print("No transactions yet")
        else:
            print(history, end="")

    elif option== "Q":
        break

    else:
        print("Invalid option, please try again.")
