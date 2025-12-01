print("[Welcome to the Letter Frequency Quiz]")
stc = input("Enter a sentence(lowercase letters only): ")
stc_no = ("")
i = 0
while i < len(stc):
    if stc[i] != "":
        stc_no += stc[i]
    i +=1
processed = ""
i = 0
while i < len(stc_no):
    letter = stc_no[i]
    done = False
    j = 0
    while j < len(processed):
        if processed[j] == letter:
            done = True
            break
        j += 1
    if not done:
        count = 0
        k = 0
        while k < len(stc_no):
            if stc_no[k] == letter:
                count += 1
            k += 1
        while True:
            guess = int(input(f"Guess the frequency of letter '{letter}"))
            if guess > count:
                print("Too high!")
            elif guess < count:
                print("Too low!")
            else:
                print("Correct!")
                break
        processed += letter
    i += 1
print("Congratulations! You completed the quiz.")
