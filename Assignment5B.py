import random
width = int(input("Enter the width of the grid: "))
height = int(input("Enter the height of the grid: "))
board = []
numberOfUndiscoveredTreasures = 0
for i in range(width):
    row = []
    for j in range(height):
        if random.random() >= 0.7:
            row.append("T")
            numberOfUndiscoveredTreasures += 1
        else:
            row.append("O")
    board.append(row)

print(f"Number of treasures hidden: {numberOfUndiscoveredTreasures}")
while numberOfUndiscoveredTreasures > 0:
    row_guess = int(input(f"Enter the row number (0 to {width - 1}): "))
    col_guess = int(input(f"Enter the column number (0 to {height - 1}): "))

    if board[row_guess][col_guess] == "T":
        print("Congratulations! You found a treasure!")
        board[row_guess][col_guess] = "X"
        numberOfUndiscoveredTreasures -= 1
    else:
        print("No treasure here, try again!")
    for row in board:
        print(" ".join(row))

print("Congratulations! You've found all the treasures!")
for row in board:
    print(" ".join(row))