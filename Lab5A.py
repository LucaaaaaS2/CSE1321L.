print("Please enter 10 numbers and this program will display the largest.")
largest = 0
for x in range(1,11):
    number = int(input(f" Please enter number {x}:"))
    if number > largest:
        largest = number
print(f"The largest number was {largest}")



