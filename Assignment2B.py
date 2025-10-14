
brasskey = False
ironkey = False
checkedmattress = False
escaped = False


print("You wake up in a dimly lit room. The air smells faintly of dust and old wood.")
print("The only visible exit is a heavy iron door with a large lock.")
print("Looking around, you notice:")
print("- A small wooden chest sitting on a table in the corner")
print("- A bare mattress on the floor")
print("- A section of the floorboards that looks slightly uneven, almost as if one plank doesn't quite fit.")

while not escaped:
    print("What do you do?")
    print("A. Open the heavy iron door.")
    print("B. Inspect the wooden chest.")
    print("C. Inspect the mattress.")
    print("D. Inspect the suspicious plank in the floorboard.")

    choice = input()

    if choice == "A":
        if ironkey:
            print("The iron key slides into the lock. You turn it, the mechanism clicks. The door swings open. You're free!")
            escaped = True
        elif brasskey:
            print("The brass key is too small for the door’s lock. Maybe it opens something else.")
        else:
            print("You tug the handle. It doesn't budge. The key must be somewhere in this room...")

    elif choice == "B":
        if brasskey and not ironkey:
            print("The brass key fits the chest lock. It clicks open. Inside rests a heavier iron key. This one looks it is made for a door.")
            ironkey = True
        elif brasskey and ironkey:
            print("You check the chest again, nothing else inside.")
        else:
            print("The chest is locked. The key has to be around here somewhere...")

    elif choice == "C":
        if not checkedmattress:
            print("You inspect the thin mattress, there is nothing on it. You lift it, there is nothing underneath either.")
            checkedmattress = True
        else:
            print("You already checked the mattress. There is nothing there.")

    elif choice == "D":
        if not brasskey:
            print("You pry up the loose plank. Hidden in the dust lies a small brass key.")
            brasskey = True
        else:
            print("You've already pried up the plank. There is nothing else underneath.")

    else:
        print("Invalid choice, please select A, B, C, or D.")