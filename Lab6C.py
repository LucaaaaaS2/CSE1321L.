while True:
    rows = int(input("Enter number for rows or 0 to quit: "))
    if rows == 0:
        break
    for i in range(1, rows + 1):
        for s in range(rows - i):
            print(" ",end="")
        for d in range(i,0,-1):
            print(d,end="")
        for a in range(2,i + 1):
            print(a,end="")
        print()
