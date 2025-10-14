print("[Sum of Unique Products of Pairs]")
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    j = 1
    while j <= n:
        product = i * j
        duplicate = False
        a = 1
        while a <= i:
            b = 1
            while b <= n:
                if a == i and b >=j:
                    break
                if a * b == product:
                    duplicate = True
                b += 1
            a += 1
        if duplicate:
            print(f"({i},{j}) = {product} (duplicate, ignore)")
        else:
            print(f"({i},{j}) = {product}")
            sum += product
        j += 1
    i +=1
print("sim of unique products: ",sum)
