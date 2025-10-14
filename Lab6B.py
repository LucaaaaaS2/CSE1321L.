import random
randow_number = random.randint(1, 100)
print(randow_number)
print("Guess the number I am thinking!")
while True:
    x = int(input("Enter any number between 1 and 100: "))
    if x > randow_number:
        print("Too high!")
    elif x < randow_number:
        print("Too low!")
    else:
        print(f"Correct! I was thinking of {randow_number}!")
        break
