#Sandwiches
s = int(input("Enter the number of small sandwiches:"))
m = int(input("Enter the number of medium sandwiches:"))
l = int(input("Enter the number of large sandwiches:"))
xl = int(input("Enter the number of extra-large sandwiches:"))
print(f"You've entered {s} small sandwiches.")
print(f"You've entered {m} medium sandwiches.")
print(f"You've entered {l} large sandwiches.")
print(f"You've entered {xl} extra-large sandwiches.")
s = s * 30
m = m * 60
l = l * 75
xl = xl * 135
tt = s + m + l + xl
min = tt / 60
min = int(min)
sec = tt % 60
sec = int(sec)
print(f"Total cooking time is {min} minutes and {sec} seconds.")
