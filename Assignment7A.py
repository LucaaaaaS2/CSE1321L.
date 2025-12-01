def display_menu():
    print("Menu Items:")
    print("1. Coffee - $3.50")
    print("2. Sandwich - $5.75")
    print("3. Smoothie - $4.25")
    print("4. Muffin - $2.75")

def take_order():
    items = ["Coffee", "Sandwich", "Smoothie", "Muffin"]
    prices = [3.50, 5.75, 4.25, 2.75]
    order = []
    total = 0

    while True:
        display_menu()
        try:
            choice = int(input("Select an item (1-4): "))
            if choice < 1 or choice > 4:
                print("Error: Please enter a number between 1 and 4.")
                continue
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        item_total = prices[choice - 1] * quantity
        order.append((items[choice - 1], quantity, item_total))
        total += item_total
        print(f"Added {quantity} {items[choice - 1]}(s) - ${item_total:.2f}")

        another = input("Add another item? (Y/N): ").lower()
        if another != 'y':
            break

    print(f"Order complete! Total for this order: ${total:.2f}")
    return order, total

def show_sales(sales):
    print("Today's Sales:")
    total = 0
    for item, qty, cost in sales:
        print(f"- {qty} {item}(s): ${cost:.2f}")
        total += cost
    print(f"Total Sales: ${total:.2f}")

def main():
    daily_sales = []
    while True:
        print("[Owl Cafe]")
        print("1. Place Order")
        print("2. View Daily Sales")
        print("3. Exit")
        choice = input("> ")
        if choice == "1":
            order, _ = take_order()
            daily_sales.extend(order)
        elif choice == "2":
            show_sales(daily_sales)
        elif choice == "3":
            print("Thank you for visiting Owl Cafe!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()