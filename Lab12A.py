def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a whole number (no decimals), try again.")

def main():
    print("[My Integer Collection]")
    numbers = []

    for i in range(10):
        num = input_int("Enter an integer: ")
        numbers.append(num)

    print("These are the numbers you entered:")
    for index, value in enumerate(numbers):
        print(f"{index}. {value}")

if __name__ == "__main__":
    main()