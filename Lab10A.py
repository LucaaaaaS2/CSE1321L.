class Chair:
    def __init__(self, numOfLegs = 4, rolling = False, material = "wood"):
        self.numOfLegs = numOfLegs
        self.rolling = rolling
        self.material = material

print("You are about to create a chair.")
numOfLegs = int(input("How many legs does your chair have: "))
rolling = input("Is your chair rolling (true/false): ").lower()
material = input("What is your chair made of: ").lower()

if rolling == "true":
    rolling = True
else:
    rolling = False

chair = Chair(numOfLegs, rolling, material)

if chair.rolling:
    print(f"Your chair has {chair.numOfLegs} legs, is rolling, and is made of {chair.material}.")
else:
    print(f"Your chair has {chair.numOfLegs} legs, is not rolling, and is made of {chair.material}.")

print("This program is going to change that.")

chair.numOfLegs = 4
chair.rolling = False
chair.material = "wood"

if chair.rolling:
    print(f"Your chair has {chair.numOfLegs} legs, is rolling, and is made of {chair.material}.")
else:
    print(f"Your chair has {chair.numOfLegs} legs, is not rolling, and is made of {chair.material}.")