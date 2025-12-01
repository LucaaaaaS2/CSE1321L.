def find_frequency(data):
    freq = {}
    for item in data:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
while True:
    print("Main Menu")
    print("1. Enter letters")
    print("2. Enter numbers")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        letters = input("Enter letters separated by commas: ")
        data = tuple(letters.split(","))
    elif choice == "2":
        numbers = input("Enter numbers separated by commas: ")
        data = tuple(int(x) for x in numbers.split(","))
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")
        continue

    freq_dict = find_frequency(data)
    max_freq = max(freq_dict.values())
    most_frequent = [str(k) for k, v in freq_dict.items() if v == max_freq]

    print("Tuple:", data)
    print("Frequency dictionary:", freq_dict)
    print("Most frequent element(s):", ", ".join(most_frequent))
    print("Frequency:", max_freq)