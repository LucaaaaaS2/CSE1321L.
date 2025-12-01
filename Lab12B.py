def main():
    print("[Division]")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 / num2
            print(f"{num1} / {num2} = {result:.2f}")
        except ValueError:
            print("Please enter numerical values.")
        except ZeroDivisionError:
            print("We cannot divide by zero.")

        again = input("Do you want to perform another division (Y/N)?: ")
        if again.upper() != "Y":
            break

if __name__ == "__main__":
    main()