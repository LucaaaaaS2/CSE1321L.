def validate(message, offset):
    if offset < 0 or offset > 26:
        return False
    for letter in message:
        if not (letter.isalpha() or letter == " "):
            return False
    return True

def encrypt(message, offset):
    message = message.upper()
    result = ""
    for letter in message:
        if letter == " ":
            result += " "
        else:
            new_code = ord(letter) + offset
            if new_code > ord('Z'):
                new_code -= 26
            result += chr(new_code)
    return result

def main():
    while True:
        message = input("Enter your message:\n ")
        try:
            offset = int(input("Enter your offset value: "))
        except:
            print("Sorry, we can only process messages with letters and spaces, and the offset must be between 0 and 26.")
            continue
        if not validate(message, offset):
            print("Sorry, we can only process messages with letters and spaces, and the offset must be between 0 and 26.")
        else:
            secret = encrypt(message, offset)
            print("Your secret message is....")
            print(secret)
        again = input("Do you want to encrypt another message? (Y/N): ").upper()
        if again == "N":
            print("Closing out...")
            break

main()







