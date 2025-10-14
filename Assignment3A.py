print("[Pyramid Pattern]")
str = input("Enter a string: ")
no = ""
for ch in str:
    if ch != " ":
        no += ch
result = ""
for ch in no:
    result += ch
    print(result)

