temps = input("Enter temperatures in F (separate them with ,): ")
temps += ','
sum = 0.0
count = 0
current = ''
for char in temps:
    if char != ',':
        current += char
    else:
        if current != '':
            sum += float(current)
            count += 1
            current = ''
average = sum / count if count > 0 else 0
print(f"You've entered {count} temperature points.")
print(f"The average temperature is {average:.2f}F")
