print("[Factorial Calculator]")

while True:
    num = int(input(" Enter a number: "))
    if num < 0:
        print(" Error: Number must be 0 or positive, try again.\n")
    else:
        break


factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f" Calculating {num}! ...")
print(f" {num}! is {factorial}\n")
print(" Program Terminated")
